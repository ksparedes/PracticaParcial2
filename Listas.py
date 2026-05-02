class Node:
    def _init_(self,data):
        self.data=data
        self.next=None

#Lista enlazada simple
class listaEnlazada:
    def _init_(self):
        self.head=None

    #Insertar al inicio
    def insert_at_first(self, data):
        new_node=Node(data)
        new_node.next=self.head
        new_node=self.head

    #Insertar al final
    def insert_at_end(self, data):
        new_node=Node(data)

        if self.head is None:
            self.head=new_node
            return

        current=self.head
        while current.next is not None:
            current=current.next

        current.next = new_node

    #Mostrar lista
    def mostrarLista(self):
        if self.head is None:
            return
        
        current=self.head
        while current:
            print(current.data)
            current=current.next 
        
    #Mostrar lista display ->
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    #Buscar elemento
    def search(self,k):
        if self.head is None:
            return
        
        current=self.head
        while current is not None:
            if current.data == k:
                return True
            current = current.next
        
        return False 
    
    #Eliminar primer elemento
    def delete_first(self):
        if self.head:
            self.head = self.head.next

    #Eliminar por valor
    def delete_value(self,k):
        if self.head is None:
            print("Lista vacia")
            return
        
        current=self.head

        if current.data == k:
            self.head=self.head.next
            return

        while current.next is not None:
            if current.next.data == k:
                current.next=current.next.next
                return
            current=current.next
        print("Valor no encontrado")
    
    #Tamaño de la lista
    def mostrarTam(self):
        if self.head is None:
            return "Lista vacia"
        
        current=self.head
        c=0
        while current:
            c+=1
            current=current.next
        return c

    #Invertir lista
    def reverse(self):
        prev=None
        current=self.head

        while current:
            sgte = current.next
            current.next=prev
            prev=current

    def sort(self):
        if self.head is None:
            return
        
        #Algoritmo de ordenamiento burbuja
        intercambio=True
    
    
        while intercambio:
            intercambio=False
            current = self.head
            while current.next:
                #Comparar el valor actual con el siguiente nodo
                if current.data > current.next.data:

                    #Intercambiar los valores de los nodos
                    current.data , current.next.data = current.next.data , current.data                  
                   
                    #Marcar que se realizó un intercambio
                    intercambio=True

                #pasamos al siguiente nodo
                current = current.next
          

    




