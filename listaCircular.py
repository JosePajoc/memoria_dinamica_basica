'''1 crear el objeto nodo
    Por teoría el atributo siguiente apunta a Nulo'''
class nodo():
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

'''2 crar el objeto lista circular
    Por teoría la lista se crea vacía
    Su apuntador debe ser nulo, este se usa para el inicio de la lista'''
class listaCir():
    def __init__(self):
        self.inicio = None
    
    '''3 Insertar nodo al inicio si esta vacío y el apuntador es a si mismo, en caso contrario
        se crea un método que recorra los nodos hasta encontrar el que apunte al inicio de la lista, en
        otras palabras se da una vuelta completa hasta encontrar al último nodo insertado
        y se da la instrucción de que su apuntador este enlazado con el nuevo Nodo y este nuevo Nodo apunta
        al inicio para cerrar el circulo'''
    def insertar(self, nuevoNodo):
        if self.inicio == None:
            self.inicio = nuevoNodo
            nuevoNodo.siguiente = self.inicio
        else:
            temporal = self.inicio
            while temporal.siguiente != self.inicio:
                temporal = temporal.siguiente
            temporal.siguiente = nuevoNodo
            nuevoNodo.siguiente = self.inicio
        print("Nodo agregado")
    
    '''4 Mostrar nodos'''
    def recorrer(self):
        if self.inicio == None:
            print("La lista circular esta vacía")
        else:
            #Se muestran los datos del nodo inicial, en caso de existir más entra al ciclo
            temporal = self.inicio
            print("valor: ", temporal.valor)
            while temporal.siguiente != self.inicio:
                temporal = temporal.siguiente
                print("valor: ", temporal.valor)
    
    '''5 Eliminar nodo'''
    def eliminar(self, valorEliminar):
        if self.inicio == None:
            print("La lista esta vacía")
        else:
            temp = self.inicio
            anterior = None
            #si el valor se encuentra en el inicio entonces, se busca al último nodo y se cambian los apuntadores
            if self.inicio.valor == valorEliminar:
                #se cambia al segundo nodo para entrar al ciclo
                temp = temp.siguiente
                while temp.siguiente != self.inicio:
                    temp = temp.siguiente
                #cambio de apuntadores
                temp.siguiente = self.inicio.siguiente
                self.inicio = temp
                print("Nodo eliminado")
            else:
                #caso contrario se ubica al nodo y se reasignan apuntadores para el anterior y el actual nodo
                while temp.valor != valorEliminar and temp.siguiente != self.inicio:
                    anterior = temp
                    temp = temp.siguiente
                if temp.valor == valorEliminar:
                    anterior.siguiente = temp.siguiente
                    temp.siguiente = None
                    print("Nodo eliminado")
                else:
                    print("No existe el valor")
    
    '''5 Buscar nodo'''
    def buscar(self, valorBuscar):
        if self.inicio == None:
            print("La lista esta vacía")
        else:
            temp = self.inicio
            while temp.valor != valorBuscar and temp.siguiente != self.inicio:
                temp = temp.siguiente
            if temp.valor == valorBuscar:
                print("Nodo encontrado -> ", temp.valor)
            else:
                print("No existe la clave")

#Se crea la lista circular
circular1 = listaCir()
#Se insertan nodos
circular1.insertar(nodo(10))
circular1.insertar(nodo(20))
circular1.insertar(nodo(30))
circular1.insertar(nodo(40))
circular1.insertar(nodo(50))
#mostrar datos
circular1.recorrer()
#eliminar valor
circular1.eliminar(30)
circular1.eliminar(10)
circular1.recorrer()
#buscar nodo
circular1.buscar(20)