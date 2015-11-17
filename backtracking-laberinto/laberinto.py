import os
import time
class Vector:
	def __init__(self,x,y):
		self.x=x
		self.y=y

	def __add__(self,v):
		return Vector(self.x+v.x,self.y+v.y)

	def __eq__(self,v):
		return self.x==v.x and self.y==v.y

	def __str__(self):
		return "(" + str(self.x) + ","+ str(self.y) + ")"

class laberinto:
	# Constructor, lee laberinto y localiza al agente
	def __init__(self, path):
		self.leer_laberinto(path)
		self.encontrar_agente()
		self.visitados=[]
	# Muestra el tablero
	def mostrar(self):
		for fila in self.lab:
			print(''.join(fila))
	# Lee el laberinto desde el archivo
	def leer_laberinto(self, path):
		archivo = open(path)
		self.lab = []
		for linea in archivo:
			lab_linea = []
			for c in linea.rstrip('\n'):
				lab_linea.append(c)
			self.lab.append(lab_linea)
		archivo.close()
	# Encuentra la posición inicial del agente
	def encontrar_agente(self):
		for i in range(len(self.lab)):
			for j in range(len(self.lab[i])):
				if self.lab[i][j] == '+':
					self.pos = Vector(i,j)
	#Retorna las movidas posibles


    # retorna una lista de vectores con las movidas posibles
	def movidas_posibles(self):
		desp=[Vector(-1,0),Vector(1,0), Vector(0,-1),	Vector(0,1)]
		movs=[]
		for d in desp:
			nueva_pos=self.pos+d
			if self.lab[nueva_pos.x][nueva_pos.y]!='x' and not nueva_pos in self.visitados:
				movs.append(nueva_pos)
		return movs

	def marcar_ruta(self):
		for v in self.visitados:
			os.system('clear')
			if self.lab[v.x][v.y]!='g':
				self.lab[v.x][v.y]='*'
			self.mostrar()
			time.sleep(0.3)

def backtrack(l,i,limite):
	if l.lab[l.pos.x][l.pos.y]=='o':
		l.marcar_ruta()
		return True
	if i==limite:
		return False
	movidas=l.movidas_posibles()
	for m in movidas:
		l.visitados.append(l.pos)
		anterior=l.pos
		l.pos=m
		if backtrack(l,i+1,limite):
			return True
		l.visitados.pop() #estas dos lineas "restituyen P"
		l.pos=anterior
	return False

def resolver(l, i):
		if l.lab[l.pos.x][l.pos.y]=='o':
			l.marcar_ruta()
			return True
		decisiones=l.movidas_posibles()
		for d in decisiones:
			oldpos=l.pos
			l.pos=d
			l.visitados.append(l.pos)
			if resolver(l, i+1):
				return True
			l.visitados.pop()
			l.pos=oldpos
		return False

# Código principal

lab = laberinto('./maze_2.txt')
lab.mostrar()
lim=1
while not backtrack(lab,0,lim):
	lim=lim+1
