# 📚 Story Narrator🎧

A simple web application that converts PDF files into audio using Python (FastAPI, gTTS) and a basic HTML + JS frontend.

---

## 🚀 Features

- Upload a PDF file from your browser
- Extracts text from the PDF file
- Converts extracted text to speech using Google Text-to-Speech (gTTS)
- Plays the generated audio directly in the browser
- Clean and simple interface

---

## 🛠️ Tech Stack

- **Backend:** Python, FastAPI, PyPDF2, gTTS
- **Frontend:** HTML, CSS, JavaScript (Vanilla)
- **Extras:** UUID for unique audio filenames, CORS for frontend-backend communication

---

## 📁 Folder Structure

```
pdf-to-audio-app/
├── backend/
│   ├── main.py               # FastAPI app
│   ├── requirements.txt      # Python dependencies
│   ├── audio/                # Output audio files (.mp3)
│   └── venv/                 # Python virtual environment (optional)
├── frontend/
│   ├── index.html            # Main webpage
│   ├── script.js             # JavaScript to handle uploads and play audio
│   └── style.css             # Styles for the webpage
```

---

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pdf-to-audio-app.git
cd pdf-to-audio-app
```

### 2. Set Up and Start Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate       # Windows
# source venv/bin/activate  # macOS/Linux

pip install -r requirements.txt
uvicorn main:app --reload
```

FastAPI backend will run on:  
**http://127.0.0.1:8000**

---

### 3. Run the Frontend

Open a new terminal:

```bash
cd frontend
start index.html
```

Or just double-click `index.html` to open in your browser.

---

## 📦 Requirements

Contents of `requirements.txt`:

```
fastapi
uvicorn
PyPDF2
gTTS
```

Generate automatically:

```bash
pip freeze > requirements.txt
```

---

## 📸 Preview

_A screenshot or preview GIF of the web app could go here._

---

## 📝 Notes

- Ensure the PDF contains **selectable text** (not just scanned images).
- gTTS requires an **internet connection** to access Google APIs.
- The generated MP3 files are saved in the `/backend/audio/` folder.

---

## 🤝 Contributions

Contributions, issues, and feature requests are welcome!  
Feel free to fork and submit a pull request.

---

## 📃 License

This project is licensed under the MIT License.
```

---

