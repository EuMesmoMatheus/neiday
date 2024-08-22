from collections import deque

# Função para verificar a solubilidade contando o número de inversões
def verifica_soluvel(estado):
    # Converte o estado para uma lista linear, ignorando o zero
    lista = sum(estado, [])
    lista = [num for num in lista if num != 0]
    
    inversoes = 0
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                inversoes += 1

    # Mostra a contagem de inversões
    print(f"Número de inversões: {inversoes}")
    
    # Se o número de inversões for par, o quebra-cabeça é solúvel
    return inversoes % 2 == 0

# Função para encontrar a posição do espaço vazio (0)
def encontrar_vazio(estado):
    for i in range(3):
        for j in range(3):
            if estado[i][j] == 0:
                return i, j

# Função para gerar novos estados após um movimento
def gerar_novo_estado(estado, vazio, movimento):
    x, y = vazio
    novo_estado = [linha[:] for linha in estado]
    
    # Movimentos possíveis: cima, baixo, esquerda, direita
    if movimento == 'cima' and x > 0:
        novo_estado[x][y], novo_estado[x-1][y] = novo_estado[x-1][y], novo_estado[x][y]
    elif movimento == 'baixo' and x < 2:
        novo_estado[x][y], novo_estado[x+1][y] = novo_estado[x+1][y], novo_estado[x][y]
    elif movimento == 'esquerda' and y > 0:
        novo_estado[x][y], novo_estado[x][y-1] = novo_estado[x][y-1], novo_estado[x][y]
    elif movimento == 'direita' and y < 2:
        novo_estado[x][y], novo_estado[x][y+1] = novo_estado[x][y+1], novo_estado[x][y]
    
    return novo_estado

# Função para verificar se o estado atual é o estado final
def estado_objetivo(estado):
    objetivo = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    return estado == objetivo

# Função de busca em largura (BFS)
def bfs(estado_inicial):
    fila = deque([(estado_inicial, [])])
    visitados = set()
    
    while fila:
        estado_atual, caminho = fila.popleft()

        # Verifica se é o estado objetivo
        if estado_objetivo(estado_atual):
            return caminho + [estado_atual]
        
        # Converte o estado atual para uma tupla imutável para poder adicionar ao conjunto
        estado_tuple = tuple(tuple(linha) for linha in estado_atual)
        
        # Verifica se o estado já foi visitado
        if estado_tuple in visitados:
            continue
        
        # Marca o estado como visitado
        visitados.add(estado_tuple)
        
        # Encontra a posição do espaço vazio
        vazio = encontrar_vazio(estado_atual)
        
        # Geração de novos estados possíveis
        for movimento in ['cima', 'baixo', 'esquerda', 'direita']:
            novo_estado = gerar_novo_estado(estado_atual, vazio, movimento)
            if novo_estado != estado_atual:
                fila.append((novo_estado, caminho + [estado_atual]))
    
    return None  # Caso não encontre solução

# Estado inicial
estado_inicial = [
    [4, 2, 7],
    [0, 8, 6],
    [3, 5, 1]
]

# Verifica se o estado inicial é solúvel
if verifica_soluvel(estado_inicial):
    # Executa a busca BFS para encontrar a solução
    caminho_solucao = bfs(estado_inicial)

    if caminho_solucao:
        print("Solução encontrada:")
        for estado in caminho_solucao:
            for linha in estado:
                print(linha)
            print()
    else:
        print("Nenhuma solução encontrada.")
else:
    print("O estado inicial não é solúvel.")
