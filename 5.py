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

# Algoritmo de Busca Gulosa
def busca_gulosa(grafo, heuristica, inicio, objetivo):
    # Fila de prioridade com base na heurística
    fila_prioridade = []
    heapq.heappush(fila_prioridade, (heuristica[inicio], inicio))
    
    # Conjunto de cidades visitadas
    visitados = set()
    
    # Caminho percorrido
    caminho = []
    
    while fila_prioridade:
        # Pega o estado com a menor heurística
        _, cidade_atual = heapq.heappop(fila_prioridade)
        
        # Se já visitado, ignora
        if cidade_atual in visitados:
            continue
        
        # Marca como visitado
        visitados.add(cidade_atual)
        caminho.append(cidade_atual)
        
        # Verifica se o objetivo foi alcançado
        if cidade_atual == objetivo:
            return caminho
        
        # Adiciona as cidades vizinhas à fila de prioridade
        for vizinho, _ in grafo[cidade_atual]:
            if vizinho not in visitados:
                heapq.heappush(fila_prioridade, (heuristica[vizinho], vizinho))
    
    return None  # Nenhum caminho encontrado

# Testando a busca gulosa de Arad para Bucharest
caminho = busca_gulosa(grafo_romenia, heuristica_romenia, 'Arad', 'Bucharest')

if caminho:
    print("Caminho encontrado:", caminho)
else:
    print("Nenhum caminho encontrado.")
