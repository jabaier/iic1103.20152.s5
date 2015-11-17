def subsecuencia(L):
    if L==[]:
        return [[]]
    R=subsecuencia(L[1:])
    S=[]
    for r in R:
        S.append([L[0]]+r)
    #S = [[L[0]]+r for r in R]
    return R + S

print(subsecuencia([1000,2000,2000,500,500,100]))
