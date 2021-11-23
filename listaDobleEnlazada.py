'''1 crear el objeto nodo
    Por teoría el atributo siguiente y anterior apuntan a Nulo'''
class nodo():
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

'''2 crar el objeto lista doble enlazada
    Por teoría la lista se crea vacía
    Su apuntador debe ser nulo, este se usa para el inicio de la lista'''
class listaDoble():
    def __init__(self):
        self.inicio = None
    
    '''3 Insertar nodo al inicio si esta vacío, en caso contrario
        se crea un método que recorra los nodos hasta encontrar el que apunte su siguiente a Nulo (último nodo)
        y se da la instrucción de que ese nodo nuevo insertado su apuntador anterior este enlazado con el 
        último Nodo encontrado'''
    
    def insertar(self, nodo):
        if self.inicio == None:
            self.inicio = nodo
        else:
            temporal = self.inicio
            while temporal.siguiente != None:
                temporal = temporal.siguiente
            #3.1 Asignación de punteros
            temporal.siguiente = nodo
            nodo.anterior = temporal
        print("Nodo agregado")
    
    '''4 Mostrar nodos'''
    def recorrer(self):
        if self.inicio == None:
            print('La lista esta vacía')
        else:
            temporal = self.inicio
            print('valor: ', temporal.valor)
            while temporal.siguiente != None:
                temporal = temporal.siguiente
                print('valor: ', temporal.valor)
    
    '''5 Eliminar nodo'''
    def eliminar(self, valorEliminar):
        temp = self.inicio
        #Caso 1: el nodo incial es el único que existe
        if self.inicio.valor == valorEliminar and self.inicio.siguiente == None:
            self.inicio = None
            print('Nodo eliminado en el inicio, la lista esta vacía')
        #caso 2: el nodo es el inicio y se posee más nodos la lista
        elif self.inicio.valor == valorEliminar and self.inicio.siguiente != None:
            temp = self.inicio
            temp.siguiente.anterior = None
            self.inicio = temp.siguiente
            print('Nodo eliminado en el inicio')
        #caso 3: el nodo es diferente al inicio y se encuentra en medio
        else:
            #Asignamos el segundo Nodo a temporal y se recorren los nodos
            temp = self.inicio.siguiente
            while temp.siguiente != None and temp.valor != valorEliminar:
                ante = temp
                temp = temp.siguiente
            #3.1 El nodo se encuentra en medio
            if temp.valor == valorEliminar and temp.siguiente != None:
                ante.siguiente = temp.siguiente
                temp.siguiente.anterior = ante
                temp = None
                print('El nodo se elimino, estaba en medio')
            #caso 4: el nodo se encuentra al final
            elif temp.valor == valorEliminar and temp.siguiente == None:
                ante.siguiente = None
                temp = None
                print('El nodo se elimino, estaba al final')
            else:
                print('El valor no existe')


#crear lista enlazada doble
listaD = listaDoble()
#insertar nodos
listaD.insertar(nodo(12))
listaD.insertar(nodo(13))
listaD.insertar(nodo(14))
listaD.insertar(nodo(15))
listaD.insertar(nodo(16))
#mostrar nodos
listaD.recorrer()
#eliminar nodo
listaD.eliminar(12)
listaD.recorrer()
#Prueba usando los apuntadores de los nodos
a = listaD.inicio.siguiente.siguiente.siguiente.anterior.anterior
print('---> ', a.valor)