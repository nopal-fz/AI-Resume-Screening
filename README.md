# Smart HR: CV Screening and Candidate Fit

🚀 **Smart HR** adalah aplikasi berbasis **Streamlit** yang membantu tim HR dalam proses **screening CV** dan mencocokkan kandidat dengan pekerjaan yang tersedia menggunakan **AI & NLP**. Aplikasi ini juga menyediakan fitur **chatbot interaktif** untuk menjawab pertanyaan tentang isi CV kandidat.

## ✨ Fitur Utama
- **📄 CV Parsing**: Ekstraksi teks otomatis dari file PDF.
- **🔍 Gap Analysis**: Analisis kesenjangan keterampilan antara kandidat dan deskripsi pekerjaan.
- **🤖 AI Chatbot**: Berinteraksi dengan CV menggunakan model **Ollama (Mistral LLM)**.
- **📌 Job Matching**: Mencocokkan kandidat dengan pekerjaan terbaik berdasarkan skill dan pengalaman.
- **🔎 Semantic Search**: Menggunakan **FAISS** untuk pencarian informasi dari CV kandidat.

## 📦 Teknologi yang Digunakan
- **Python**
- **Streamlit**
- **FAISS (Facebook AI Similarity Search)**
- **LangChain**
- **Ollama LLM (Mistral)**
- **PyPDF2**
- **NumPy**

## 🚀 Instalasi dan Menjalankan Aplikasi
### 1️⃣ Clone Repository
```bash
git clone https://github.com/username/smart-hr-cv-screening.git
cd smart-hr-cv-screening
```

### 2️⃣ Install Dependencies
Disarankan menggunakan virtual environment:
```bash
pip install -r requirements.txt
```

### 3️⃣ Jalankan Aplikasi
```bash
streamlit run app.py
```

## 📁 Struktur Direktori
```
📂 smart-hr-cv-screening
│── 📂 data                   # Data JSON untuk daftar pekerjaan
│── 📂 models                 # Model AI untuk analisis gap & matching
│── 📂 utils                  # Utility functions untuk preprocessing teks & embedding
│── 📄 app.py                 # Main Streamlit app
│── 📄 requirements.txt       # Dependencies
│── 📄 README.md              # Dokumentasi proyek
```

## 🤖 Cara Menggunakan AI Chatbot
Setelah **CV diunggah**, pengguna dapat **bertanya tentang isi CV** dengan beberapa contoh pertanyaan berikut:
- "Siapa nama kandidat di CV ini?"
- "Apa posisi terakhir yang dipegang oleh kandidat?"
- "Berapa tahun pengalaman kerja kandidat?"
- "Apakah kandidat memiliki pengalaman dalam Python dan Machine Learning?"

## 💡 Catatan
- Pastikan **Ollama LLM (Mistral)** sudah berjalan secara lokal.
- Gunakan **Streamlit Cloud** atau **Docker** untuk deployment lebih fleksibel.

## 🏆 Kontribusi
Pull request selalu diterima! Jika ingin berkontribusi, silakan fork proyek ini dan buat **PR**.

## 📞 Kontak
👤 **Naufal Faiz**  
🔗 [LinkedIn](www.linkedin.com/in/naufal-faiz-nugraha-867534292)

---
🚀 *Smart HR – Membantu HR dalam menemukan kandidat terbaik dengan AI!*
