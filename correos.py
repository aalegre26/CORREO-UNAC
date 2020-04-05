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

with open('DATA-INGRESANTES.csv') as csvarchivo:
    #ARCHVIO CON LA DATA
    entrada = csv.DictReader(csvarchivo)
    #ARCHIVO DE SALIDA PARA GSUITE
    csvsalida = open('uGsuite.csv', 'w', newline='')
    salida = csv.writer(csvsalida)
    #ARCHIVO DE SALIDA PARA SGA
    csvsalida1 = open('uSGA.csv','w',newline='')
    salida1 =csv.writer(csvsalida1)



    salida.writerow(["First Name [Required]","Last Name [Required]","Email Address [Required]","Password [Required]","Password Hash Function [UPLOAD ONLY]","Org Unit Path [Required]","New Primary Email [UPLOAD ONLY]","Home Secondary Email","Work Secondary Email","Work Phone","Home Phone","Mobile Phone","Work Address","Home Address","Employee ID","Employee Type","Employee Title","Manager Email","Department","Cost Center","Building ID","Floor Name","Floor Section","Change Password at Next Sign-In"])

    for reg in entrada:
        Lname = reg['PATERNO'] + " " + reg['MATERNO']
        Fname = reg['PRIMER NOMBRE']

        apeP = removeCharSpecial(reg['PATERNO']).replace(' ','')
        apeM = removeCharSpecial(reg['MATERNO'])[0:1]
        name = removeCharSpecial(reg['PRIMER NOMBRE'])[0:1]

        if(reg['SEGUNDO NOMBRE'] != "" ):
            Fname += " " + reg ['SEGUNDO NOMBRE']
            name += removeCharSpecial(reg['SEGUNDO NOMBRE'])[0:1]

        if(reg['TERCER NOMBRE'] != "" ):
            Fname += " " + reg ['TERCER NOMBRE']
            name += removeCharSpecial(reg['TERCER NOMBRE'])[0:1]
    
        if(reg['CUARTO NOMBRE'] != "" ):
            Fname += " " + reg ['CUARTO NOMBRE']
            name += removeCharSpecial(reg['CUARTO NOMBRE'])[0:1]

        if(reg['QUINTO NOMBRE'] != ""):
            Fname += " " + reg ['QUINTO NOMBRE']
            name += removeCharSpecial(reg['QUINTO NOMBRE'])[0:1]
        
        correo = name + apeP + apeM + "@unac.edu.pe"
        
        PASS = passSure()

        switcher = {
        "1": "/FCA",
        "11": "/FCC",
        "21": "/FCE",
        "31": "/FIEE",
        "32": "/FIEE",
        "41": "/FIPA",
        "42": "/FIPA",
        "51": "/FIIS",
        "52": "/FIIS",
        "61": "/FIQ",
        "71": "/FIME",
        "72": "/FIME",
        "81": "/FCS",
        "82": "/FCS",
        "91": "/FCNM",
        "92": "/FCNM",
        "95": "/FIARN",       
    }                  

        path = switcher.get(reg['COD_FAC'], "/")
        cod_fac = reg['COD_FAC']
        cod_alu = reg['COD_ALU']
        salida.writerow([Fname, Lname, correo, PASS,'',path,'','','','','','','','','','','','','','','','','',"TRUE" ])
        salida1.writerow([Fname, Lname, correo, cod_alu,cod_fac,PASS])

del entrada, salida, salida1, reg
csvsalida.close()
csvsalida1.close()
del csvsalida, csvsalida1
