import random

def digitoi(N,i):
    return (N//10**(i-1))%10

def toques(N,Nc,cifras):
    ntoques=0
    i = 1
    while i <= cifras:
        j = 1
        encontrado = False
        while j <= cifras:
            if i != j and digitoi(N,i) == digitoi(Nc,j):
                encontrado = True
            j = j + 1
        if encontrado:
            ntoques = ntoques + 1
        i = i + 1
    return ntoques

def famas(N,Nc,cifras):
    nfamas = 0
    i = 1
    while i <= cifras:
        if digitoi(N,i) == digitoi(Nc,i):
            nfamas = nfamas + 1
        i = i + 1
    return nfamas


cifras = 4

nivel = int(input("Elige tu nivel \n\t1: 8 intentos\n\t2: 6 intentos\n\t3: 4 intentos\n\n\t?"))

if nivel==1:
    intentos=8
elif nivel==2:
    intentos=6
else:
    intentos=4

print("Pensando un número de",cifras,"cifras")

numero_escondido = random.randint(10**(cifras-1),10**cifras-1)

while intentos > 0:
    numero=int(input("cual crees que es el número? "))

    if numero == numero_escondido:
        print("Adivinaste el número!!!")
        break

    print("Tienes ",toques(numero_escondido,numero,cifras),"toques y",famas(numero_escondido,numero,cifras),"famas")
    intentos = intentos - 1
    print("Te quedan solo", intentos,"intentos.")
