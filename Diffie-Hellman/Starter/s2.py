def findPrimGen(p):
    for g in range(p):
        i = g*g % p
        k=2
        while i != g:
            i *= g
            i %= p
            k+=1
        if k == p:
            return g


