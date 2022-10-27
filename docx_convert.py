from docx import Document
import os

#Function to convert txt file to doc send the txt path and the new name of the docx
def docxConvert(path, filename):
    doc = Document()
    

    with open(path, "r", encoding= "utf-8") as openfile:
        line = openfile.read()
        doc.add_paragraph(line)
        doc.save(filename + ".docx")

    os.system(filename + ".docx")


