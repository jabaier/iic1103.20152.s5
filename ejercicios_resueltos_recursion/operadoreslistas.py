
# funcion (recursiva) que imprime la expresion dado una lista de operadores
# y una lista de numeros

def pretty_print(L,sol):
    if len(L)==1:
        print(L[0],end='')
    else:
        print('(',end='')
        pretty_print(L[:-1],sol[:-1])
        print(sol[-1],end='')
        print(L[-1],end='')
        print(')',end='')

# Dada una lista L y un numero N, determina si
# hay una forma de intercalar operadores entre los numeros
# de tal forma que al computar la expresion resultante,
# asociando por la izquierda, el resultado es N
# El resultado impreso en pantalla son los operadores que van entre los números

def oplista(L,N,Lorig,sol=[],ultimo_op='+',res_parcial=0):
    resultado=operacion(res_parcial,ultimo_op,L[0])
    if len(L)==1:
        if resultado==N:
            pretty_print(Lorig,sol)
            print(' =',N)
            return True
        else:
            return False
    operadores=['+','-','*','/']
    for op in operadores:
        if oplista(L[1:],N,Lorig,sol+[op],op,resultado):
            return True
    return False

def op(L,N):
    if not oplista(L,N,L):
        print("no es posible insertar operadores en",L,"para obtener",N)
        
def operacion(l,op,r):
    if op=='+':
        return l+r
    if op=='-':
        return l-r
    if op=='*':
        return l*r
    if op=='/':
        return l/r
    else:
        return 0


op([1,4,10,1],-30)
op([1,4,10,1],-29)
op([1,4,10,1],49)
op([1,4,10,1],5)
            
