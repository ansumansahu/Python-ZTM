from csv import reader
from pydoc import pager
import PyPDF2

with open('dummy.pdf','rb') as file:
    #rb-read binary converts file object to binary 
    reader= PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    
    page=reader.getPage(0)
    page.rotateCounterClockwise(180)
    writer= PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('rotated.pdf','wb') as new_file:
        writer.write(new_file)