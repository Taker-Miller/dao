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
        j = buscar()
        if j != None:
        opcion = input("Desea eliminar a este juego(s/n): ")
        if opcion.lower() == "s":
            d = DAO()
            d.eliminar_juego(j.get_id())
        else:
            print("No se ha eliminado el juego")

def modificar():
        j = buscar()
        if j != None:
        codigo = recibir_valor("codigo",j.get_codigo())
        j.set_codigo(codigo)
        nombre = recibir_valor("nombre",a.get_nombre())
        j.set_nombre(nombre)
        precio = recibir_valor("precio",a.get_precio())
        j.set_precio(float(precio))
        genero = (recibir_valor("genero",a.get_genero()))
        j.set_genero(genero)
        d = DAO()
        d.modificar_animal(j)

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
