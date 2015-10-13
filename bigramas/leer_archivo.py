
nombre=input("nombre del archivo? ")

f=open(nombre,"r")

palabras=[]
for linea in f:
    palabras.extend(linea.split())

print(palabras)
