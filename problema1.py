class estudiante():
    def __init__(self, nombre, carne, edad, telefono, cursos):
        self.nombre = nombre
        self.carne = carne
        self.edad = edad
        self.telefono = telefono
        self.cursos = cursos
        self.siguiente = None

class curso():
    def __init__(self, nombreCurso):
        self.nombre = nombreCurso
        self.siguiente = None
#------------------------------------Listas--------------------------------------------------------------
class listaEn():
    def __init__(self):
        self.inicio = None

    def insertarAlumno(self, nuevoNodo):
        if self.inicio == None:
            self.inicio = nuevoNodo
            print('Alumno registrado')
        else:
            temp = self.inicio
            while temp.siguiente != None:
                temp = temp.siguiente
            temp.siguiente = nuevoNodo
            print('Alumno registrado')
    
    def mostrarAlumno(self):
        if self.inicio == None:
            print('La lista no posee nodos')
        else:
            temp = self.inicio
            print('Nombre: ', temp.nombre, ' carné: ', temp.carne, ' edad: ', temp.edad, ' teléfono: ', temp.telefono)
            print('Cursos: ')
            #llamar al método de impresión de los cursos
            temp.cursos.mostrarCurso()
            while temp.siguiente != None:
                temp = temp.siguiente
                print('Nombre: ', temp.nombre, ' carné: ', temp.carne, ' edad: ', temp.edad, ' teléfono: ', temp.telefono)
                print('Cursos: ')
                #llamar al método de impresión de los cursos
                temp.cursos.mostrarCurso()

class listaEnCursos():
    def __init__(self):
        self.inicio = None

    def insertarCurso(self, nuevoNodo):
        if self.inicio == None:
            self.inicio = nuevoNodo
            print('Curso registrado')
        else:
            temp = self.inicio
            while temp.siguiente != None:
                temp = temp.siguiente
            temp.siguiente = nuevoNodo
            print('Curso registrado')
    
    def mostrarCurso(self):
        if self.inicio == None:
            print('La lista no posee nodos')
        else:
            temp = self.inicio
            print('--> ', temp.nombre)
            while temp.siguiente != None:
                temp = temp.siguiente
                print('--> ', temp.nombre)
    
alumnos1 = listaEn()

cursos1 = listaEnCursos()
cursos1.insertarCurso(curso('123- IPC2'))
cursos1.insertarCurso(curso('456- IPC1'))
cursos1.insertarCurso(curso('678- LFP'))
alumnos1.insertarAlumno(estudiante('Jose', '201115455', '29', '12345', cursos1))

cursos2 = listaEnCursos()
cursos2.insertarCurso(curso('123- Mate1'))
cursos2.insertarCurso(curso('678- Lógica sistemas'))
alumnos1.insertarAlumno(estudiante('Samuel', '2011', '19', '65478', cursos2))

cursos3 = listaEnCursos()
cursos3.insertarCurso(curso('123- Química General'))
alumnos1.insertarAlumno(estudiante('Cristal', '15455', '20', '89076', cursos3))

alumnos1.mostrarAlumno()
