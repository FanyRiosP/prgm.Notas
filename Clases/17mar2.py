#CLASE PUNTO 

#Atributos privados = encapsulamiento

#Recibe e inicializa los parámetros en la firma del método

import math

class Punto:
    def __init__(self, x = 0, y = 0):
    
        self.__x = x
        self.__y = y
        #Si no recibe parámetros, va a adquirir los valores del encabezado; si sí recibe, los sustituye

    def set_x(self, x:float):
        self.x = x

    def set_y(self, y:float):
        self.y = y

    def get_x(self)->float:
        return self.__x
    
    def get_y(self)->float:
        return self.__y
    
    #Función suma y resta de dos puntos
    
    def suma(self, otro_punto):
        coord_x = self.__x + otro_punto.get_x()
        coord_y = self.__y + otro_punto.get_y()
        punto_suma = Punto(coord_x, coord_y)
        return punto_suma
    
    def resta(self, otro_punto:object)->object:
        coord_x_nuevo = self.get_x() - otro_punto.get_x()
        coord_y_nuevo = self.get_y() - otro_punto.get_y()
        punto_resta = Punto(coord_x_nuevo, coord_y_nuevo)
        return punto_resta

    #Distancia entre dos puntos  d = √(x2-x1)^2 + (y2-y1)^2

    def distancia(self, otro_punto=object)->float:
        resta1 = otro_punto.get_x() - self.get_x()
        resta2 = otro_punto.get_y() - self.get_y()

        potencia1 = math.pow(resta1)
        potencia2 = math.pow(resta2)

        resultado = math.sqrt(potencia1 + potencia2)
        return resultado 
    
    #Firma __str__
    def __str__(self)->str:
        return "(" + str(self.get_x()) + " , " + str(self.get.get_y()) + ")"
    
    #Compara el punto 1 con el punto que me dan de parámetro
    def __eq__(self, otro:object)->bool:
        return self.get_x() == otro.get_x() and self.get_y() == otro.get_y()

    #Desplazar un punto

    def desplazamiento(self, aumento_x:float, aumento_y:float)->object:
        return Punto(self.get_x() +  aumento_x, self.get_y() + aumento_y)


if __name__ == "__main__":
    punto = Punto()
    punto2 = Punto(4, 5)