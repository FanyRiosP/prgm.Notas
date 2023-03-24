#ESTRUCTURA DE WHILE

'''''
while condición:
    Código que se ejecuta mientras 
    la condición sea verdadera
else:
    Código que se ejecuta cuando la condición
    del while se evalúe como False
'''

if __name__ == "__main__":
    i = 2
    while i <= 5:
        print(i)
        i+=1
    else:
        print("Se ejecuta el bloque else")

print("")

#Programa que convierte un número decimal a un número binario

if __name__ == "__main__":
    decimal = int(input("Ingrese un número: "))
    cociente = decimal
    binario = ""
    while cociente > 0:
        residuo = str(cociente % 2)
        cociente //= 2
        binario = residuo + binario
    
    print("El número en binario es: ", binario)


#Programa que convierte un número binario a un número decimal
#PENDIENTE


print("")

#Ejemplo de break dentro de un ciblo

if __name__ == "__main__":
    var = float(input("Escribe un número: "))
    while var > 0:
        var = var -1
        if var == 5:
            break
        print("Imprimiendo el valor de var: ", var)

print("")

#Ejemplo de continue dentro de un ciclo

if __name__ == "__main__":
    núm = float(input("Escribe un número: "))
    while núm > 0:
        núm = núm -1
        if núm == 5:
            continue
        print("Imprimiendo el valor de var: ", núm)

print("")

#Escribir un programa que pida al usuario un número positivo.
#El programa debe terminar hasta que el usuario escriba la palabra FIN.
#Al finalizar el programa debe mostrar el número más pequeño y el más grande que el usuario haya ingresado.

peque = None
grande = None

while True:
    núm = input("Escribe un número positivo o fin/FIN si deseas terminar el programa: ")
    if (núm.upper().strip() == "FIN"):
        break
    else:
        núm_int = int(núm)
        if (núm_int < 0):
            print("Por favor, solo acepto número positivos...")
        else:
            if (peque == None):
                peque = núm_int
            if (grande == None):
                grande = núm_int
            if (núm_int > grande):
                grande = núm_int
            if (núm_int < peque):
                peque = núm_int

print("El elemento más pequeño es: ", peque)
print("El elemento más grande es: ", grande)
            























