class Solution:
    def longestIncreasingPath(self, matrix):
        total_linhas = len(matrix) # Número de linhas da matriz
        total_colunas = len(matrix[0]) # Número de colunas da matriz
        memo = {} # Memoização de caminhos já calculados
        movimentos = [(1,0),(-1,0),(0,1),(0,-1)] # Movimentos possíveis: baixo, cima, direita, esquerda
        def dentro_limites(linha,coluna): 
            return 0<=linha<total_linhas and 0<=coluna<total_colunas # Verifica se célula está dentro da matriz
        def explorar_vizinhos(linha,coluna): # Retorna lista de vizinhos crescentes
            vizinhos = []
            k = 0
            while k < 4: # Percorre todas as direções
                desloc_linha, desloc_coluna = movimentos[k]
                nova_linha = linha + desloc_linha
                nova_coluna = coluna + desloc_coluna
                if dentro_limites(nova_linha,nova_coluna) and matrix[nova_linha][nova_coluna] > matrix[linha][coluna]:
                    vizinhos.append((nova_linha,nova_coluna)) # Adiciona vizinho maior
                k += 1
            return vizinhos
        def dfs(linha,coluna): 
            if (linha,coluna) in memo: return memo[(linha,coluna)] # Retorna resultado já calculado
            comprimento_maximo_local = 1 
            for vizinho_linha,vizinho_coluna in explorar_vizinhos(linha,coluna): # Expande para vizinhos maiores
                comprimento_maximo_local = max(comprimento_maximo_local, 1 + dfs(vizinho_linha,vizinho_coluna))
            memo[(linha,coluna)] = comprimento_maximo_local # Memoiza resultado
            return comprimento_maximo_local
        def processar_celula(linha,coluna,maior_caminho_global): # Atualiza maior caminho global a partir de célula
            return max(maior_caminho_global, dfs(linha,coluna))
        def processar_toda_matriz(): # Itera sobre todas as células da matriz
            maior_caminho_global = 0
            linha = 0
            while linha < total_linhas:
                coluna = 0
                while coluna < total_colunas:
                    maior_caminho_global = processar_celula(linha,coluna,maior_caminho_global) # Calcula DFS por célula
                    coluna += 1
                linha += 1
            return maior_caminho_global # Retorna o maior caminho encontrado
        return processar_toda_matriz() 
