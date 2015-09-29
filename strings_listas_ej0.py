
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

print(sumalista_cool([1,1,1,1]))
print(sumalista_cool([1,5,3,7,11]))
