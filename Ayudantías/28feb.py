#Ayudantía 28/02

#Programa para ingresar fecha o algo así xd :3

fecha = input("Ingrese una fecha en el formato dd/mm/aaaa: ").lower()
sep = fecha[-5]
fecha = fecha.split("/")
print(fecha)

if fecha[1] in "enero":
    fecha[1] = 1
elif fecha [1] in "febrero":
    fecha[1] = 2
elif fecha[1] in "marzo":
    fecha[1] = 3
elif fecha[1] in "abril":
    fecha[1] = 4
elif fecha[1] in "mayo":
    fecha[1] = 5
elif fecha[1] in "junio":
    fecha[1] = 6
elif fecha[1] in "julio":
    fecha[1] = 7
elif fecha[1] in "agosto":
    fecha[1] = 8
elif fecha[1] in "septiembre":
    fecha[1] = 9
elif fecha[1] in "octubre":
    fecha[1] = 10 
elif fecha[1] in "noviembre":
    fecha[1] = 11
elif fecha[1] in "diciembre":
    fecha[1] = 12
elif not fecha[1].isdigit():
    fecha[1] = 13

día = int(fecha[0])
mes = int(fecha[1])
año = int(fecha[2])

d = False
m = False
a = False



