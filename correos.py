from secrets import choice
import csv

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

with open('DATA.csv') as csvarchivo:
    #ARCHVIO CON LA DATA
    entrada = csv.DictReader(csvarchivo)
    #ARCHIVO DE SALIDA
    csvsalida = open('uemailADM.csv', 'w', newline='')
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
    
        if(reg['NAME3'] != "" ):
            Fname += " " + reg ['NAME3']
            name += removeCharSpecial(reg['NAME3'])[0:1]

        if(reg['NAME4'] != ""):
            Fname += " " + reg ['NAME4']
            name += removeCharSpecial(reg['NAME4'])[0:1]
        
        correo = name + apeP + apeM + "@unac.edu.pe"
        
        PASS = passSure()

        salida.writerow([Fname, Lname, correo, PASS,'','/','','','','','','','','','','','','','','','','','',"TRUE" ])

del entrada, salida, reg
csvsalida.close()
del csvsalida

        

