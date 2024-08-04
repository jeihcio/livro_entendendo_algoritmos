def fatorial(x, acumulador=1):
    if x == 1:
        return acumulador
    else:
        return fatorial(x - 1, x * acumulador)
    
print(fatorial(3))