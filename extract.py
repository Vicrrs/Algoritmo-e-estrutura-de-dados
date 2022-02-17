from typing import Text
import PyPDF2

pdfFileObj = open("xxx.pdf", "rb")

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage(1)

text = pageObj.extractText()

print(text)