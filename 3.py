from collections import deque

class ProblemaDoFazendeiro:
    def __init__(self):
        self.visitados = set()

    # Função de transição de estados
    def oper(self, acao, estado):
        F, R, G, M = estado

        # Ações possíveis e suas respectivas transições de estado
        if acao == 'vaiSozinho' and F == 'e':
            if R != G or G != M:  # Não há perigo de algo ser comido
                return ('d', R, G, M)
        elif acao == 'levaRaposa' and F == 'e' and R == 'e' and G != M:
            return ('d', 'd', G, M)
        elif acao == 'levaGalinha' and F == 'e' and G == 'e':
            return ('d', R, 'd', M)
        elif acao == 'levaMilho' and F == 'e' and M == 'e' and R != G:
            return ('d', R, G, 'd')
        elif acao == 'voltaSozinho' and F == 'd':
            if R != G or G != M:  # Não há perigo de algo ser comido
                return ('e', R, G, M)
        elif acao == 'trazRaposa' and F == 'd' and R == 'd' and G != M:
            return ('e', 'e', G, M)
        elif acao == 'trazGalinha' and F == 'd' and G == 'd':
            return ('e', R, 'e', M)
        elif acao == 'trazMilho' and F == 'd' and M == 'd' and R != G:
            return ('e', R, G, 'e')

        # Retorna o estado original se nenhuma ação for aplicável
        return estado

    # Verifica se o estado é o objetivo (todos na margem direita)
    def estado_objetivo(self, estado):
        return estado == ('d', 'd', 'd', 'd')

    # Busca em largura (BFS)
    def busca_bfs(self, estado_inicial):
        fila = deque([(estado_inicial, [])])

        while fila:
            estado_atual, caminho = fila.popleft()

            # Verifica se o estado atual é o objetivo
            if self.estado_objetivo(estado_atual):
                return caminho + [estado_atual]

            # Evita revisitar estados
            if estado_atual in self.visitados:
                continue
            self.visitados.add(estado_atual)

            # Geração de novos estados a partir das ações possíveis
            for acao in ['vaiSozinho', 'levaRaposa', 'levaGalinha', 'levaMilho', 'voltaSozinho', 'trazRaposa', 'trazGalinha', 'trazMilho']:
                novo_estado = self.oper(acao, estado_atual)
                if novo_estado not in self.visitados:
                    fila.append((novo_estado, caminho + [estado_atual]))

        return None  # Caso não encontre solução


# Definição do estado inicial (todos na margem esquerda)
estado_inicial = ('e', 'e', 'e', 'e')

# Criação do problema do fazendeiro
fazendeiro = ProblemaDoFazendeiro()

# Executa a busca BFS para encontrar a solução
caminho_solucao = fazendeiro.busca_bfs(estado_inicial)

if caminho_solucao:
    print("Solução encontrada:")
    for estado in caminho_solucao:
        print(estado)
else:
    print("Nenhuma solução encontrada.")
