#Ejemplos de clases 

#Ax^2+Bxy+Cy^2+Dx+Ey+F=0

class ecuaciónGeneral:
    def __init__(self, A, B, C, D, E, F):
        self.__A = A
        self.__B = B
        self.__C = C
        self.__D = D
        self.__E = E
        self.__F = F

    def get_A(self):
        return self.__A
    
    def cónica(self):
        discriminante = self.__B**2 - 4*self.__A*self.__C
        if discriminante < 0:
            if self.__A == self.__C:
                return "Circunferencia"
            else:
                return "Elipse"
        elif discriminante == 0:
            return "Parábola"
        elif discriminante > 0: 
            return "Hipérbola"
        
    

eq1 = ecuaciónGeneral(5, -9, 6, -9, -9, -19)
eq2 = ecuaciónGeneral(5, 9, -5, 12, -9, -18)
eq3 = ecuaciónGeneral(2, -4, 10, 13, -9, 28)
eq4 = ecuaciónGeneral(2, 1, 2, 13, -9, 28)

print(eq1.get_A())
print(eq1.cónica())
print(eq2.cónica())
print(eq3.cónica())
print(eq4.cónica())



class póliza:
    def __init__(self):
        self.__deducible = 2000
        self.__límite = 1000
        self.__siniestro = 0
        
    def set_siniestro(self, sin:int):
        self.__siniestro = sin

    def pago(self):
        if self.__siniestro < self.__deducible:
            return 0
        elif self.__siniestro > self.__deducible and self.__siniestro:
            #Agregar la última desigualdad en la línea ant. ->
            return self.__siniestro - self.__deducible
        else:
            return self.__límite - self.__deducible
        
miPóliza = póliza()
miPóliza.set_siniestro(5000)
print(miPóliza.pago())



