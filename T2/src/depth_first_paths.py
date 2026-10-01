from graph import Graph


class DepthFirstPaths:

    def __init__(self, G, s):
        # Vetor que indica se cada vértice já foi visitado
        self.marked = [False for _ in range(G.V)]

        # Vetor de predecessores
        # Guarda por qual vértice chegamos a cada vértice
        self.edge_to = [0 for _ in range(G.V)]

        # Vértice de origem da busca
        self.s = s

        # Inicia a busca em profundidade a partir da origem
        self.dfs(G, s)

    def dfs(self, G, v):
        # Marca o vértice atual como visitado
        self.marked[v] = True

        # Percorre todos os vizinhos do vértice atual
        for w in G.adj[v]:

            # Se o vizinho ainda não foi visitado
            if not self.marked[w]:

                # Registra que chegamos em w através de v
                self.edge_to[w] = v

                # Continua a busca em profundidade a partir de w
                self.dfs(G, w)

    def has_path_to(self, v):
        # Se v foi visitado, existe caminho da origem até v
        return self.marked[v]

    def path_to(self, v):
        # Se não existe caminho até v, não há caminho para retornar
        if not self.has_path_to(v):
            return None

        # Lista que armazenará os vértices do caminho
        path = []

        # Começamos pelo vértice destino
        x = v

        # Voltamos pelos predecessores até chegar à origem
        while x != self.s:
            path.append(x)
            x = self.edge_to[x]

        # Adiciona também o vértice de origem
        path.append(self.s)

        # O caminho foi construído do destino para a origem,
        # por isso retornamos sua ordem invertida
        return reversed(path)