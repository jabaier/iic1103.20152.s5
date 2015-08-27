N=int(input('numero? '))

divisor=2

no_es_primo = False # en este momento yo "creo" que el numero es primo

while divisor<N:
    if N%divisor == 0:
        no_es_primo = True  # me acuerdo de
                            # que "es verdad que no es primo"
    divisor=divisor+1

if no_es_primo:
    print("el numero no es primo")
else:
    print("el numero es primo")
