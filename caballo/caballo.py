class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y


    def __add__(self,v):
        return Vector(self.x+v.x,self.y+v.y)

class Caballo:
    def __init__(self,posicion):
        self.posicion=posicion

    def movidas_legales(self,tablero):
        incrementos = [Vector(-1,-2),Vector(1,-2),Vector(-1,2),Vector(1,2),\
                    Vector(-2,-1),Vector(2,-1),Vector(-2,1),Vector(2,1)]
        mov=[]
        for inc in incrementos:
            pos=self.posicion+inc
            if 0<=pos.x<tablero.tamano and 0<=pos.y<tablero.tamano and \
            tablero.libre(pos):
                mov.append(pos)
        return mov

class Tablero:
    def __init__(self,tamano):
        i = 0
        self.tamano=tamano
        self.matriz = []
        while i < tamano:
            self.matriz.append([0]*tamano)
            i+=1

    def __str__(self):
        s=''
        for x in self.matriz:
            y=[str(z) for z in x]
            s+="\t".join(y)+ "\n"
        return s

    def marcar(self,v,marca):
        self.matriz[v.x][v.y] = marca

    def libre(self,v):
        return self.matriz[v.x][v.y]==0

def resolver(caballo, tablero, i):
    if i==tablero.tamano**2:
        print(tablero)  # acá podríamos escojer guardar esto en una lista de resultados
        return True     # cambiar esto por False para imprimir *todas* las soluciones
    decisiones=caballo.movidas_legales(tablero)
    for d in decisiones:
        tablero.marcar(d,i+1)
        if resolver(Caballo(d),tablero,i+1):
            return True
        tablero.marcar(d,0)
    return False


t=Tablero(5)
inicio=Vector(0,0)
t.marcar(inicio,1)
resolver(Caballo(inicio),t,1)
