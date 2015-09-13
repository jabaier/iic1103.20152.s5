
def es_primo(N):
    valor = True # variable que indica si N es primo
    i = 2

    while valor and i <= N-1:
        valor=valor and (N % i != 0)
        i = i + 1
    return valor

total = int(input("cuantos primos muestro? "))
N = 2
cuantos = 0

while cuantos < total:
    M=N+2
    if  es_primo(N) and es_primo(M):
        print(N,M)
        cuantos = cuantos + 1
    N = N + 1
