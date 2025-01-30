import streamlit as st
import json
import numpy as np
import faiss
from utils.text_processing import extract_text_from_pdf
from utils.embedding import get_embeddings
from models.gap_analysis import analyze_gap, adaptive_matching
from streamlit_pdf_viewer import pdf_viewer
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents import Document
from langchain_core.runnables import RunnablePassthrough

# fungsi untuk membaca daftar pekerjaan dari JSON
def load_available_jobs():
    with open('data\\available_jobs.json', 'r') as file:
        jobs = json.load(file)
    return jobs

# inisialisasi session state untuk menyimpan hasil analisis dan riwayat chat
if "gap_score" not in st.session_state:
    st.session_state.gap_score = None
if "best_match" not in st.session_state:
    st.session_state.best_match = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# title aplikasi
st.markdown("<h1 style='text-align: center;'>Smart HR: CV Screening and Candidate Fit</h1>", unsafe_allow_html=True)
st.caption("Aplikasi ini membantu HR dalam proses screening CV dan mencocokkan kandidat dengan pekerjaan yang tersedia.")

# sidebar untuk input file dan job description
with st.sidebar:
    st.header('Upload CV dan Job Description')
    uploaded_cv = st.file_uploader('Upload CV (PDF)', type=['pdf'])
    uploaded_jd = st.text_area('Job Description')

    if uploaded_cv:
        # preview CV di sidebar
        binary_data = uploaded_cv.getvalue()
        pdf_viewer(input=binary_data, width=700)

    analyze_button = st.button('Analyze')
    add_vertical_space(12)
    st.write('Made with ❤️ by [Naufal Faiz](www.linkedin.com/in/naufal-faiz-nugraha-867534292)')

# jika tombol analyze ditekan akan menyimpan ke session state
if analyze_button and uploaded_cv and uploaded_jd:
    cv_text = extract_text_from_pdf(uploaded_cv)
    cv_embeddings = get_embeddings(cv_text)
    jd_embeddings = get_embeddings(uploaded_jd)

    st.session_state.gap_score = analyze_gap(cv_embeddings, jd_embeddings)
    available_jobs = load_available_jobs()
    st.session_state.best_match = adaptive_matching(cv_text, available_jobs)

    # simpan teks CV ke session_state agar bisa dipakai chatbot
    st.session_state.cv_text = cv_text

# menampilkan hasil analisis jika sudah tersedia
if st.session_state.gap_score is not None and st.session_state.best_match is not None:
    # show result gap score dan best match job
    st.markdown(f"<h6 style='text-align: center;'>Gap Score: {st.session_state.gap_score}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \
        |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Best Match: {st.session_state.best_match['title']}</h6>", unsafe_allow_html=True)

# chatbot Setup
st.markdown("---")

# jika file CV sudah ada, proses untuk chatbot
if "cv_text" in st.session_state:
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = [Document(page_content=chunk) for chunk in text_splitter.split_text(st.session_state.cv_text)]

    # FAISS Index setup
    doc_texts = [doc.page_content for doc in chunks]
    doc_embeddings = np.array([get_embeddings(text) for text in doc_texts]).astype('float64')
    index = faiss.IndexFlatL2(doc_embeddings.shape[1])
    index.add(doc_embeddings)

    # inisialisasi LLM Ollama
    local_model = "mistral"
    llm = ChatOllama(model=local_model)

    # chat input
    user_input = st.chat_input("Ask a question about the CV...")

    # jika ada input, cari jawaban model llm dan FAISS
    if user_input:
        user_embedding = np.array(get_embeddings(user_input)).astype('float64').reshape(1, -1)
        _, I = index.search(user_embedding, k=3)

        retrieved_docs = [doc_texts[i] for i in I[0]]
        context = "\n\n".join(retrieved_docs)

        prompt = ChatPromptTemplate.from_template('''
            Anda adalah seorang asisten HR yang membantu dalam proses screening CV. Format informasi yang diambil dalam bentuk teks.
            
            Gunakan hanya konteks jawaban dari CV untuk menjawab pertanyaan user. Jawaban harus informatif dan sesuai dengan pertanyaan user.
            Jawab menggunakan bahasa indonesia yang baik dan benar.
            
            question: "{question}"
            
            context: "{context}"
        '''
        )

        chain = (
            RunnablePassthrough()
            | {"context": lambda x: x["context"], "question": lambda x: x["question"]}
            | prompt
            | llm
            | StrOutputParser()
        )

        response = chain.invoke({"context": context, "question": user_input})


        # Simpan chat ke session state
        st.session_state.chat_history.append((user_input, response))

# Tampilkan riwayat chat
for user_q, bot_a in st.session_state.chat_history:
    with st.chat_message("user"):
        st.write(user_q)
    with st.chat_message("assistant"):
        st.write(bot_a)