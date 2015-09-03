
total = int(input("cuantos primos muestro? "))
N = 2
cuantos = 0

while cuantos < total:
    valor = True # variable que indica si N es primo
    i = 2

    while valor and i <= N-1:
        valor=valor and (N % i != 0)
        i = i + 1

    if valor:
        print(N)
        cuantos = cuantos + 1

    N = N + 1
