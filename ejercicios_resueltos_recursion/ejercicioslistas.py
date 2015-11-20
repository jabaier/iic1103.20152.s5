def sumar(lista):
    suma = 0
    for i in lista:
        if isinstance(i,(tuple,list)):
            suma = suma + sumar(i)
        elif isinstance(i,(int,float)):
            suma = suma + i
    return suma

def index(elem,lista):
    for i in range(len(lista)):
        if isinstance(lista[i],(tuple,list)):
            pos = index(elem,lista[i])
            if len(pos)>0:
                pos.insert(0,i)
                return pos
        elif lista[i]==elem:
            return [i]
    return []

def aplanar(lista):
    i=0
    while i<len(lista):
        if isinstance(lista[i],(tuple,list)):
            aplanar(lista[i])
            a = len(lista[i])
            for j in range(a):
                lista.insert(i+1,lista[i].pop())
            lista.pop(i)
            i = i + a
        else:
            i = i + 1
    return lista

print(sumar([0,0.5,[98],'hola',[57,[6,9,8],(9,8)]]))
print(index(4,[[0,1],[[2],[3,[4]]]]))
print(index(2,[[[[[0]]]]]))
print(index(3,[[],90,3,0,[3]]))
print(aplanar([[0,1],0,[[2],[3,[4]]]]))
