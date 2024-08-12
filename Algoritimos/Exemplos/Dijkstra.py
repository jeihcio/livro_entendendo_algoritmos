grafo = {}
grafo["inicio"] = {}
grafo["inicio"]["a"] = 6
grafo["inicio"]["b"] = 2

grafo["a"] = {}
grafo["a"]["fim"] = 1

grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5

grafo["fim"] = {}

infinito = float("inf")

custos = {}
custos["a"] = 6
custos["b"] = 2 
custos["fim"] = infinito

pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

processados = []

def ache_no_custo_mais_baixo(custos):
    custo_mais_baixo = float("inf")
    nodo_custo_mais_baixo = None

    for nodo in custos:
        custo = custos[nodo]

        if custo < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo

nodo = ache_no_custo_mais_baixo(custos)
while nodo is not None:
    custo = custos[nodo]
    vizinhos = grafo[nodo]

    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:
            custos[n] = novo_custo
            pais[n] = nodo

    processados.append(nodo)
    nodo = ache_no_custo_mais_baixo(custos)

# Reconstruindo o caminho do final até o início
caminho = []
nodo_atual = "fim"
while nodo_atual != "inicio":  # Alterei para parar quando atingir "inicio"
    caminho.insert(0, nodo_atual)
    nodo_atual = pais[nodo_atual]

# Adiciona o início ao caminho
caminho.insert(0, "inicio")

# Imprimindo o caminho e o custo final
print("Caminho mais curto:", " -> ".join(caminho))
print("Custo total:", custos["fim"])
