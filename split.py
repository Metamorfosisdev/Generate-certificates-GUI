from db_update import searchId

def generateCertificates(uIds):


    #Save into array all id that will be certificates
    Uarray = uIds.split()

    for i in Uarray:
        searchId(i, "generate")
    

