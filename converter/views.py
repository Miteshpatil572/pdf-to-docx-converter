# converter/views.py

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from pdf2docx import Converter
import os
from django.conf import settings

def upload_pdf(request):
    docx_file = None
    message = ''
    
    if request.method == 'POST' and request.FILES.get('pdf_file'):
        pdf_file = request.FILES['pdf_file']
        fs = FileSystemStorage()
        filename = fs.save(pdf_file.name, pdf_file)
        uploaded_file_url = fs.url(filename)

        # Convert PDF to DOCX
        pdf_path = os.path.join(settings.MEDIA_ROOT, filename)
        docx_filename = filename.replace('.pdf', '.docx')
        docx_path = os.path.join(settings.MEDIA_ROOT, docx_filename)

        cv = Converter(pdf_path)
        cv.convert(docx_path)
        cv.close()

        docx_file = fs.url(docx_filename)
        message = "Conversion successful!"

    return render(request, 'converter/upload.html', {'docx_file': docx_file, 'message': message})
