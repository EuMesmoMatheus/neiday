class AspiradorTresSalas:
    def __init__(self):
        self.visitados = set()

    # Função de transição de estados
    def oper(self, acao, estado):
        X, Y, Z, W = estado

        # Ações de aspiração
        if acao == 'aspirar':
            if X == 'sala1' and Y == 1:
                return ('sala1', 0, Z, W)
            elif X == 'sala2' and Z == 1:
                return ('sala2', Y, 0, W)
            elif X == 'sala3' and W == 1:
                return ('sala3', Y, Z, 0)

        # Ações de movimentação entre salas
        elif acao == 'entrarSala1' and X in ['sala2', 'sala3']:
            return ('sala1', Y, Z, W)
        elif acao == 'entrarSala2' and X in ['sala1', 'sala3']:
            return ('sala2', Y, Z, W)
        elif acao == 'entrarSala3' and X in ['sala1', 'sala2']:
            return ('sala3', Y, Z, W)

        # Nenhuma ação válida, retorna o mesmo estado
        return estado

    # Verifica se o estado é o objetivo (todas as salas limpas)
    def estado_objetivo(self, estado):
        _, Y, Z, W = estado
        return Y == 0 and Z == 0 and W == 0

    # Busca em profundidade com prevenção de ciclos
    def busca_dfs(self, estado_inicial):
        pilha = [(estado_inicial, [])]

        while pilha:
            estado_atual, caminho = pilha.pop()
            print(f"Explorando: {estado_atual}")

            # Verifica se o estado é objetivo
            if self.estado_objetivo(estado_atual):
                return caminho + [estado_atual]

            # Adiciona o estado atual aos visitados para evitar ciclos
            if estado_atual in self.visitados:
                continue
            self.visitados.add(estado_atual)

            # Geração de novos estados a partir das ações possíveis
            for acao in ['aspirar', 'entrarSala1', 'entrarSala2', 'entrarSala3']:
                novo_estado = self.oper(acao, estado_atual)
                if novo_estado not in self.visitados:
                    pilha.append((novo_estado, caminho + [estado_atual]))

        return None  # Caso não encontre solução


# Definição do estado inicial (aspirador na sala1, todas as salas sujas)
estado_inicial = ('sala1', 1, 1, 1)

# Criação do problema do aspirador
aspirador = AspiradorTresSalas()

# Executa a busca DFS para encontrar a solução
caminho_solucao = aspirador.busca_dfs(estado_inicial)

if caminho_solucao:
    print("Solução encontrada:")
    for estado in caminho_solucao:
        print(estado)
else:
    print("Nenhuma solução encontrada.")
