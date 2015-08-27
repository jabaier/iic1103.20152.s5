cont = 0
respuesta='s'

while respuesta=='s' or respuesta=='S':
    print("hola",cont)
    respuesta = str(input("quieres que te salude nuevamente? (s/n)"))
    cont=cont+1
print("chao")
