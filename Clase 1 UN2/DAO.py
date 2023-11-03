from Juego import Juego
class DAO:
    def __init__(self):
        pass

    def registrar_juego(self, j:Juego):
        #print("----")
        #print(j) #Esto si tienes el __str
        #print(j.mostrar()) - si tienes una función que retorne un str
        #j.mostrar() - si tienes una función que muestre
        #print("----")
        #Recuperar cada campo para insertarlo en la BD
        pass

    def recuperar_juego(self, codigo:str)->Juego:
        #Ir a la BD y traer el juego en base al codigo
        #Retornar el juego si lo encuentra
        #Retornar None si no lo encuentra
        return None
