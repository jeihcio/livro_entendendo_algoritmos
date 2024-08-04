# Minha resolução usando a recursividade com caudas 
def encontrarValorMaisAlto(lista, acumulador=0):
    if not lista:
        return acumulador
    else:
        if lista[0] > acumulador:
            acumulador = lista[0]

        return encontrarValorMaisAlto(lista[1:], acumulador)    
    
# exemplo do livro
def maximo(lista): 
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    
    sub_max = maximo(lista[1:])
    return lista[0] if lista[0] > sub_max else sub_max
    
print(encontrarValorMaisAlto([1,5,2,10,-1,54]))
print(encontrarValorMaisAlto([]))
print(encontrarValorMaisAlto([1]))
print(encontrarValorMaisAlto([100,5,2,10,-1,54]))
print(encontrarValorMaisAlto([100,5,2,999,-1,54]))

print("\n")

print(maximo([1,5,2,10,-1,54]))
# print(maximo([]))
# print(maximo([1]))
print(maximo([100,5,2,10,-1,54]))
print(maximo([100,5,2,999,-1,54]))

