from Juego import Juego
import Credenciales
import mysql.connector
class DAO:
    def __init__(self):
        self.__conectar()

    def __conectar(self):
        self.__conexion = mysql.connector.connect(**Credenciales.get_Credenciales())
        self.__cursor = self.__conexion.cursor() #El cursor ejecuta las querys 

    def __cerrar(self):
        self.__conexion.commit() #El commit aplica cambios
        self.__conexion.close()

    def registrar_juego(self, j:Juego):
        self.__conectar()
        sql = "INSERT INTO juego (Codigo, Nombre,Genero,Precio) VALUES (%s,%s,%s,%s)"
        values = (j.get_codigo(), j.get_nombre(), j.get_genero(), j.get_precio())
        self.__cursor.execute(sql, values) #Esta ejecutando la sentencia sql con los valores que estan ingresados en el parentesis
        self.__cerrar()

    def recuperar_juego(self, codigo:str)->Juego:
        self.__conectar
        sql = "SELECT * FROM juego WHERE codigo = %s"
        values = (codigo,) #si o si debe ir la coma para indicar que es una tupla
        self.__cursor.execute(sql, values)
        respuesta = self.__cursor.fetchone() #fetchone solo recupera 1 
        self.__cerrar()
        j = Juego(respuesta[1],respuesta[2],respuesta[3],respuesta[4],respuesta[0])
        return j
