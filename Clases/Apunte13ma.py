'''''

Métodos: 
Similares a las funciones

    -Constructores: Inicializan el estado del objeto
    dif__init__(self)   // Self - Objeto que se crea a partir de una clase.
    Recibe: Self. Regresa: Nada

    -De acceso: Acceso al valor de una clase
    def get_nombre_atributo(self):  <- Encabezado
        return self.__nombre_atributo


    -Modificadores: Pueden cambiar el valor de un atributo
    def set_nombre(self, nuevo):  // Recibe 2 parámetros: self y el nuevo valor
        self.__nombre = nuevo
        

'''