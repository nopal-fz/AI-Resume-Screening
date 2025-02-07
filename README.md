# Smart HR: CV Screening and Candidate Fit

🚀 **Smart HR** is a **Streamlit** based application that helps HR teams in the process of **CV screening** and matching candidates with available jobs using **AI & NLP**. This application also provides an **interactive chatbot** feature to answer questions about the contents of the candidate's CV.

## ✨ Key Features
- **📄 CV Parsing**: Automatic text extraction from PDF files.
- **🔍 Gap Analysis**: Analyze the skill gap between candidates and job descriptions.
- **🤖 AI Chatbot**: Interact with CVs using the **Ollama (Mistral LLM)** model.
- **📌 Job Matching**: Match candidates with the best jobs based on skills and experience.
- **🔎 Semantic Search**: Uses **FAISS** to search for information from candidate CVs.

## 📦 Technologies Used
- **Python**
- **Streamlit**
- **FAISS (Facebook AI Similarity Search)**
- **LangChain**
- **Ollama LLM (Mistral)**
- **PyPDF2**
- **NumPy**

## 🚀 Installing and Running the Application
### 1️⃣ Clone Repository
```bash
git clone https://github.com/username/smart-hr-cv-screening.git
cd smart-hr-cv-screening
```

### 2️⃣ Install Dependencies
It is recommended to use a virtual environment:
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application
```bash
streamlit run app.py
```

## 📁 Structure Directory
```
📂 smart-hr-cv-screening
│── 📂 data # JSON data for job listings
│── 📂 models # AI models for gap analysis & matching
│── 📂 utils # Utility functions for text preprocessing & embedding
│── 📄 app.py # Main Streamlit app
│── 📄 requirements.txt # Dependencies
│── 📄 README.md # Project documentation
```

## 🤖 How to Use AI Chatbot
After **CV is uploaded**, users can **ask about the CV** with some sample questions:
- "What is the candidate's name on this CV?"
- "What was the last position held by the candidate?"
- "How many years of work experience does the candidate have?"

- "Does the candidate have experience in Python and Machine Learning?"

## 💡 Note
- Make sure **Ollama LLM (Mistral)** is running locally.
- Use **Streamlit Cloud** or **Docker** for more flexible deployment.

## 🏆 Contribution
Pull requests are always welcome! If you want to contribute, please fork this project and create a **PR**.

## 📞 Contact
👤 **Naufal Faiz**
🔗 [LinkedIn](www.linkedin.com/in/naufal-faiz-nugraha-867534292)

---
🚀 *Smart HR – Helping HR find the best candidates with AI!*
