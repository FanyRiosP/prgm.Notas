#CREACIÓN DE OBJETOS 

'''''
Clase: Robot 
Atritutos: 
    nombre: str
    peso: float
    km: int
Métodos: 
    ...
'''

#Método constructor: 
# El programador decide los valores de inicio
# No recibe parámetros
# Atributos con self - atributos públicos, que tienen acceso fuera de la clase

class Robot:
    def __init__(self):
        self.nombre = "Robonosuke"
        self.peso = 200.0
        self.km = 1

if __name__ == '__main__':
    bunny = Robot()
    #Llamar objetos : nombre_objeto.nombre_atributo
    print(bunny.nombre)
    print(bunny.peso)
    print(bunny.km)

    robotina = Robot()
    robotina.nombre = "Lola"
    robotina.km = 2
    robotina.peso = 50
    print(robotina.nombre)

#Atributos privados - solo son accesibles dentro de la clase 
#self.__nombre_atributo

class Robott:
    def __init__(self):
        self.__nombre = "Atlas"
        self.__peso = 300
        self.__km = 100

    def get_nombre(self)-> str:
        return self.__nombre
    
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def get_peso(self)-> float:
        return self.__peso
    
    def set_peso(self, nuevo_peso:float):
        self.__peso = nuevo_peso
    
    def get_km(self)-> int:
        return self.__km
    
    def set_km(self, nuevo_km:int):
        self.__km = nuevo_km

#Para acceder a atributos privados se crea un método de acceso y algo más que no me acuerdo   
if __name__ == "__main__":
    robocop = Robott()

    print("Nombre: ", robocop.get_nombre())
    robocop.set_nombre("VP 5")
    print("Nombre: ", robocop.get_nombre())
    robocop.set_peso(1000)
    print("Peso: ", robocop.get_peso())
    robocop.set_km(10000)
    print("Km: ", robocop.get_km())

#Crear objetos que reciban parámetros

class Robottt:
    def __init__(self, nombre:str, peso:float, km:int):
        self.__nombre = nombre
        self.__peso = peso
        self.__km = km 
    
    def get_nombre(self)-> str:
        return self.__nombre
    
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        

    def get_peso(self)-> float:
        return self.__peso
    
    def set_peso(self, nuevo_peso:float):
        #self.__peso = nuevo_peso
        self.__peso = nuevo_peso if nuevo_peso > 0 else 0
    
    def get_km(self)-> int:
        return self.__km
    
    def set_km(self, nuevo_km:int):
        #self.__km = nuevo_km
        self.__km = nuevo_km if nuevo_km > 0 else 0

if __name__ == "__main__":
    wall_e = Robottt("wall_e", 40.0, 80)

    print("Nombre: ", wall_e.get_nombre())
    wall_e.set_nombre("hoLA")
    print("Nombre: ", wall_e.get_nombre())








