Exercícios de Algoritmos de Busca
1. Algoritmo de Busca para o Problema do Mundo do Aspirador com Três Salas
Neste exercício, foi implementado um algoritmo de busca para o problema do aspirador com três salas, utilizando uma estratégia que evita ciclos. O algoritmo explora possíveis ações (aspirar ou mover para outra sala) e garante que todas as salas sejam aspiradas sem revisitar estados anteriores. O código utiliza uma fila para armazenar estados a serem explorados e um conjunto para registrar estados já visitados, evitando ciclos e garantindo uma busca eficiente.

2. Algoritmo de Busca para o Problema dos Jarros
Foi desenvolvido um algoritmo para resolver o problema dos jarros com capacidades de 3 e 4 litros, com o objetivo de atingir exatamente 2 litros no jarro de 4 litros. O código representa o estado dos jarros e considera ações como encher, esvaziar e transferir água entre os jarros. Utiliza uma busca em largura (BFS) para explorar possíveis estados e encontrar a sequência de ações necessária para alcançar o objetivo, mantendo um registro dos estados já visitados para evitar ciclos.

3. Algoritmo de Busca para o Problema do Fazendeiro
Este código implementa um algoritmo para ajudar um fazendeiro a atravessar um rio com uma raposa, uma galinha e milho, sem deixar condições desfavoráveis em sua ausência. O algoritmo explora movimentos do fazendeiro e os itens entre as margens do rio. Utiliza uma busca em largura (BFS) para encontrar a sequência de movimentos que leva todos os itens para a outra margem, garantindo que as condições sejam sempre respeitadas.

4. Algoritmo de Busca Gulosa no Mapa da Romênia
Foi implementado um algoritmo de busca gulosa para encontrar o caminho mais curto de Arad a Bucharest no mapa da Romênia. O código utiliza uma heurística baseada na distância estimada até o destino para priorizar estados promissores durante a busca. A busca gulosa explora estados com base em uma função de custo que combina o custo acumulado e a estimativa da distância restante, minimizando o número de estados visitados.

5. Algoritmo de Busca A* no Mapa da Romênia
Este exercício desenvolveu um algoritmo A* para encontrar o caminho mais curto entre Arad e Bucharest no mapa da Romênia. O código combina o custo real do caminho percorrido com uma heurística estimada para o custo restante até o destino. Utiliza uma estrutura de prioridade para explorar estados, garantindo que o caminho mais eficiente seja encontrado com o menor número possível de estados candidatos.

6. Algoritmo A* com Distância Euclidiana em Matriz
Foi criado um algoritmo A* para um problema de pathfinding em uma matriz M x N, com custos de movimentos laterais e diagonais. O código usa a distância Euclidiana como heurística para estimar o custo restante até o destino. O algoritmo encontra o caminho mais eficiente entre o ponto de origem e o destino, evitando obstáculos e minimizando o custo total do percurso. As ações são ajustadas para refletir os diferentes custos associados a movimentos laterais e diagonais.
