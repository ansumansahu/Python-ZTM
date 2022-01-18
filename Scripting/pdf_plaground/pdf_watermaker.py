from re import template
from unittest import main
import PyPDF2

wtr= PyPDF2.PdfFileReader('wtr.pdf','rb')
mainfile= PyPDF2.PdfFileReader('merged.pdf','rb')
watermark_pdf= PyPDF2.PdfFileWriter()

for pages in range(mainfile.numPages):
    page=mainfile.getPage(pages)
    page.mergePage(wtr.getPage(0))
    watermark_pdf.addPage(page)

with open('watermark.pdf','wb')as file:
    watermark_pdf.write(file)