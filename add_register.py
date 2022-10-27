
#Adding new register



def addRegister(id, instituto, nombre, registro, carrera, duracion, actual, fecha, responsable, cargo, correo, telefono, domicilio, colonia, cp):
    #add =  str(id) + ", UNE, SUSANA AURORA NIEVES REYES, 3271928, QUIMICO FARMACO BIOLOGO, 9, 8, 19 Octubre 22, ING. RAUL ESPINAL, SUBDIRECTOR, raul@gmail.com, 3316306555, Prolongacion Revolucion, Nextipac, 42115, \n"

    text = str(id) + ", " + instituto + ", " + nombre + ", " + registro + ", " + carrera + ", "+ duracion + ", " + actual + ", " + fecha + ", " + responsable + ", " + cargo + ", " + correo + ", " + telefono + ", " + domicilio + ", " + colonia + ", " + cp + ", \n"

    db = open("DB.txt", "a", encoding="UTF-8")

    db.write(text)

    db.close()

    print("You added new register successfully")


#addRegister(20, "CUAUTEMOC", "RUBI ESPINAL FLORES", "14301085", "INGENIERIA FORECENCE", "9", "5", "20 Octubre 2022", "ING. AHTZIRY", "DIRECTORA", "aht@hotmail.com", "3320912074", "Prolo. Revolcion", "Nextipac", "45220")