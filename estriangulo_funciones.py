def estriangulo(a,b,c):
    return a>0 and b>0 and c>0 and a+b>c and b+c>a and c+a>b

def espitagorico(a,b,c):
    return a**2+b**2==c**2 or b**2+c**2==a**2 or c**2+a**2==b**2

def esisosceles(a,b,c):
    return a==b or a==c or b==c

def esequilatero(a,b,c):
    return a==b and b==c

a=float(input("a? "))
b=float(input("b? "))
c=float(input("c? "))

if estriangulo(a,b,c): # es un triangulo
    if espitagorico(a,b,c):
        if esisosceles(a,b,c):
            print("Estos numeros son los lados de un triangulo recto e isosceles")
        else:
            print("Estos numeros son los lados de un triangulo recto")
#    elif a==b or a==c or b==c:
    elif esequilatero(a,b,c):
        print("Estos numeros son los lados de un triangulo equilatero")
    elif esisosceles(a,b,c):
        print("Estos numeros son los lados de un triangulo isosceles")
    else:
        print("Estos numeros son los lados de un triangulo")
else:
    print("Estos numeros no son los lados de un triangulo")
