# Código de exemplo com algumas alterações minhas e inclusão de impressão de dados

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

# Aqui o infinito representa algo que não dá para calcular 
infinito = float("inf")

'''
Esse array de custos é para identificar o quanto custa
até chegar a determinado vértice 

Exemplo: Quanto custa até chegar até a? 
'''
custos = {}
custos["a"] = 6
custos["b"] = 2 
custos["fim"] = infinito

'''
Esse array de pais vai ser usado para encontrar o caminho reverso
e identificar como chegar do fim para o inicio passando
pelo o caminho de menor custo

O pai é o vértice anterior que é usado para chegar no 
vértice atual, por exemplo, o A pode vir do 'início' ou do 'b'
o que vai definir é o menor custo. 

Sabendo o vértice anterior vc consegue encontrar o caminho do fim até o inicio
'''
pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

processados = []

def ache_no_de_custo_mais_baixo(custos):
    custo_mais_baixo = float("inf")
    no_com_custo_mais_baixo = None

    for nodo in custos:
        custo = custos[nodo]

        if custo < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            no_com_custo_mais_baixo = nodo
    return no_com_custo_mais_baixo

nodo = ache_no_de_custo_mais_baixo(custos)
while nodo is not None:
    custo = custos[nodo]
    vizinhos = grafo[nodo]

    for chave in vizinhos.keys():
        novo_custo = custo + vizinhos[chave]
        if custos[chave] > novo_custo:
            custos[chave] = novo_custo
            pais[chave] = nodo

    processados.append(nodo)
    nodo = ache_no_de_custo_mais_baixo(custos)

''' 
É necessário reconstruir de trás para frente pq só temos o
ponteiro que aponta para trás (tabela hash de pais) 
'''

# Reconstruindo o caminho do final até o início
caminho = []
nodo_atual = "fim"
while nodo_atual is not None:  
    caminho.insert(0, nodo_atual)
    nodo_atual = pais.get(nodo_atual, None)

# Imprimindo o caminho e o custo final
print("Caminho mais curto:", " -> ".join(caminho))
print("Custo total:", custos["fim"])
