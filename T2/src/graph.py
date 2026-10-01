class Graph:

    def __init__(self, v):
        # Quantidade de vértices do grafo
        self.V = v

        # Quantidade de arestas do grafo
        # O grafo começa sem nenhuma aresta
        self.E = 0

        # Lista de adjacência
        # Para cada vértice, criamos uma lista vazia de vizinhos
        self.adj = [[] for _ in range(self.V)]

    def __str__(self):
        # Cria a primeira linha da representação textual do grafo
        lines = [f"{self.V} vertices, {self.E} edges"]

        # Percorre todos os vértices
        for v in range(self.V):

            # Converte os vizinhos do vértice para texto
            # e separa cada um deles por espaço
            neighbors = " ".join(str(w) for w in self.adj[v])

            # Adiciona uma linha no formato:
            # 0: 1 2 3
            lines.append(f"{v}: {neighbors}")

        # Junta todas as linhas usando quebra de linha
        return "\n".join(lines)

    def add_edge(self, v, w):
        # Garante que os vértices recebidos sejam inteiros
        v = int(v)
        w = int(w)

        # Adiciona w à lista de vizinhos de v
        self.adj[v].append(w)

        # Adiciona v à lista de vizinhos de w
        # Isso ocorre porque nosso grafo é não direcionado
        self.adj[w].append(v)

        # Incrementa o número de arestas
        self.E += 1

    def degree(self, v):
        # O grau de um vértice é a quantidade de vizinhos dele
        return len(self.adj[v])

    def max_degree(self):
        # Inicialmente assumimos que o maior grau é zero
        max_deg = 0

        # Percorre todos os vértices
        for v in range(self.V):

            # Compara o maior grau atual com o grau do vértice v
            max_deg = max(max_deg, self.degree(v))

        # Retorna o maior grau encontrado
        return max_deg

    def number_of_self_loops(self):
        # Contador de auto-laços
        count = 0

        # Percorre todos os vértices
        for v in range(self.V):

            # Percorre todos os vizinhos de v
            for w in self.adj[v]:

                # Se v possui uma aresta para ele mesmo,
                # encontramos um auto-laço
                if w == v:
                    count += 1

        # Cada auto-laço aparece duas vezes na lista de adjacência
        return count // 2