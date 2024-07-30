def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0

    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i

    return menor_indice

def ordenacaoSelecao(arr):
    novoArr = []

    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))

    return novoArr

arr = [550, 5, 3, 4, 1, 50, 1000, 2, 10]

print(ordenacaoSelecao(arr))