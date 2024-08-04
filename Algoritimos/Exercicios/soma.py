def somar(lista):
    if not lista:
        return 0
    else:
        return lista[0] + somar(lista[1:])

print(somar([2,4,6]))
print(somar([]))
print(somar([0 -1, 2]))
