class Digraph:

    def __init__(self, v):
        # Quantidade de vértices
        self.V = v

        # Quantidade de arestas
        self.E = 0

        # Lista de adjacência
        self.adj = [[] for _ in range(self.V)]

    def add_edge(self, v, w):
        # Adiciona a aresta direcionada v -> w
        self.adj[v].append(w)

        # Incrementa a quantidade de arestas
        self.E += 1

    def reverse(self):
        # Cria o grafo reverso
        reversed_graph = Digraph(self.V)

        # Para cada aresta v -> w,
        # adiciona w -> v no reverso
        for v in range(self.V):
            for w in self.adj[v]:
                reversed_graph.add_edge(w, v)

        return reversed_graph


class DirectedDFS:

    def __init__(self, G, s):
        # Marca quais vértices foram alcançados
        self._marked = [False for _ in range(G.V)]

        # Executa a DFS a partir da origem
        self.dfs(G, s)

    def dfs(self, G, s):
        # Pilha explícita para evitar limite de recursão do Python
        stack = [s]

        while stack:

            # Remove o último elemento inserido
            v = stack.pop()

            # Ignora caso já tenha sido visitado
            if self._marked[v]:
                continue

            # Marca o vértice
            self._marked[v] = True

            # Adiciona os vizinhos ainda não visitados
            for w in G.adj[v]:
                if not self._marked[w]:
                    stack.append(w)

    def marked(self, v):
        return self._marked[v]


def main():
    # Lê número de cidades e de rotas
    n, m = map(int, input().split())

    # Constrói o dígrafo
    g = Digraph(n)

    # Lê as rotas
    for _ in range(m):
        a, b = map(int, input().split())

        # Converte de 1..n para 0..n-1
        a -= 1
        b -= 1

        # Adiciona a rota a -> b
        g.add_edge(a, b)

    # Primeira DFS:
    # verifica se a cidade 1 alcança todas as outras
    dfs = DirectedDFS(g, 0)

    for v in range(n):
        if not dfs.marked(v):
            print("NO")
            print(1, v + 1)
            return

    # Constrói o grafo reverso
    reversed_graph = g.reverse()

    # Segunda DFS:
    # verifica se todas as cidades alcançam a cidade 1
    dfs_reversed = DirectedDFS(reversed_graph, 0)

    for v in range(n):
        if not dfs_reversed.marked(v):
            print("NO")
            print(v + 1, 1)
            return

    # Se as duas verificações passaram,
    # o grafo é fortemente conexo
    print("YES")


if __name__ == "__main__":
    main()