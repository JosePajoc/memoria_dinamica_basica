'''1 crear el objeto nodo
    Por teoría el atributo siguiente apunta a Nulo'''
class nodo():
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

'''2 crar el objeto lista
    Por teoría la lista se crea vacía
    Su apuntador debe ser nulo, este se usa para el inicio de la lista'''
class listaEn():
    def __init__(self):
        self.inicio = None

    '''3 Insertar nodo al inicio si esta vacío, en caso contrario
        se crea un método que recorra los nodos hasta encontrar el que apunte a Nulo
        y se da la instrucción de que su apuntador este enlazado con el nuevo Nodo'''
    
    def insertar(self, nuevoNodo):
        if self.inicio == None:
            self.inicio = nuevoNodo
            print('insertado al inicio')
        else:
            temp = self.inicio
            while temp.siguiente != None:
                temp = temp.siguiente
            temp.siguiente = nuevoNodo
            print('insertado al final')
    
    '''4 Mostrar nodos'''
    def mostrar(self):
        if self.inicio == None:
            print('La lista no posee nodos')
        else:
            temp = self.inicio
            print(temp.valor)
            while temp.siguiente != None:
                temp = temp.siguiente
                print(temp.valor)
    
    '''5 Eliminar nodo'''
    def eliminar(self, valorEliminar):
        if self.inicio == None:
            print('La lista no posee nodos')
        #5.1 verificar que el nodo inicial coincida con el valor a eliminar y reasignar apuntador
        elif self.inicio.valor == valorEliminar:
            self.inicio = self.inicio.siguiente
            print('Nodo eliminado')
        else:
            temp = self.inicio
            anterior = None
            #5.2 Buscar el nodo que coincida con el valor y no se apunte a nulo
            while temp.siguiente != None and temp.valor != valorEliminar:   
                anterior = temp
                temp = temp.siguiente
            #5.3 Ya localizado el nodo se reasignan apuntadores
            if temp.valor == valorEliminar:
                anterior.siguiente = temp.siguiente
                temp.siguiente = None
                print('Nodo eliminado')
            else:
                print('No existe ese valor')
    
    '''6 Buscar nodo'''
    def buscar(self, valorBuscar):
        if self.inicio == None:
            print('La lista no posee nodos')
        #6.1 recorrer y ver que coincida el valor
        else:
            temp = self.inicio
            #6.2 Buscar el nodo que coincida con el valor y no se apunte a nulo
            while temp.siguiente != None and temp.valor != valorBuscar:   
                temp = temp.siguiente
            #6.3 Ya localizado el nodo se muestra
            if temp.valor == valorBuscar:
                print('Nodo encontrado ->', temp.valor)
            else:
                print('No existe ese valor')
        
# 3.1 Se instancia la lista
lista1 = listaEn()
#3.2 Se crean nodos por separado o como parámetro en el método
nodo1 = nodo(10)
nodo2 = nodo(4)
lista1.insertar(nodo1)
lista1.insertar(nodo2)
lista1.insertar(nodo(8))
lista1.insertar(nodo(15))
#4 mostrar nodos
lista1.mostrar()
print('------')
lista1.eliminar(10)
lista1.mostrar()
lista1.buscar(8)