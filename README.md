# 📝 OCR Web Application (Flask + Tesseract)

A web-based **Optical Character Recognition (OCR)** application that extracts text from uploaded images and converts it into structured JSON format.

---

## 🚀 Features

- 📷 Upload image files (PNG, JPG, JPEG)
- 🔍 Extract text using Tesseract OCR
- 🧹 Clean and preprocess extracted text
- 🗂 Convert extracted text into structured JSON
- 🌐 Interactive web interface using Flask
- ⚡ Lightweight and fast execution

---

## 🛠️ Tech Stack

- Python
- Flask
- Tesseract OCR
- Pytesseract
- Pillow (PIL)
- Regex (re module)

---

## 📂 Project Structure

OCR-Flask-App/
│
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md

---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository

git clone https://github.com/your-username/ocr-flask-app.git  
cd ocr-flask-app

### 2️⃣ Install Dependencies

pip install -r requirements.txt

### 3️⃣ Install Tesseract OCR

#### Windows:
Download from:
https://github.com/tesseract-ocr/tesseract

After installation, add Tesseract to your system PATH.

If needed, specify the path inside app.py:

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#### Ubuntu:

sudo apt update  
sudo apt install tesseract-ocr

---

## ▶️ Run the Application

python app.py

Then open your browser and visit:

http://127.0.0.1:5000/

---

## 🧠 How It Works

1. User uploads an image through the web interface.
2. Flask receives the file.
3. The image is processed using pytesseract.
4. Extracted text is cleaned and structured.
5. Output is returned in JSON format and displayed on the webpage.

---

## 🖼️ Example Output

{
  "Name": "John Doe",
  "Invoice Number": "INV1234",
  "Amount": "₹2500"
}

---

## 📌 Possible API Endpoint (Optional)

If implemented:

@app.route("/api/ocr", methods=["POST"])

Endpoint URL:

http://127.0.0.1:5000/api/ocr

---

## 🔥 Future Improvements

- Add PDF support
- Improve OCR accuracy with preprocessing
- Add authentication system
- Store results in database (MongoDB/PostgreSQL)
- Deploy to AWS / Render / HuggingFace

---

## 💼 Resume Value

This project demonstrates:

- Backend development using Flask
- OCR pipeline implementation
- File handling and image processing
- Data structuring using JSON
- Building and running a local web server

---

## 👩‍💻 Author

Namradha Mani  
Aspiring Cloud & Data Engineer  
Focused on ML Deployment, APIs, and Automation Systems
