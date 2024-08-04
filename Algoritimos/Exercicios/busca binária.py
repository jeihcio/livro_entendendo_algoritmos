import random
import time

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio 
        
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1

    return None

def pesquisa_simples(lista, item):
    for indice, elemento in enumerate(lista):
        if elemento == item:
            return indice
               
    return None

# Gerar uma lista com N números aleatórios ordenados
quantidade_numeros = 10000000
minha_lista = sorted(random.sample(range(1, quantidade_numeros * 10), quantidade_numeros))
itens_para_procurar = [minha_lista[10000], minha_lista[50000], minha_lista[90000], -1, quantidade_numeros * 10 + 1]

for item in itens_para_procurar:
    # Medir o tempo de execução da pesquisa binária
    inicioTempoBuscaBinaria = time.time()
    resultado_binaria = pesquisa_binaria(minha_lista, item)  
    finalTempoBuscaBinaria = time.time()
    tempo_binaria = finalTempoBuscaBinaria - inicioTempoBuscaBinaria

    # Medir o tempo de execução da pesquisa simples
    inicioTempoBuscaSimples = time.time()
    resultado_simples = pesquisa_simples(minha_lista, item)
    fimTempoBuscaSimples = time.time()
    tempo_simples = fimTempoBuscaSimples - inicioTempoBuscaSimples

    # Comparar tempos
    diferenca = abs(tempo_binaria - tempo_simples)
    if tempo_binaria < tempo_simples:
        mais_rapida = "A pesquisa binária foi mais rápida"
    else:
        mais_rapida = "A pesquisa simples foi mais rápida"

    # Imprimir resultados para o item atual
    print(f"Item procurado: {item}")
    print(f"Resultado da pesquisa_binaria: {resultado_binaria}")
    print(f"Tempo de execução da pesquisa_binaria: {tempo_binaria} segundos")
    print(f"Resultado da pesquisa_simples: {resultado_simples}")
    print(f"Tempo de execução da pesquisa_simples: {tempo_simples} segundos")
    print(f"{mais_rapida} por {diferenca} segundos\n")