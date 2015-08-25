
suma = 0
contador = 0

numero=float(input("numero "+str(contador+1)+": "))
suma = suma + numero

while numero >= 0:
    numero=float(input("numero "+str(contador+2)+": "))
    suma = suma + numero
    contador = contador + 1

promedio=(suma - numero)/contador
print("el promedio es "+str(promedio))
