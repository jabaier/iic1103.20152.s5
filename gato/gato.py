
def ficha2str(valor):
    if valor==0:
        return ' '
    elif valor==1:
        return 'X'
    else:
        return 'O'

class Jugada:
    def __init__(self,x,y,ficha):
        self.x = x
        self.y = y
        self.ficha = ficha

    def __str__(self):
        return ficha2str(self.ficha)+" juega en (" + str(self.x) + "," + str(self.y) + ")"

class JugadorHumano:
    def __init__(self,ficha):
        self.ficha=ficha

    def jugar(self,tablero):
        ## retorna una jugada
        while True:
            linea=input("Jugador" + ficha2str(self.ficha) + ", ingresa tu jugada [x] [y] (ejemplo 1 2): ")
            coords=linea.split()
            if len(coords)==2 and coords[0].isnumeric() and coords[1].isnumeric():
                intcoords = [int(c) for c in coords]
                if 0 <= intcoords[0] <= 2 and 0 <= intcoords[1] <= 2:
                    jugada=Jugada(intcoords[0],intcoords[1],self.ficha)
                    if tablero.posible(jugada):
                        return jugada
            print("Ingresa una jugada válida!")

    def __str__(self):
        return "Jugador humano con "+ficha2str(self.ficha)

import random

class JugadorAleatorio:

    def __init__(self,ficha):
        self.ficha=ficha

    def jugar(self,tablero):
        legales=tablero.legales(self.ficha)
        return random.choice(legales)

    def __str__(self):
        return "Jugador aleatorio con " + ficha2str(self.ficha)


class JugadorPerfecto:
    def __init__(self,ficha):
        self.ficha=ficha
        self.ficha_opuesta=-ficha

    def jugar(self,tablero):
        valor,jugada = self.mejor_jugada(tablero,self.ficha)
        return jugada

    def valor_tablero(self,tablero,ficha):
        quien_gana = tablero.ganador()
        if quien_gana != 0:
            return quien_gana*self.ficha
        valor,jugada = self.mejor_jugada(tablero,ficha)
        return valor

    def mejor_jugada(self,tablero,ficha):
        jugadas_legales=tablero.legales(ficha)
        if len(jugadas_legales)==0:
            return 0,Jugada(-1,-1,0)
        elif len(jugadas_legales)==9: # tablero está vacio
            return 0,Jugada(1,1,self.ficha)
        valores=[self.valor_tablero(tablero.jugar(j),-ficha) for j in jugadas_legales]
        if ficha==self.ficha:
            indice=valores.index(max(valores))
        else:
            indice=valores.index(min(valores))
        return valores[indice],jugadas_legales[indice]

    def __str__(self):
        return "Jugador perfecto con "+ficha2str(self.ficha)

class Tablero:
    def __init__(self,tablero=[[0,0,0],[0,0,0],[0,0,0]]):
        self.tablero = tablero

    def posible(self,jugada):
    ## retorna verdadero si es posible aplicar la jugada en este tablero
        return self.tablero[jugada.x][jugada.y] == 0

    def jugar(self,jugada):
    ## retorna el tablero que resulta de aplicar la jugada en el tablero
        newtab=[list(self.tablero[0]),list(self.tablero[1]),list(self.tablero[2])] # newtab contiene una copia del tablero antiguo
        newtab[jugada.x][jugada.y]=jugada.ficha
        return Tablero(newtab)

    def legales(self,ficha):
    ## retorna una lista ca
        lista_legales=[]
        i=0
        while i<3:
            j=0
            while j<3:
                if self.tablero[i][j]==0:
                    lista_legales.append(Jugada(i,j,ficha))
                j = j + 1
            i = i+1
        return lista_legales


    def ganador(self):
    ## retorna la ficha del ganador del tablero, de haber un ganador, o 0 de no haber ganador
        # revisamos las filas
        i = 0
        while i < 3:
            if self.tablero[i][0]==self.tablero[i][1]==self.tablero[i][2]!=0:
                return self.tablero[i][0]
            i = i + 1

        # revisamos las columnas
        i = 0
        while i < 3:
            if self.tablero[0][i]==self.tablero[1][i]==self.tablero[2][i]!=0:
                return self.tablero[0][i]
            i = i + 1
        # revisamos las diagonales

        if self.tablero[0][0]==self.tablero[1][1]==self.tablero[2][2]!=0 or \
            self.tablero[2][0]==self.tablero[1][1]==self.tablero[0][2]!=0:

            return self.tablero[1][1]

        return 0

    def __str__(self):
        tab_str = ''
        tab_str = tab_str + "|".join([ficha2str(x) for x in self.tablero[0]]) + '\n'
        tab_str = tab_str + "-"*5 + '\n'
        tab_str = tab_str + "|".join([ficha2str(x) for x in self.tablero[1]]) + '\n'
        tab_str = tab_str + "-"*5 + '\n'
        tab_str = tab_str + "|".join([ficha2str(x) for x in self.tablero[2]]) + '\n'

        return tab_str

jugador1=JugadorPerfecto(1)
jugador2=JugadorPerfecto(-1)

tablero=Tablero()

print(tablero)

while True:
    jugada=jugador1.jugar(tablero)
    print(jugada)
    tablero=tablero.jugar(jugada)
    print(tablero)
    if tablero.ganador()!=0:
        print("Ha ganado",jugador1)
        break
    if tablero.legales(jugador2.ficha)==[]:
        print("Empate!")
        break
    jugada=jugador2.jugar(tablero)
    print(jugada)
    tablero=tablero.jugar(jugada)
    print(tablero)
    if tablero.ganador()!=0:
        print("Ha ganado",jugador2)
        break
