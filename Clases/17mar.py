#Clase Punto 

#Constructores sin parámetros, contructores que reciben parámetros 

class Robot:
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
        self.__peso = nuevo_peso if nuevo_peso > 0 else 0
    
    def get_km(self)-> int:
        return self.__km
    
    def set_km(self, nuevo_km:int):
        self.__km = nuevo_km if nuevo_km > 0 else 0
    '''''
    def __str__(self):
        return "Nombre: " + self.get_nombre + "Peso " + str(self.get_peso()) + "Km: " + str(self.get_km())
    '''
    #Recibe como 2do parámetro un objeto de la misma clase
    def __eq__(self, otro_robot: object)->bool:
        return self.get_nombre() == otro_robot.get_nombre() and self.get_peso() == otro_robot.get_peso() and self.get_km() == otro_robot.get_peso()
    

if __name__ == "__main__":
    #Pedimos datos al usuario y los guardamos en el objeto
    #nombre = input("Dame nombre: ")
    #peso = float(input("Dame peso: "))
    #km = int(input("Dame kilometraje: "))

    #print("Nombre: ", Robot.get_nombre())

    robotina = Robot("Hola", 100, 20)
    robox = Robot("Hola", 100, 20)
    print("Son iguales: ", robotina == robox)



