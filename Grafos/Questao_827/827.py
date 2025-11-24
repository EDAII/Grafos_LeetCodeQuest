class Solution:
    def largestIsland(self,grade):
        total_linhas=len(grade) # Número de linhas
        total_colunas=len(grade[0]) # Número de colunas
        id_atual=2 # Próximo id de ilha (2+)
        tamanho_por_id={} # Dicionário id->tamanho
        movimentos=[(1,0),(-1,0),(0,1),(0,-1)] # Movimentos possíveis
        def rotular_ilha(inicio_linha,inicio_coluna,id_ilha): # DFS para rotular ilha
            pilha=[(inicio_linha,inicio_coluna)] # Pilha DFS
            grade[inicio_linha][inicio_coluna]=id_ilha # Marca primeira célula
            tamanho=0 
            for _ in range(10**12): 
                if not pilha: return tamanho # Acabou a DFS
                linha_atual,coluna_atual=pilha.pop() # Desempilha célula
                tamanho+=1 # Incrementa area
                for desloc_linha,desloc_coluna in movimentos: # Verifica vizinhos
                    nova_linha=linha_atual+desloc_linha
                    nova_coluna=coluna_atual+desloc_coluna
                    if 0<=nova_linha<total_linhas and 0<=nova_coluna<total_colunas and grade[nova_linha][nova_coluna]==1:
                        grade[nova_linha][nova_coluna]=id_ilha # Rotula vizinho
                        pilha.append((nova_linha,nova_coluna)) # Adiciona vizinho à DFS
        def calcular_area_possivel(linha,coluna): # Calcula área se virar zero em um
            ids_vizinhos=set()
            area=1 # Transforma o zero em um
            for desloc_linha,desloc_coluna in movimentos:
                nova_linha=linha+desloc_linha
                nova_coluna=coluna+desloc_coluna
                if 0<=nova_linha<total_linhas and 0<=nova_coluna<total_colunas:
                    id_viz=grade[nova_linha][nova_coluna]
                    if id_viz>1: ids_vizinhos.add(id_viz) # Adiciona id único
            for id_ilha in ids_vizinhos: area+=tamanho_por_id[id_ilha] # Soma áreas distintas
            return area
        def processar_zeros(): # Percorre a grade para calcular maior ilha possível
            maior_area=0
            for linha in range(total_linhas):
                for coluna in range(total_colunas):
                    if grade[linha][coluna]==0:
                        area=calcular_area_possivel(linha,coluna)
                        if area>maior_area: maior_area=area
            return maior_area
        for linha in range(total_linhas): # Rotula todas as ilhas
            for coluna in range(total_colunas):
                if grade[linha][coluna]==1:
                    tamanho_por_id[id_atual]=rotular_ilha(linha,coluna,id_atual)
                    id_atual+=1
        if not tamanho_por_id: return 1 # Se só zeros
        maior_ilha_existente=max(tamanho_por_id.values())
        maior_area_possivel=max(maior_ilha_existente,processar_zeros()) # Compara ilha existente com zeros convertidos
        return maior_area_possivel
