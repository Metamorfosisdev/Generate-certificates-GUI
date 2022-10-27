#Obtain the new id
def newId():

    #Open DB
    file = open('DB.txt', 'r', encoding="utf-8")

    #count the lines in the DB
    content = file.readlines()

    #close the file
    file.close()

    #save the last register
    lastLine = content[len(content)-1]

    #save the last id
    id = lastLine.split(",")

    newId = int(id[0]) + 1

    
    return newId

