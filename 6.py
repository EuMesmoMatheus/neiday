import heapq

# Grafo representando o mapa da Romênia
grafo_romenia = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Oradea', 71), ('Arad', 75)],
    'Oradea': [('Sibiu', 151), ('Zerind', 71)],
    'Sibiu': [('Oradea', 151), ('Arad', 140), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Lugoj', 111), ('Arad', 118)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Pitesti', 97), ('Craiova', 146)],
    'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90)],
    'Giurgiu': [('Bucharest', 90)]
}

# Heurística: Distância em linha reta de cada cidade até Bucharest
heuristica_romenia = {
    'Arad': 366,
    'Zerind': 374,
    'Oradea': 380,
    'Sibiu': 253,
    'Timisoara': 329,
    'Lugoj': 244,
    'Mehadia': 241,
    'Drobeta': 242,
    'Rimnicu Vilcea': 193,
    'Craiova': 160,
    'Fagaras': 176,
    'Pitesti': 100,
    'Bucharest': 0,
    'Giurgiu': 77
}

# Algoritmo A*
def busca_a_star(grafo, heuristica, inicio, objetivo):
    # Fila de prioridade com base na função f(n) = g(n) + h(n)
    fila_prioridade = []
    heapq.heappush(fila_prioridade, (heuristica[inicio], 0, inicio, []))
    
    # Dicionário para armazenar o custo do caminho mais curto encontrado até cada cidade
    custo_total = {inicio: 0}
    
    while fila_prioridade:
        heuristica_atual, custo_atual, cidade_atual, caminho_atual = heapq.heappop(fila_prioridade)
        
        # Verifica se o objetivo foi alcançado
        if cidade_atual == objetivo:
            return caminho_atual + [cidade_atual]
        
        # Adiciona a cidade atual ao caminho
        caminho_atual = caminho_atual + [cidade_atual]
        
        # Explora os vizinhos da cidade atual
        for vizinho, custo in grafo[cidade_atual]:
            novo_custo = custo_atual + custo
            if vizinho not in custo_total or novo_custo < custo_total[vizinho]:
                custo_total[vizinho] = novo_custo
                f_vizinho = novo_custo + heuristica[vizinho]
                heapq.heappush(fila_prioridade, (f_vizinho, novo_custo, vizinho, caminho_atual))
    
    return None  # Nenhum caminho encontrado

# Testando a busca A* de Arad para Bucharest
caminho = busca_a_star(grafo_romenia, heuristica_romenia, 'Arad', 'Bucharest')

if caminho:
    print("Caminho encontrado:", caminho)
else:
    print("Nenhum caminho encontrado.")
