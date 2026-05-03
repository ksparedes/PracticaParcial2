import Listas

list = Listas.listaEnlazada()


#Menu para lista enlazada simple     

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
            data = input("Digite el valor a insertar: ")
            list.insert_at_first(data)


        if op=="2":
            data = input("Digite el valor a insertar: ")
            list.insert_at_end(data)

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
