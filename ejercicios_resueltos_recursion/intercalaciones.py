intercalar(x,y):
    lista = []
    if len(x)==0:
        lista.append(y)
        return lista
    elif len(y)==0:
        lista.append(x)
        return lista
    nuevo = intercalar(x[1:],y)
    for i in nuevo:
        lista.append(x[0]+i)
    nuevo = intercalar(x,y[1:])
    for i in nuevo:
        lista.append(y[0]+i)
    return lista

intercalan(x,y,w):
    if x[0]==w[0]:
        if len(w)==1:
            return True
        elif len(x)==1:
            if y==w[1:]:
                return True
        elif intercalan(x[1:],y,w[1:]):
            return True
    if y[0]==w[0]:
        if len(w)==1:
            return True
        elif len(y)==1:
            if x==w[1:]:
                return True
        elif intercalan(x,y[1:],w[1:]):
            return True
    return False
