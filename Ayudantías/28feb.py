#Ayudantía 28/02

#Programa para ingresar fecha o algo así xd :3

fecha = input("Ingrese una fecha en el formato dd/mm/aaaa: ").lower()

'''''
Se podrá ingresar la fecha en diferentes formatos:
fecha = "28/02/2023"
fecha = "28-febrero-2023"
fecha = "28 feb 23"
fecha = "28/feb/2023"
fecha = "1/mar/23"
'''

if fecha[:2].isdigit():
    día = fecha[:2]    #Crea subcad de los primeros dos dígitos dd/
    fecha = fecha[2:]  #Crea subcad de los ultimos dos dígitos
else:
    día = fecha[:1]
    fecha = fecha[1:]

#Separación
sep = fecha[0]  

#Variables para encontrar mes y año
mes = fecha[1:fecha.find(sep,1)]
año = fecha[fecha.find(sep,1)+1]

#Si el mes está escrito por su nombre o abreviatura lo cambiamos a su dígito
if mes in "enero":
    mes = 1
elif mes in "febrero":
    mes = 2
elif mes in "marzo":
    mes = 3
elif mes in "abril":
    mes = 4
elif mes in "mayo":
    mes = 5
elif mes in "junio":
    mes = 6
elif mes in "julio":
    mes = 7
elif mes in "agosto":
    mes = 8
elif mes in "septiembre":
    mes = 9
elif mes in "octubre":
    mes = 10 
elif mes in "noviembre":
    mes = 11
elif mes in "diciembre":
    mes = 12
#Si nungún mes coincide con su nombre o abreviatura y no es ya un dígito, lo cambiamos por un dígito que nos invalide la fecha
elif not mes.isdigit():
    mes = 13

#Casteamos nuestras variables a datos enteros con int()
día = int(día)
mes = int(mes)
año = int(año)

#Variables auxiliares para validar
d = False
m = False
a = False

#Validamos que el día dado esté en su intervalo según el mes correspondiente

if mes == 4 or mes == 6 or mes == 9 or mes == 11:
    #Meses de 30 días
    if día > 0 and día <= 30:
        d = True

#La cantidad de días de febrero depende del años
if mes == 2:
    #Años bisiestos
    if año%4 == 0:
        if día > 0 and día <= 29:
            d = True
    #Demás años
    else:
        if día > 0 and día <= 28:
            d = True
#Para los meses de 31
else:
    if día > 0 and día <= 31:
        d = True

#Validamos que el mes esté en el intervalo [1,12]
if mes > 0 and mes <= 12:
    m = True

#Validamos el años
if año > 0:
    a = True

#Si el día, mes y año son correctos, la fecha es correcta
if d and m and a:
    print("Fecha válida")
#Si alguno es falso, la fecha es incorrecta
else:
    print("Fecha inválida")
