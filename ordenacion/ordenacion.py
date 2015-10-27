
def minimo(i,L):
    #encuentra el minimo elemento en L desde la posicion i en adelante
    minimo = L[i]
    pos = i
    i = i + 1
    while i < len(L):
        if minimo > L[i]:
            minimo = L[i]
            pos = i
        i = i + 1
    return pos

def OrdenacionInsercion(L):
    i = 1
    while i < len(L):
        j = i
        while j > 0 and L[j-1] > L[j]:
            L[j-1],L[j]=L[j],L[j-1]
            j = j - 1
        i = i + 1

def OrdenacionBurbuja(L):
    j = len(L)-1
    while j > 0:
        i = 0
        intercambio=False
        while i < j:
            if L[i+1]<L[i]:
                L[i],L[i+1]=L[i+1],L[i]
                intercambio=True
            i=i+1
        if not intercambio: break
        j=j-1

def OrdenacionSeleccion(L):
    i = 0
    while i < len(L)-1:
        indice = minimo(i,L)
        L[i],L[indice] = L[indice],L[i]
        i=i+1

# Prueba con una lista pequeña
#L=[7,5,3,1,4,3,5,6]
#OrdenacionSeleccion(L)
#OrdenacionBurbuja(L)
#OrdenacionInsercion(L)
#print(L)

# Ordenamos una lista de numeros
L=[]
f=open("numeros.txt","r")
#f=open("numeros_ordenados.txt","r")
for s in f:
    L.append(int(s))
f.close()
OrdenacionBurbuja(L)
#OrdenacionSeleccion(L)
#OrdenacionInsercion(L)
for e in L:
    print(e)
