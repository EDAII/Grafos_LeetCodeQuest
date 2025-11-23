from collections import deque 
class Solution:
    def shortestPathLength(self, graph):
        total_nos = len(graph) # Armazena o número total de nós
        objetivo = frozenset(range(total_nos)) 
        passos = 0 
        fila = deque() 
        visitados = set() 
        def inicializar_estado(indice): # Inicializa a fila com cada nó como ponto de partida
            estado = (indice, frozenset([indice])) # Nó atual
            fila.append(estado) # Adiciona o estado a fila
            visitados.add(estado) # Marca o estado como visitado
        for i in range(total_nos):
            inicializar_estado(i) # Para cada nó, inicializa a BFS a partir dele
        def processar_nivel():
            for _ in range(len(fila)):
                no_atual, nos_visitados = fila.popleft() # Para cada estado, remove o próximo estado da fila
                if nos_visitados == objetivo:
                    return True # Se todos os nós foram visitados, retorna True
                for vizinho in graph[no_atual]:
                    novo_visitado = nos_visitados | {vizinho} # Marca o vizinho como visitado
                    novo_estado = (vizinho, frozenset(novo_visitado)) # Novo estado a ser visitado
                    if novo_estado not in visitados:
                        visitados.add(novo_estado) # Marca o novo estado como visitado
                        fila.append(novo_estado) # Adiciona o novo estado a fila
            return False # Caso os nós não possam ser visitados, retorna False
        while fila:
            if processar_nivel(): # Processa o nível e verifica se todos os foram visitados
                return passos # Retorna o número de passos se a condição for satisfeita
            passos +=1 # Incrementa o número de passos após processar um nível
