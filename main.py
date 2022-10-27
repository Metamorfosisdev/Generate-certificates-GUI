import PySimpleGUI as sg
import os

from count_lines import newId
from add_register import addRegister
from db_update import searchId
from docx_convert import docxConvert
from pdf_convert import pdfConvert
from split import generateCertificates


def pdf_window():

    layout = [
        [sg.Text("Enter register certificate + .txt",size=(20,1)), sg.InputText()],
        [sg.Text("Enter the new pdf name",size=(20,1)), sg.InputText()],
        [sg.Button("Submit", key="submit", size=(210,1))],
        [sg.Button("Cancel", key="cancel", size=(210,1))],
    ]

    window = sg.Window("Pdf converter", layout, size = (420, 450))
    while True:
        event, values = window.read()

        if event == "cancel" or event == sg.WIN_CLOSED:
            break
        if event == "submit":
            path = values[0]
            filename = values[1]
            pdfConvert(os.getcwd()+ "\\" + path, filename)
            break
            
    window.close()


def docx_window():

    layout = [
        [sg.Text("Enter register certificate",size=(10,1)), sg.InputText()],
        [sg.Text("Enter the docx name:",size=(10,1)), sg.InputText()],
        [sg.Button("Submit", key="submit", size=(210,1))],
        [sg.Button("Cancel", key="cancel", size=(210,1))],
    ]

    window = sg.Window("Docx converter", layout, size = (420, 450))
    while True:
        event, values = window.read()

        if event == "cancel" or event == sg.WIN_CLOSED:
            break
        if event == "submit":
            path = values[0]
            filename = values[1]
            docxConvert(os.getcwd() + "\\" + path, filename)
            break
            
    window.close()




def generate_window():
    
    with open("DB.txt","r",encoding="utf8") as f:
        text = f.read()
        popup_text("DB.txt", text)

    layout = [
        [sg.Text("Enter register",size=(10,1)), sg.InputText()],
        [sg.Button("Submit", key="submit", size=(210,1))],
        [sg.Button("Cancel", key="cancel", size=(210,1))],
    ]

    window = sg.Window("Generate certificates", layout, size = (420, 450))
    while True:
        event, values = window.read()

        if event == "cancel" or event == sg.WIN_CLOSED:
            break
        if event == "submit":
            
            certificates = values[0] + ","
            
            generateCertificates(certificates)

            with open(values[0] + ".txt","r",encoding="utf8") as f:
                text = f.read()
                popup_text( values[0]+ ".txt", text)


            break
            
    window.close()



def delete_window():

    with open("DB.txt","r",encoding="utf8") as f:
        text = f.read()
        popup_text("DB.txt", text)

    layout = [
        [sg.Text("Enter register",size=(10,1)), sg.InputText()],
        [sg.Button("Submit", key="submit", size=(210,1))],
        [sg.Button("Cancel", key="cancel", size=(210,1))],
    ]

    window = sg.Window("Update register", layout, size = (420, 450))
    while True:
        event, values = window.read()

        if event == "cancel" or event == sg.WIN_CLOSED:
            break
        if event == "submit":
            
            delreg = str(values[0]) + ","

            searchId(delreg, "delete")

            
            break
            
    window.close()
#####DELETE

def upload_window():


    layout = [
        [sg.Text("INSTITUTO", size=(10,1)), sg.InputText()],
        [sg.Text("NOMBRE",size=(10,1)), sg.InputText() ],
        [sg.Text("REGISTRO",size=(10,1)), sg.InputText()],
        [sg.Text("CARRERA",size=(10,1)), sg.InputText()],
        [sg.Text("DURACION",size=(10,1)), sg.InputText()],
        [sg.Text("ACTUAL",size=(10,1)), sg.InputText()],
        [sg.Text("FECHA",size=(10,1)), sg.InputText()],
        [sg.Text("RESPONSABLE",size=(13,1)), sg.InputText()],
        [sg.Text("CARGO",size=(10,1)), sg.InputText()],
        [sg.Text("CORREO",size=(10,1)), sg.InputText()],
        [sg.Text("TELEFONO",size=(10,1)), sg.InputText()],
        [sg.Text("DOMICILIO",size=(10,1)), sg.InputText()],
        [sg.Text("COLONIA",size=(10,1)), sg.InputText()],
        [sg.Text("CP",size=(10,1)), sg.InputText()],
        [sg.Button("Submit", key="submit", size=(210,1))],
        [sg.Button("Cancel", key="cancel", size=(210,1))],
    ]

    window = sg.Window("Upload new register", layout, size = (420, 450))
    while True:
        event, values = window.read()

        if event == "cancel" or event == sg.WIN_CLOSED:
            break
        if event == "submit":
            id = newId()
            instituto =values[0]
            nombre =values[1]
            registro =values[2]
            carrera =values[3]
            duracion =values[4]
            actual =values[5]
            fecha =values[6]
            responsable =values[7]
            cargo =values[8]
            correo =values[9]
            telefono =values[10]
            domicilio =values[11]
            colonia =values[12]
            cp =values[13]
            addRegister(id, instituto, nombre, registro, carrera, duracion, actual, fecha, responsable, cargo, correo, telefono, domicilio, colonia, cp)
            sg.popup("Register successfully")
            break
            
    window.close()

def popup_text(filename, text):

    layout = [
        [sg.Multiline(text, size=(80, 25)),],
    ]
    win = sg.Window(filename, layout, modal=True, finalize=True)

    while True:
        event, values = win.read()
        if event == sg.WINDOW_CLOSED:
            break
    win.close()

def update_window():

    with open("DB.txt","r",encoding="utf8") as f:
        text = f.read()
        popup_text("DB.txt", text)

    layout = [
        [sg.Text("Enter register",size=(10,1)), sg.InputText()],
        [sg.Text("Word to change",size=(10,1)), sg.InputText()],
        [sg.Text("New word",size=(10,1)), sg.InputText()],
        [sg.Button("Submit", key="submit", size=(210,1))],
        [sg.Button("Cancel", key="cancel", size=(210,1))],
    ]

    window = sg.Window("Update register", layout, size = (420, 450))
    while True:
        event, values = window.read()

        if event == "cancel" or event == sg.WIN_CLOSED:
            break
        if event == "submit":
            
            upreg = str(values[0]) + ","
            old = str(values[1])
            new = str(values[2])
            #Search ID and if it exist it will be updated and added to updates.txt
            searchId(upreg, "update", old, new)
            print("Successfully updated")
            break
            
    window.close()

def main():
    # Add some color
    # to the window
    sg.theme('SandyBeach')     
    
    # Very basic window.
    # Return values using
    # automatic-numbered keys
    layout = [
        [sg.Text('Certificates converter')],
        [sg.Button('Upload', size =(300, 1), key = 'upload'), ],
        [sg.Button('Update', size =(300, 1), key = 'update')],
        [sg.Button('Delete', size =(300, 1), key = 'delete')],
        [sg.Button('Generate certificates', size =(300, 1),key = 'generate')],
        [sg.Button('Show updates and deletes', size =(300, 1),key = 'activity')],
        [sg.Button('pdf converter', size =(300, 1),key = 'pdf')],
        [sg.Button('docx converter', size =(300, 1),key = 'docx')],
    ]
    
    window = sg.Window('Certificates converter', layout, size = (500, 300))
    while True:
            event, values = window.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
            if event == "upload":
                upload_window()
            
            if event == "update":
                update_window()
            
            if event == "delete":
                delete_window()

            if event == "generate":
                generate_window()

            if event == "activity":

                with open("deletes.txt","r",encoding="utf8") as f:
                    text = f.read()
                    popup_text("deletes.txt", text)

                with open("updates.txt","r",encoding="utf8") as f:
                    text = f.read()
                    popup_text("updates.txt", text)
            
            if event == "pdf":
                pdf_window()
            
            if event == "docx":
                docx_window()

    window.close()

    



if __name__ == '__main__':
    main()