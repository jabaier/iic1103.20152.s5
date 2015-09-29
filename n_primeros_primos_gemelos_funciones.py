def isprime(N):
    valor = True # variable que indica si N es primo
    i = 2
    while valor and i <= N-1:
        valor=valor and (N % i != 0)
        i = i + 1
    if valor:
        return True
    else:
        return False

total = int(input("cuantos primos gemelos muestro? "))
x = 2
cuantos = 0

while cuantos < total:
    if isprime(x) and isprime(x+2):
        print(x,x+2)
        cuantos=cuantos+1
    x=x+1
