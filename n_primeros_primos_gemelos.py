
total = int(input("cuantos primos gemelos muestro? "))
N = 2
cuantos = 0

while cuantos < total:
    valor = True # variable que indica si N es primo
    i = 2

    while valor and i <= N-1:
        valor=valor and (N % i != 0)
        i = i + 1

    M = N + 2
    valor2 = True # variable que indica si N+2 (=M) es primo
    i = 2

    while valor2 and i <= M-1:
        valor2=valor2 and (M % i != 0)
        i = i + 1


    if valor and valor2:
        print(N,M)
        cuantos = cuantos + 1

    N = N + 1
