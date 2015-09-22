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
    def __init__(self,x,y,lado):
        self.x=x
        self.y=y
        self.lado=lado
        self.color=color(0,0,0)
        self.r="undef"

    def inscribir(self,circ):
        self.lado=(2**.5)*circ.radio
        self.x = circ.x - self.lado/2
        self.y = circ.y - self.lado/2

    def mover(self,x,y):
        self.x = x
        self.y = y

    def pintar(self,color):
        self.color=color

    def cambiarlado(self,L):
        self.lado=L

    def escalar(self,escala):
        self.lado = self.lado*escala

    def mostrar(self):
        print("este cuadrado está en ("+str(self.x)+","+str(self.y)+") y tiene lado "+str(self.lado))

    def desplazar(self,v):
        self.x=self.x+v.x
        self.y=self.y+v.y

    def __str__(self):
        return "[]"+str(vector(self.x,self.y))+":"+str(self.lado)

    def dibujar(self,window):
        if self.r != "undef":
            self.r.undraw()

        self.r=Rectangle(Point(self.x,self.y),Point(self.x+self.lado,self.y+self.lado))
        self.r.setOutline(color_rgb(self.color.red,self.color.green,self.color.blue))
        self.r.setWidth(2)
        self.r.draw(window)

class circulo:
    def __init__(self,x,y,radio):
        self.x=x
        self.y=y
        self.radio=radio
        self.r="undef"
        self.color=color(0,0,0)

    def inscribir(self,cuad):
        self.radio = cuad.lado/2
        self.x = cuad.x + cuad.lado/2
        self.y = cuad.y + cuad.lado/2

    def desplazar(self,vec):
        self.x = self.x + vec.x
        self.y = self.y + vec.y

    def dibujar(self,window):
        if self.r != "undef":
            self.r.undraw()

        self.r=Circle(Point(self.x,self.y),self.radio)
        self.r.setOutline(color_rgb(self.color.red,self.color.green,self.color.blue))
        self.r.setWidth(2)
        self.r.draw(window)




from graphics import *

def parte_grafica():
    c=cuadrado(10,10,100)
    w = GraphWin("Mi pantalla", 500, 500)
    c.dibujar(w)
    w.getMouse() # pause to view result
    c.escalar(2)
    c.dibujar(w)
    w.getMouse() # pause to view result
    c.pintar(color(255,0,0))
    c.dibujar(w)
    w.getMouse() # pause to view result
    w.close()

import time

def animacion():
    c=cuadrado(10,10,100)
    w = GraphWin("Mi pantalla", 500, 500)
    circ=circulo(150,150,100)
    circ.dibujar(w)
    while c.x<200:
        c.dibujar(w)
        circ.inscribir(c)
        circ.dibujar(w)
        c.desplazar(vector(0.1,0.1))
        c.escalar(1.0005)
        time.sleep(0.002)

    while c.x>10:
        c.dibujar(w)
        c.desplazar(vector(-0.1,-0.1))
        c.escalar(1/1.0005)
        time.sleep(0.002)



    w.getMouse() # pause to view result



def animacion2():
    circ=circulo(150,150,200)
    cuad=cuadrado(10,10,300)
    w = GraphWin("Mi pantalla", 500, 500)
    contador = 10
    while contador > 0:
        cuad.desplazar(vector(10,10))
        circ.inscribir(cuad)
        circ.dibujar(w)
        cuad.dibujar(w)
        w.getMouse() # pause to view result
        circ.desplazar(vector(10,10))
        cuad.inscribir(circ)
        circ.dibujar(w)
        cuad.dibujar(w)
        w.getMouse() # pause to view result
        contador = contador - 1
    w.close()


#parte_grafica()
animacion2()

c1=cuadrado(1,2,10)
c1.mostrar()

circ=ciculo(10,10,50)

circ.inscribir(c1)


vector_desplazamiento = vector(-10,0)
c1.desplazar(vector_desplazamiento)
c1.desplazar(vector(7,8))
c1.mostrar()
