class Digraph:

    def __init__(self, v):
        # Quantidade de vértices do dígrafo
        self.V = v

        # Quantidade de arestas do dígrafo
        # Inicialmente não existe nenhuma aresta
        self.E = 0

        # Lista de adjacência
        # Cada posição representa um vértice
        # e armazena os vértices alcançados por arestas que saem dele
        self.adj = [[] for _ in range(self.V)]

    def __str__(self):
        # Cria a primeira linha da representação textual
        lines = [f"{self.V} vertices, {self.E} edges"]

        # Percorre todos os vértices
        for v in range(self.V):

            # Converte os vizinhos de v para texto
            neighbors = " ".join(str(w) for w in self.adj[v])

            # Adiciona a linha correspondente ao vértice
            lines.append(f"{v}: {neighbors}")

        # Junta todas as linhas com quebra de linha
        return "\n".join(lines)

    def add_edge(self, v, w):
        # Garante que os vértices sejam inteiros
        v = int(v)
        w = int(w)

        # Adiciona uma aresta direcionada de v para w
        self.adj[v].append(w)

        # Incrementa a quantidade de arestas
        self.E += 1

    def reverse(self):
        # Cria um novo dígrafo com a mesma quantidade de vértices
        reversed_graph = Digraph(self.V)

        # Percorre todos os vértices do dígrafo original
        for v in range(self.V):

            # Percorre todas as arestas que saem de v
            for w in self.adj[v]:

                # Se no original existe v -> w,
                # no reverso adicionamos w -> v
                reversed_graph.add_edge(w, v)

        # Retorna o dígrafo com todas as arestas invertidas
        return reversed_graph