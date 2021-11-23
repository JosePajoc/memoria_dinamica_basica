'''1 crear el objeto nodo'''
class nodo():
    def __init__(self, valor):
        self.valor = valor

'''2 se crea una lista vacia desde el constructor'''
class pila:
    def __init__(self):
        self.pila = []
    
    '''3 Se agrega al final de la lista el nuevo nodo'''
    def apilar(self, nodoNuevo):
        self.pila.append(nodoNuevo)
        print('Nodo insertado')

    '''4 recorrer pila'''
    def recorrer(self):
        for nodo in self.pila:
            print(nodo.valor)
    
    '''5 eliminar nodo'''
    def eliminar(self):
        if len(self.pila) > 0:
            self.pila.pop()
            '''En el caso de ser una cola lo único que cambia es el nodo a eliminar, 
            se debe quitar al primero que ingreso a la cola
            ej: self.cola.pop(0)'''
            print('Nodo eliminado')
        else:
            print('no hay nodos')

#crear pila
pila1 = pila()
#insertar nodo a la pila
pila1.apilar(nodo(10))
pila1.apilar(nodo(15))
pila1.apilar(nodo(20))
pila1.apilar(nodo(25))
pila1.apilar(nodo(30))
#recorrer pila
pila1.recorrer()
pila1.eliminar()
pila1.recorrer()
        