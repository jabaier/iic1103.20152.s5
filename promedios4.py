
suma = 0
contador = 0

numero = float(input("numero "+str(contador+1)+": "))

while numero >= 0:
    suma = suma + numero
    numero=float(input("numero "+str(contador+2)+": "))
    contador = contador + 1

if contador > 0:
    promedio=suma/contador
    print("el promedio es "+str(promedio))
else:
    print("ingrese un numero al menos!")
