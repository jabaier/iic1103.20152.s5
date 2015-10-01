
# defina una función que dado una lista de numeros
# retorne la suma de ellos

def sumalista(l):
# calcula l[0] + l[1] + l[2] + ... + l[??]
# el largo de la lista l se obtiene con len(l)
    suma = 0
    i = 0
    while i < len(l):
        suma = suma + l[i]
        i = i + 1
    return suma

def sumalista_cool(l):
    suma = 0
    for e in l:
        suma = suma + e
    return suma


def desafio_google(l):
    i = 0
    while i < len(l):
        if sumalista(l[:i])==sumalista(l[i+1:]):
            return i
        i = i + 1
    return -1


def mayusculas():
    i = ord('A')
    limite = ord('Z')
    may=''
    while i <= limite:
        may = may + chr(i)
        i = i + 1
    return may

def minusculas():
    return mayusculas().lower()

def encriptar_rot(mensaje, incremento):
    M = mayusculas()
    m = minusculas()

    respuesta = ''
    for c in mensaje:
        indiceM = M.find(c)
        indicem = m.find(c)

        if indiceM > -1:
            respuesta = respuesta + M[(indiceM+incremento)%26]
        elif indicem > -1:
            respuesta = respuesta + m[(indicem+incremento)%26]
        else:
            respuesta = respuesta + c

    return respuesta

men = "Andate al cerro que mas te guste, querido"
enc = encriptar_rot(men,13)
desenc = encriptar_rot(enc,13)
print(enc)
print(desenc)
