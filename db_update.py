#update register 
def searchId (id, action, old='', new=''):



    #Save ids in the db
    with open("DB.txt", "r", encoding="utf-8") as f:
        ids = []
        for line in f:
            ids.append(line.split(None, 1)[0])

    #Search if the id exist the coma is with the id

    if id in ids:


        #Found the line in the txt file
        pos = 0

        for i in ids:
            if i == id:
                break
            pos = pos + 1

        

        #Printing the line to update
        doc = open("DB.txt", "r", encoding= "utf-8")
        line = doc.readlines()
        doc.close()
        print(line[pos])

        #Update the register
        if action == 'update':
            update(pos, old, new)
        
        #Delete the register
        if action == 'delete':
            delete(pos)
        
        if action == 'generate':
            generate(pos)
        

    else:
        print("the value does not exist")

def update(line, old, new):
    

    with open("DB.txt", "r", encoding="utf-8") as f:
        data = f.readlines()

    #New data to update
    newdata = data[line].replace(old , new)

    #Assing the new data
    data[line] = newdata

    #Write in the DB.txt
    with open("DB.txt", "w", encoding="utf-8") as f:
        f.writelines(data)


    print("data updated: " + newdata)

    with open("updates.txt", "a", encoding="utf-8") as f:
        f.write(newdata)
    

def delete(delreg):
    print("line to delete: " + str(delreg))
    

    try: 
        with open("DB.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        deletefile = lines[delreg]
        pos = 0
        with open("DB.txt", "w", encoding="utf-8") as fw:

            for line in lines:

                if pos != int(delreg):
                    fw.write(line)

                pos += 1

            with open("deletes.txt", "a", encoding="utf-8") as f:
                f.write(deletefile)
            
            print("Register deleted successfully")

    except:
        print("Something went wrong with the DB file")


def generate(pos):
    print("generating certificate...\n")
    

    try: 
        with open("DB.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()

            array = lines[pos].split(",")
            
            fin = open("constancia.txt", "rt", encoding= "utf-8")
            
            fout = open(array[0]+".txt", "wt", encoding= "utf-8")
            
            for line in fin:
                fout.write(line.replace("INSTITUTO", array[1]).replace(
                    "NOMBRE", array[2]).replace("REGISTRO", array[3]).replace(
                        "CARRERA", array[4]).replace("DURACION", array[5]).replace(
                            "ACTUAL", array[6]).replace("FECHA", array[7]).replace(
                                "RESPONSABLE", array[8]).replace("CARGO", array[9]).replace(
                                    "CORREO", array[10]).replace("TELEFONO", array[11]).replace(
                                        "DOMICILIO", array[12]).replace("COLONIA",array[13]).replace(
                                            "CP", array[14]))

            fin.close()
            fout.close()
            print("CERTIFICATE GENERATED SUCCESSFULLY")

    except:
        print("Something went wrong with the DB file")

    #Split the line register
