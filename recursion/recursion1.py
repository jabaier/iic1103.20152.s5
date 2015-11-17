def insert(c,s):
    return [s[:i]+c+s[i:] for i in range(len(s)+1)]

def perm(s):
    if s=='':
        return ['']
    L=[]
    for p in perm(s[1:]):
        L.extend(insert(s[0],p))
    return L

print(perm('1234567890'))
