class DirectedDFS:

    def __init__(self, G, s):
        # Vetor que indica se cada vértice já foi visitado
        self._marked = [False for _ in range(G.V)]

        # Inicia a DFS iterativa a partir da origem s
        self.dfs(G, s)

    def dfs(self, G, s):
        # Pilha que controla os próximos vértices a visitar
        stack = [s]

        # Enquanto houver vértices na pilha
        while stack:

            # Remove o último vértice inserido
            v = stack.pop()

            # Se v já foi visitado, não precisamos processá-lo novamente
            if self._marked[v]:
                continue

            # Marca v como visitado
            self._marked[v] = True

            # Adiciona à pilha os vizinhos ainda não visitados
            for w in G.adj[v]:
                if not self._marked[w]:
                    stack.append(w)

    def marked(self, v):
        # Retorna True se v foi alcançado pela DFS
        return self._marked[v]