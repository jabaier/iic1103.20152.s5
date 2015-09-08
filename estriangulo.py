a=float(input("a? "))
b=float(input("b? "))
c=float(input("c? "))

if a>0 and b>0 and c>0 and a+b>c and b+c>a and c+a>b: # es un triangulo
    if a**2+b**2==c**2 or b**2+c**2==a**2 or c**2+a**2==b**2:
        if a==b or a==c or b==c:
            print("Estos numeros son los lados de un triangulo recto e isosceles")
        else:
            print("Estos numeros son los lados de un triangulo recto")
#    elif a==b or a==c or b==c:
    elif a==b and b==c:
        print("Estos numeros son los lados de un triangulo equilatero")
    elif a==b or a==c or b==c:
        print("Estos numeros son los lados de un triangulo isosceles")
    else:
        print("Estos numeros son los lados de un triangulo")
else:
    print("Estos numeros no son los lados de un triangulo")
