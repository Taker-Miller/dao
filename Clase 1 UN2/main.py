from Juego import Juego
from DAO import DAO
def registrar():
        print("Vas a registrar un Juego")
        codigo = input("ingresa codigo")
        nombre = input("Ingrese nombre del juego: ")
        genero = input("Ingrese genero del juego: ")
        precio = int(input("Ingrese precio del juego: "))
        j = Juego(nombre, genero, precio, codigo)
        d = DAO()
        d.registrar_juego(j)

       
def recuperar():    
    print("Buscando juego...")
    codigo = input("Ingrese codigo del juego a buscar: ")
    d = DAO()
    j = d.recuperar_juego(codigo)
    if j!=None:
        print(j)
    else:
        print("No se encuentra el juego")

def eliminar():
    pass

def modificar():
    pass

def mostrar_todo():
    pass

def menu():
    print("---Bienvenido---")
    print("1 - Registrar Juego")
    print("2 - Buscar Juego")
    print("3 - Eliminar Juego")
    print("4 - Modificar Juego")
    print("5 - Mostrar Todo")
    print("6 - Salir")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        registrar()
    if opcion == "2":
        recuperar()
    if opcion == "3":
        eliminar()
    if opcion == "4":
        modificar()
    if opcion == "5":
        mostrar_todo()
    if opcion == "6":
        return True
    else:
        print("La opción no es valida, intenta de nuevo.")

while menu()!=True:
    pass
