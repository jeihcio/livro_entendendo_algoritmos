def contarNumeroItens(lista):
    if not lista:
        return 0
    else:
        return 1 + contarNumeroItens(lista[1:])

print(contarNumeroItens([1,2,3]))
print(contarNumeroItens([0,1,2,3,4,5,6,7,8,9]))