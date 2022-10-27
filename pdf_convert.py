from fpdf import FPDF
import os



def pdfConvert(path, filename):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size = 12)


    with open(path, 'r', encoding= 'utf-8') as f1:
    
        for l1 in f1:
            pdf.cell(180, 5, txt = l1, ln = 1, align = 'C') 

        pdf.output(filename + ".pdf")
        os.system(filename + ".pdf")
   
   


