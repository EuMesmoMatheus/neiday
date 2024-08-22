from collections import deque

class ProblemaDosJarros:
    def __init__(self):
        self.visitados = set()

    # Função de transição de estados
    def oper(self, acao, estado):
        X, Y = estado

        # Ações para encher os jarros
        if acao == 'enche1' and X < 3:
            return (3, Y)
        elif acao == 'enche2' and Y < 4:
            return (X, 4)

        # Ações para esvaziar os jarros
        elif acao == 'esvazia1' and X > 0:
            return (0, Y)
        elif acao == 'esvazia2' and Y > 0:
            return (X, 0)

        # Transferir do jarro 1 para o jarro 2
        elif acao == 'transfere1para2' and X > 0:
            if X + Y <= 4:
                return (0, X + Y)
            else:
                return (X - (4 - Y), 4)

        # Transferir do jarro 2 para o jarro 1
        elif acao == 'transfere2para1' and Y > 0:
            if X + Y <= 3:
                return (X + Y, 0)
            else:
                return (3, Y - (3 - X))

        # Nenhuma ação válida, retorna o mesmo estado
        return estado

    # Verifica se o estado é o objetivo (jarro 2 com 2 litros)
    def estado_objetivo(self, estado):
        _, Y = estado
        return Y == 2

    # Busca em Largura (BFS) para encontrar a solução
    def busca_bfs(self, estado_inicial):
        fila = deque([(estado_inicial, [])])

        while fila:
            estado_atual, caminho = fila.popleft()
            print(f"Explorando: {estado_atual}")

            # Verifica se o estado é objetivo
            if self.estado_objetivo(estado_atual):
                return caminho + [estado_atual]

            # Adiciona o estado atual aos visitados para evitar ciclos
            if estado_atual in self.visitados:
                continue
            self.visitados.add(estado_atual)

            # Geração de novos estados a partir das ações possíveis
            for acao in ['enche1', 'enche2', 'esvazia1', 'esvazia2', 'transfere1para2', 'transfere2para1']:
                novo_estado = self.oper(acao, estado_atual)
                if novo_estado not in self.visitados:
                    fila.append((novo_estado, caminho + [estado_atual]))

        return None  # Caso não encontre solução


# Definição do estado inicial (jarros vazios)
estado_inicial = (0, 0)

# Criação do problema dos jarros
jarros = ProblemaDosJarros()

# Executa a busca BFS para encontrar a solução
caminho_solucao = jarros.busca_bfs(estado_inicial)

if caminho_solucao:
    print("Solução encontrada:")
    for estado in caminho_solucao:
        print(estado)
else:
    print("Nenhuma solução encontrada.")
