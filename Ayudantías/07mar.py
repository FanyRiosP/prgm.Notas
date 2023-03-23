#USO DE WHILE


#Imprimir los primos de Mersenne

k = 4
def primo(k):
    i = 2
    while i < k:
        if k%i == 0: 
            return False
        i += 1
    else:
        return True
    
mersenne = 1
n = 2
while mersenne < 10000:
    mersenne = 2**n-1
    if primo(mersenne):
        print(primo)
    n +=1


#Determinar la aproximación del valor de Pi

'''''
termino = √2
termino = √ 2 + termino
termino = √ 2 + √2+√2

'''

import math
n = int(input("Ingresa la aproximación deseada:"))
termino = 0 
producto = 1
i = 0 
while i < n:
    termino = math.sqrt(2 + termino)
    producto *= termino/2
    i +=1

pi = 2/producto
print(pi)


#

n = "12, 14, 27, 54, 43, 98, 13, 19, 67, 88, 21"
num = n. count(",")
sep = n.find(",")
print("sep")

mayor = int(n[:sep])
print(mayor)

while i < num:
    valor = int(n[sep + 1:sep])
    if mayor < valor:
        mayor = valor


