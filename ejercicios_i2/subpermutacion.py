
def permutacion(x,y):
    if len(x)!=len(y):
         return False
    for c in x:
        if x.count(c) != y.count(c):
            return False
    return True

# retorna verdadero si una permutacion de x
# es substring de y
def subpermutacion(x,y):
    i=0
    while i<=len(y)-len(x):
        if permutacion(x,y[i:i+len(x)]):
            return True
        i = i+1
    return False

print(subpermutacion("dite ","Hoy es un excelente dia"))
print(subpermutacion("yo"   ,"Hoy es un excelente dia"))
print(subpermutacion("ten"  ,"Hoy es un excelente dia"))
print(subpermutacion("diia" ,"Hoy es un excelente dia"))
