'''''
Consejos para tarea:
1. Usar while
Clase línea en un archivo dif, también clase punto
2. Hacer funciones en otros archivos: import nombreArchivo / form nombreArchivo import función
3. Importar archivo punto de la profesora :)
4. Solo debe de estar la clase
5. Se puede usar .math pero mejor crear nosotros las funciones 
No sé jsjalkdsjf unu 
'''

#Ejemplos de for

'''''
range(star,stop,step)
-Primer paréntesis > intervalo cerrado
-Segundo paréntesis > intervalo abierto 
'''

for i in range(5,13,9):
    print(i)
    #Imprime: 5 

for i in range(13,5,1):
    print(i)
    #Imprime: -

for i in range(19,2,-3):
    print(i)
    #Imprime: 19 16 13 10 7 4 

for i in range(21,9):
    print(i)
    #Imprime: -

#Suma de los primeros impares
'''''
n = int(input("Escribe un número entero: "))
suma = 0 
producto = 1

for i in range(1,2*n,2):
    suma += i
    producto *= i

print(f"La suma den los primeros {n} impares es: ")
print(f"El producto de primeros {n} impares es: ")
#f > para dar formato

suma = 0 
producto = 1

for i in range(1,2*n+1,2):
    suma += i
    producto *= i

print(f"La suma den los primeros {n} impares es: ")
print(f"El producto de primeros {n} impares es: ")
'''

#Factorial 
'''''
def factorial(n):
    fac = 1 
    for i in range(n,1,-1):
        fac *= i
    return 
'''

# Algo sjkdfla

#n = input("Ingresa un número: ")
'''''
n = 10
backwards = ""
for i in range(len(n)-1,0,-1):
    backwards += n [i]

print(backwards)
'''
#Hacer el último ejemplo 
#Imprimir los números entre 1 y 1000 que sean números prefectos (La suma de sus dividendos sea el mismo número, ej: 1+2+3=6)

for i in range(1,1000):
    suma = 0 
    for j in range(1,i):
        if i % j == 0:
            suma += j
    if suma == i:
        print(f"{j} es número perfecto")