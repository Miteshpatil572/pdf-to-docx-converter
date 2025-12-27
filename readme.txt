📄 PDF to DOCX Converter

A simple Django web application that converts PDF files into editable DOCX documents.
This project demonstrates file upload handling, third-party library integration, and basic frontend styling using Django.

🚀 Features

Upload PDF files through a web form

Convert PDF to DOCX format

Download converted DOCX file

Simple and clean UI

Works best with text-based PDFs

🛠 Tech Stack

Backend: Python, Django

Frontend: HTML, CSS

Library: pdf2docx

Version Control: Git & GitHub

📂 Project Structure
pdfconverter/
│
├── converter/
│   ├── templates/
│   │   └── converter/
│   │       └── upload.html
│   ├── static/
│   │   └── css/style.css
│   ├── views.py
│   └── urls.py
│
├── pdfconverter/
│   ├── settings.py
│   └── urls.py
│
├── media/
│   ├── uploaded_pdfs/
│   └── converted_docs/
│
├── manage.py
└── README.md

⚙️ Installation & Run
1️⃣ Clone Repository
git clone https://github.com/Miteshpatil572/pdf-to-docx-converter.git
cd pdf-to-docx-converter

2️⃣ Install Dependencies
pip install django pdf2docx

3️⃣ Run Server
python manage.py runserver

4️⃣ Open Browser
http://127.0.0.1:8000/

🔄 How It Works

User uploads a PDF file

Django saves the file to the media directory

pdf2docx converts the PDF into DOCX

User downloads the converted file

⚠️ Limitations

Image-based PDFs are not supported

Complex formatting may not convert perfectly

🔮 Future Improvements

Support for scanned PDFs (OCR)

Drag & drop upload

Deployment on cloud (Render / Railway / AWS)

👨‍💻 Author

Mitesh Patil
Java & Python Developer
🔗 GitHub: https://github.com/Miteshpatil572