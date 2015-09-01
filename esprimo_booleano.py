N=int(input("numero? "))

if N % 2 == 0:
    valor = False
else:
    valor = True

i=3

while valor and i <= N-1:
    valor=valor and (N % i != 0)
    i = i + 2
print(valor)
