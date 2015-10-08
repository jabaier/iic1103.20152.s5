from graphics import *
from getchar import *

class color:
    def __init__(self,red,green,blue):
        self.red=red
        self.green=green
        self.blue=blue

class vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,v):
        return vector(self.x+v.x,self.y+v.y)

    def __sub__(self,v):
        return vector(self.x-v.x,self.y-v.y)

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"

class cuadrado:
    def __init__(self,x,y,lado,c=color(0,0,0)):
        self.x=x
        self.y=y
        self.lado=lado
        self.color=c
        self.r="undef"

    def pintar(self,color):
        self.color=color

    def escalar(self,escala):
        self.lado = self.lado*escala

    def __str__(self):
        return "Cuadrado en ("+str(self.x)+","+str(self.y)+") con lado "+str(self.lado)

    def desplazar(self,v):
        self.x=self.x+v.x
        self.y=self.y+v.y

    def inscribir(self,circ):
        self.lado = circ.radio*(2**.5)
        self.x = circ.x - self.lado/2
        self.y = circ.y - self.lado/2

    def dibujar(self,window):
        if self.r != "undef":
            self.r.undraw()

        self.r=Rectangle(Point(self.x,self.y),Point(self.x+self.lado,self.y+self.lado))
        self.r.setOutline(color_rgb(self.color.red,self.color.green,self.color.blue))
        self.r.draw(window)

    def codificar(self):
        # retorna un string que corresponde a la codificacion del circulo
        return " ".join(['cuadrado',str(self.x),str(self.y),str(self.lado)])

class circulo:
    def __init__(self,x,y,radio):
        self.x=x
        self.y=y
        self.radio=radio
        self.color=color(0,0,0)
        self.r = "undef"

    def escalar(self,escala):
        self.radio = self.radio*escala

    def desplazar(self,vec):
        self.x = self.x + vec.x
        self.y = self.y + vec.y

    def inscribir(self,cuad):
        self.radio = cuad.lado/2
        self.x = cuad.x + self.radio
        self.y = cuad.y + self.radio

    def __str__(self):
        return "Circulo en ("+str(self.x)+","+str(self.y)+") con radio "+str(self.radio)

    def dibujar(self,window):
        if self.r != "undef":
            self.r.undraw()
        self.r=Circle(Point(self.x,self.y),self.radio)
        self.r.setOutline(color_rgb(self.color.red,self.color.green,self.color.blue))
        self.r.setWidth(2)
        self.r.draw(window)

    def codificar(self):
        # retorna un string que corresponde a la codificacion del circulo
        return " ".join(['circulo',str(self.x),str(self.y),str(self.radio)])

class lienzo:
    def __init__(self,tamano_x,tamano_y):
        self.objetos=[]
        self.ventana = GraphWin("Una ventana",tamano_x,tamano_y)

    def dibujar(self):
        for obj in self.objetos:
            obj.dibujar(self.ventana)

    def agregar(self,nuevo_objeto):  ## agrega un objeto al lienzo
        self.objetos.append(nuevo_objeto)

    def listar(self):
        i = 0
        while i < len(self.objetos):
            print(str(i)+": ",self.objetos[i])
            i += 1

    def seleccionar_objeto(self):
        self.listar()
        indice=-1
        while not indice in range(len(self.objetos)):
            indice = int(input("Indice del objeto a modificar: "))
        return self.objetos[indice]

    def guardar(self, filename):
        #filename es el nombre del archivo a Guardar
        f = open(filename,'w')
        for obj in self.objetos:
            f.write(obj.codificar()+"\n")
        f.close()

    def leer(self, filename):
        f = open(filename,'r')
        for linea in f:
            l = linea.split()
            if l[0] == "cuadrado":
                objeto = cuadrado(int(l[1]),int(l[2]),float(l[3]))
            elif l[0] == "circulo":
                objeto = circulo(int(l[1]),int(l[2]),float(l[3]))
            self.agregar(objeto)
        f.close()

    def modificar_objeto(self,objeto):
        getch=Getch()
        D=10
        up = vector(0,-D)
        down = vector(0,D)
        left = vector(-D,0)
        right = vector(D,0)
        print("'a': agrandar, 'z': achicar, flechas para mover y 'f' para salir")
        c=''
        while c!='f':
            c=getch()
            if c == 'a':
                objeto.escalar(1.05)
            elif c == 'z':
                objeto.escalar(1/1.05)
            elif ord(c) == 27:
                c1=getch()
                c=getch()
                if ord(c1)==91:
                    desplazamiento=vector(0,0)
                    if ord(c) == 68:
                        desplazamiento=left
                    elif ord(c) == 67:
                        desplazamiento=right
                    elif ord(c) == 65:
                        desplazamiento=up
                    elif ord(c) == 66:
                        desplazamiento=down
                    objeto.desplazar(desplazamiento)
            self.dibujar()


def pregunta_opcion():
    ## muestra el menu en pantalla y retorna la opcion ingresada
    opciones_legales = [str(x+1) for x in range(6)]
    while True:
        print("Cuadrados y Círculos")
        print("\t1. Crear un Círculo")
        print("\t2. Crear un Cuadrado")
        print("\t3. Modificar Objeto")
        print("\t4. Guardar a un Archivo")
        print("\t5. Leer desde un Archivo")
        print("\t6. Salir")
        opt = input("Opcion? ")
        if opt in opciones_legales:
            return opt


def pregunta_circulo():
    ## pregunta por un circulo, lo crea y lo retorna
    while True:
        linea=input("Ingresa [radio] [pos_x] [pos_y]: ")
        l = linea.split()
        if len(l) == 3 and l[0].isnumeric() and l[1].isnumeric() and l[2].isnumeric():
            break
        print("Ingresa un input válido de tres numeros!")

    c = circulo(int(l[1]),int(l[2]),int(l[0]))
    return c

def pregunta_cuadrado():
    ## pregunta por un cuadrado y lo crea
    while True:
        linea=input("Ingresa [lado] [pos_x] [pos_y]: ")
        l = linea.split()
        if len(l) == 3 and l[0].isnumeric() and l[1].isnumeric() and l[2].isnumeric():
            break
        print("Ingresa un input válido de tres numeros!")

    cuad = cuadrado(int(l[1]),int(l[2]),int(l[0]))
    return cuad

def get_nombre_archivo():
    return input("Nombre del archivo: ")


canvas=lienzo(500,500)

opcion='-1' ## valor arbitrario para entrar al while

while opcion != '6':
    opcion = pregunta_opcion()
    if opcion == '1':
        circ = pregunta_circulo()
        canvas.agregar(circ)
        canvas.dibujar()
    elif opcion == '2':
        cuad = pregunta_cuadrado()
        canvas.agregar(cuad)
        canvas.dibujar()
    elif opcion == '3':
        objeto=canvas.seleccionar_objeto()
        canvas.modificar_objeto(objeto)
    elif opcion == '4':
        print("Guardar")
        fname = get_nombre_archivo()
        canvas.guardar(fname)
    elif opcion == '5':
        print("Leer")
        fname = get_nombre_archivo()
        canvas.leer(fname)
        canvas.dibujar()

print("Nos vemos!")
