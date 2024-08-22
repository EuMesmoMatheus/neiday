import heapq
import math

# Mapa representado como uma matriz de custos
mapa = [
    [70, 66, 62, 58, 54, 50],
    [66, 56, 52, 48, 44, 40],
    [62, 52, 42, 38, 34, 30],
    [58, 48, 38, 28, 24, 20],
    [54, 44, 34, 24, 14, 10],
    [50, 40, 30, 20, 10, 0]
]

# Custo de movimentação
custo_lateral = 10
custo_diagonal = 14

# Função para calcular a distância Euclidiana
def heuristica(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) * custo_lateral

# Função para verificar se a célula está dentro dos limites do mapa
def dentro_dos_limites(x, y, altura, largura):
    return 0 <= x < altura and 0 <= y < largura

# Algoritmo A*
def busca_a_star(mapa, inicio, destino, obstaculo):
    altura = len(mapa)
    largura = len(mapa[0])
    
    # Inicialização
    fila_prioridade = []
    heapq.heappush(fila_prioridade, (0 + heuristica(*inicio, *destino), 0, inicio, []))
    
    custo_total = {inicio: 0}
    visitados = set()
    
    while fila_prioridade:
        _, custo_atual, (x_atual, y_atual), caminho_atual = heapq.heappop(fila_prioridade)
        
        # Verifica se o objetivo foi alcançado
        if (x_atual, y_atual) == destino:
            return caminho_atual + [(x_atual, y_atual)]
        
        visitados.add((x_atual, y_atual))
        caminho_atual = caminho_atual + [(x_atual, y_atual)]
        
        # Direções possíveis (movimentos laterais e diagonais)
        direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        custo_direcoes = [custo_lateral, custo_lateral, custo_lateral, custo_lateral, custo_diagonal, custo_diagonal, custo_diagonal, custo_diagonal]
        
        for (dx, dy), custo_d in zip(direcoes, custo_direcoes):
            x_novo, y_novo = x_atual + dx, y_atual + dy
            
            if dentro_dos_limites(x_novo, y_novo, altura, largura) and (x_novo, y_novo) != obstaculo:
                novo_custo = custo_atual + custo_d
                
                if (x_novo, y_novo) not in custo_total or novo_custo < custo_total[(x_novo, y_novo)]:
                    custo_total[(x_novo, y_novo)] = novo_custo
                    f_novo = novo_custo + heuristica(x_novo, y_novo, *destino)
                    heapq.heappush(fila_prioridade, (f_novo, novo_custo, (x_novo, y_novo), caminho_atual))
    
    return None  # Nenhum caminho encontrado

# Ponto de partida e destino
inicio = (0, 0)  # Célula com custo 70
destino = (5, 5)  # Célula com custo 0
obstaculo = (3, 3)  # Célula com custo 28

# Executa a busca A*
caminho = busca_a_star(mapa, inicio, destino, obstaculo)

if caminho:
    print("Caminho encontrado:", caminho)
else:
    print("Nenhum caminho encontrado.")
