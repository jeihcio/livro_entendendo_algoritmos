# Estados que precisam ser cobertos
estados_necessarios = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

# Estações de rádio e os estados que elas cobrem (atualizado)
estacoes = {}
estacoes["estacao1"] = set(["id", "nv", "ut"])
estacoes["estacao2"] = set(["wa", "id", "mt"])
estacoes["estacao3"] = set(["or", "nv", "ca"])
estacoes["estacao4"] = set(["nv", "ut"])
estacoes["estacao5"] = set(["ca", "az"])

# Conjunto final das estações escolhidas
estacoes_finais = set()

while estados_necessarios:
    melhor_estacao = None
    estados_cobertos = set()
    
    for estacao, estados in estacoes.items():
        cobertos = estados_necessarios & estados
        if len(cobertos) > len(estados_cobertos):
            melhor_estacao = estacao
            estados_cobertos = cobertos
    
    estados_necessarios -= estados_cobertos
    estacoes_finais.add(melhor_estacao)

print("Estações escolhidas:", estacoes_finais)
