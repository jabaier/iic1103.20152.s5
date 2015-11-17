def EnL(x,L):
    if L==[]:
        return False
    if x==L[0]:
        return True
    if type(L[0])==type([]) and EnL(x,L[0]):
        return True
    return EnL(x,L[1:])

print(EnL(2,[1,[2],3]))
print(EnL(2,[1,[[[[[[[2]]]]]]],3]))
print(EnL(8,[1,[2],3]))
