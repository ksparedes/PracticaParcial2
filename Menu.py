import Listas

list = Listas.listaEnlazada()


def tipoLista():
    print("Elija la lista con la que desea trabajar :")
    print("1. Lista Enlazada Simple")
    print("2. Lista Enlazada Circular")
    print("3. Salir")
    lista = input("opción:  ")

    if lista == "1":
        mostrarMenu1()  
    elif lista == "2":
        print("Lista Circular")
    elif lista == "3":
        print("Saliendo...")
    else:
        print("Opción no válida. Por favor, elija una opción válida.")  

def mostrarMenu1():
    print("1. Insertar al inicio")
    print("2. Insertar al final")
    print("3. Mostrar lista")
    print("4. Buscar elemento")
    print("5. Eliminar primer elemento")
    print("6. Eliminar por valor")
    print("7. Tamaño de la lista")
    print("8. Invertir lista")
    print("9. Ordenar lista")
    print("10. Salir")
    print("------------------------------------")

def mainSimple():
    while True:
        mostrarMenu1()

        op=input("Digite su opción " )

        if op=="1":
            n = input("Digite el valor a insertar: ")
            list.insert_at_first(n)


        if op=="2":
            n = input("Digite el valor a insertar: ")
            list.insert_at_end(n)

        if op=="3":
            list.display()

        if op=="4":
            k= input("Digite el valor a buscar ")
            list.search()

        if op=="5":
            list.delete_first()

        if op=="6":
            k = input("Digite el valor a eliminar: ")
            list.delete_by_value(k)

        if op=="7":
            print("Tamaño de la lista:", list.mostrarTam())

        if op=="8":
            list.reverse()

        if op=="9":
            list.sort()

        if op=="10":
            print("Saliendo...")
            break
