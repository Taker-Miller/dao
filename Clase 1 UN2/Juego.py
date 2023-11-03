class Juego:
    def __init__(self, codigo:str, nombre:str, genero:str, precio:int, id:int=0):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__genero = genero
        self.__precio = precio
        self.__id= id

    def get_codigo(self):
        return self.__codigo
    
    def get_nombre(self):
        return self.__nombre
    
    def get_genero(self):
        return self.__genero
    
    def get_precio(self):
        return self.__precio
    
    def get_id(self):
        return self.__id
    
    def set_codigo(self, codigo:str):
        self.__codigo = codigo
    
    def set_nombre(self, nombre:str):
        self.__nombre = nombre

    def set_genero(self, genero:str):
        self.__genero = genero

    def set_precio(self, precio:int):
        self.__precio = precio

    def set_id(self, id:int):
        self.__id = id
            
    def __str__(self):
        txt = f"ID: {self.__id}"
        txt += f"\nCodigo: {self.__codigo}"
        txt += f"\nNombre: {self.__nombre}"
        txt += f"\nGenero: {self.__genero}"
        txt += f"\nPrecio {self.__precio}"
        return txt
    
    