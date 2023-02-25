# extract_doc_info.py

from PyPDF2 import *

filePath = "source/sheets/character_sheet.pdf"

file = open(filePath, "rb")
pdfReader = PdfReader(file)

for object in pdfReader.get_object():
    print(object)