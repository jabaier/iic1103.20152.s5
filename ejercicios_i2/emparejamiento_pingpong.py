def empingpong(l1,l2):
    #dadas dos listas l1 y l2 tales que len(l1)<=len(l2) retorna el emparejamiento ping-pong de l1 con l2
    emp = []
    l1 = l1+l1[-2:0:-1] # l1 ahora tiene un pedazo adicional de l1 pero invertido
    i = 0
    while i<len(l2):  # emparejamiento entre l2 y l1 'rotando' el indice de l1
        emp.append([l2[i],l1[i%len(l1)]])
        i = i+1
    return emp

def empingpong2(l1,l2):
    #dadas dos listas l1 y l2 tales que len(l1)<=len(l2) retorna el emparejamiento ping-pong de l1 con l2
    emp = []
    while len(l1)<len(l2): # hacemos crecer l1 hasta que su tamaño sea el de l2 o mayor
        l1 = l1+l1[-2::-1] # l1 ahora tiene un pedazo adicional de l1 pero invertido
    i = 0
    while i<len(l2):   # ahora hacemos un emparejamiento "estandar"
        emp.append([l2[i],l1[i]])
        i = i+1
    return emp

def empingpong3(l1,l2):
    #dadas dos listas l1 y l2 tales que len(l1)<=len(l2) retorna el emparejamiento ping-pong de l1 con l2
    i = 0             ## indice i itera sobre l1
    j = 0             ## indice j itera sobre l2
    incremento_j = 1  ## este es el incremento para j
    emp = []
    while i<len(l2):
        emp.append([l2[i],l1[j]])
        if j == len(l1)-1 or (j == 0 and incremento_j < 0):
            incremento_j = -incremento_j   ## incremento cambia de signo si llegamos a un extemo de l1
        i = i + 1
        j = j + incremento_j
    return emp

print(empingpong(['a','b'],[1,2,3,4,5,6,7,8]))
print(empingpong(['a','b','c'],[1,2,3,4,5,6,7,8]))
print(empingpong(['a','b','c','d'],[1,2,3,4,5,6,7,8]))
print("--- version 2 ---")
print(empingpong2(['a','b'],[1,2,3,4,5,6,7,8]))
print(empingpong2(['a','b','c'],[1,2,3,4,5,6,7,8]))
print(empingpong2(['a','b','c','d'],[1,2,3,4,5,6,7,8]))
print("--- version 3 ---")
print(empingpong3(['a','b'],[1,2,3,4,5,6,7,8]))
print(empingpong3(['a','b','c'],[1,2,3,4,5,6,7,8]))
print(empingpong3(['a','b','c','d'],[1,2,3,4,5,6,7,8]))
