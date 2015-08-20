N=int(input("cuantos numeros? "))

suma = 0
contador = 0

while contador < N:
    numero=float(input("numero "+str(contador+1)+": "))
    suma = suma + numero
    contador = contador + 1

promedio=suma/N
print("el promedio es "+str(promedio))
