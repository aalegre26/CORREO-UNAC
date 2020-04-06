import os
from secrets import choice
import csv
import time


"""
#abc = os.system('gam print users allfields > users.csv')



with open('users.csv',encoding="utf-8-sig") as csvarchivo:
    #ARCHIVO CON LA DATA
    entrada = csv.DictReader(csvarchivo)
    #ARCHIVO DE SALIDA
    #csvsalida = open('uemailADM.csv', 'w', newline='')
    #salida = csv.writer(csvsalida)

    for fila in entrada:
        Lname = fila['name.familyName']
        Fname = fila['name.givenName']
        email = fila['primaryEmail']
        print(Fname + " - " + Lname + " - " + email)

del entrada
"""

def menu():
    print("##############################################################")
    print("           CORREOS INSTITUCIONALES UNAC.EDU.PE                ")
    print("")
    print("Obtener los correos actuales  ------------------ [1]")


    

def createFileUser():
    tm = time.localtime()
    year = tm[0]
    mon = tm[1]
    day = tm[2]
    hour = tm[3]
    mint = tm[4]

    file = "usuarios-"+day+mon+year+"-"+hour+mint 
    print(file)
    #os.system('gam print users allfields > users.csv')
    
    

def main():
    menu()

main()




















"""
from subprocess import PIPE, Popen

#proceso = Popen(['ping 8.8.8.8'], stdout=PIPE, stderr=PIPE)
proceso = Popen('cls')
proceso.wait()

error_encontrado = proceso.stderr.read()
proceso.stderr.close()

listado = proceso.stdout.read()
proceso.stdout.close()

if not error_encontrado: 
    print (listado) 
else: 
    print ("Se produjo el siguiente error:\n%s" % error_encontrado)



import os

#print (os.listdir('.'))
#os.system('ping 8.8.8.8')
var = os.popen('ping 8.8.8.8')
print(var)

#gam info user aealegreq@unac.edu.pe
""
from secrets import choice
import csvgam info user aealegreq@unac.edu.pe

PASS = ''

def passSure():
    caracteres = 'ABCDEFHKMNPRTXY34578'
    longitud = 8  # La longitud que queremos
    cadena_aleatoria = ''.join(choice(caracteres) for caracter in range(longitud))
    return cadena_aleatoria

def removeCharSpecial(cad):
    origin = "áàäéèëíìïóòöúùuüñÁÀÄÉÈËÍÌÏÓÒÖÚÙÜÑçÇ"
    ascii = "aaaeeeiiiooouuuunAAAEEEIIIOOOUUUNcC"
    output = cad

    for i in range(len(origin)):
         output = output.replace(origin[i], ascii[i])
    output = output.lower()

    return output

def createEmail():
    return 1


with open('DATA1.csv') as csvarchivo:
    #ARCHVIO CON LA DATA
    entrada = csv.DictReader(csvarchivo)
    #ARCHIVO DE SALIDA
    csvsalida = open('uemailADM1.csv', 'w', newline='')
    salida = csv.writer(csvsalida)


    salida.writerow(["First Name [Required]","Last Name [Required]","Email Address [Required]","Password [Required]","Password Hash Function [UPLOAD ONLY]","Org Unit Path [Required]","New Primary Email [UPLOAD ONLY]","Home Secondary Email","Work Secondary Email","Work Phone","Home Phone","Mobile Phone","Work Address","Home Address","Employee ID","Employee Type","Employee Title","Manager Email","Department","Cost Center","Building ID","Floor Name","Floor Section","Change Password at Next Sign-In"])

    for reg in entrada:
        Lname = reg['PATERNO'] + " " + reg['MATERNO']
        Fname = reg['NAME']

        apeP = removeCharSpecial(reg['PATERNO']).replace(' ','')
        apeM = removeCharSpecial(reg['MATERNO'])[0:1]
        name = removeCharSpecial(reg['NAME'])[0:1]

        if(reg['NAME1'] != "" ):
            Fname += " " + reg ['NAME1']
            name += removeCharSpecial(reg['NAME1'])[0:1]

        if(reg['NAME2'] != "" ):
            Fname += " " + reg ['NAME2']
            name += removeCharSpecial(reg['NAME2'])[0:1]
    
        #if(reg['NAME3'] != "" ):
         #   Fname += " " + reg ['NAME3']
          #  name += removeCharSpecial(reg['NAME3'])[0:1]

        #if(reg['NAME4'] != ""):
         #   Fname += " " + reg ['NAME4']
          #  name += removeCharSpecial(reg['NAME4'])[0:1]
        
        correo = name + apeP + apeM + "@unac.edu.pe"
        
        PASS = passSure()

        salida.writerow([Fname, Lname, correo, PASS,'','/','','','','','','','','','','','','','','','','','',"TRUE" ])

del entrada, salida, reg
csvsalida.close()
del csvsalida

        


    apeP = removeCharSpecial(str(row[0].value)).replace(' ','')
    apeM = removeCharSpecial((str(row[1].value))[0:1])
    name = removeCharSpecial((str(row[2].value))[0:1])

    if(str(row[3].value) != "None" ):
        name += removeCharSpecial((str(row[3].value))[0:1])

    if(str(row[4].value) != "None" ):
        name += removeCharSpecial((str(row[4].value))[0:1])
    
    if(str(row[5].value) != "None" ):
        name += removeCharSpecial((str(row[5].value))[0:1])

    if(str(row[6].value) != "None"):
        name += removeCharSpecial((str(row[6].value))[0:1])
    
    PASS = passSure()
    
    myData = [['First Name [Required]', "Last Name [Required]", "Email Address [Required]","Password [Required]","Password Hash Function [UPLOAD ONLY]","Org Unit Path [Required]","New Primary Email [UPLOAD ONLY]","Home Secondary Email","Work Secondary Email","Work Phone","Home Phone","Mobile Phone","Work Address","Home Address","Employee ID","Employee Type","Employee Title","Manager Email","Department","Cost Center","Building ID","Floor Name","Floor Section","Change Password at Next Sign-In"],
        [str(row[2].value) + str(row[3].value) + str(row[4].value) + str(row[5].value) + str(row[6].value), str(row[0].value), str(row[1].value)]]
    
    salida.writerow(myData['First Name [Required]'])

del salida
myFile.close()
"""