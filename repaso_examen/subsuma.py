
def subsuma_igual(sol,L,S):
    if L==[]:
        if S==0:
            print(sol)
            return False # esto es True si buscamos UNA solucion
        return False
    if subsuma_igual(sol,L[1:],S):
        return True
    if subsuma_igual(sol+[L[0]],L[1:],S-L[0]):
        return True
    return False

def subsuma_igual2(sol,L,S):
    if L==[]:
        if S==0:
            print(sol)
            return
        return
    subsuma_igual2(sol,L[1:],S)
    subsuma_igual2(sol+[L[0]],L[1:],S-L[0])


def subsuma_menorigual(sol,L,S):
    if L==[]:
        if S>=0:
            print(sol)
            return False # esto es True si buscamos UNA solucion
        return False
    if subsuma_menorigual(sol,L[1:],S):
        return True
    if subsuma_menorigual(sol+[L[0]],L[1:],S-L[0]):
        return True
    return False

def suma_igual(L,S):
    subsuma_igual2([],L,S)

def suma_menorigual(L,S):
    subsuma_menorigual([],L,S)

suma_menorigual([1,2,4,3],5)
