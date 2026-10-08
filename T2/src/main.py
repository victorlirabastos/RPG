from digraph import Digraph
from directed_dfs import DirectedDFS


def main():
    # Lê a quantidade de cidades (vértices)
    # e de rotas aéreas (arestas direcionadas)
    n, m = map(int, input().split())

    # Cria o dígrafo com n vértices
    g = Digraph(n)

    # Lê as m rotas
    for _ in range(m):
        a, b = map(int, input().split())

        # O CSES numera as cidades de 1 até n.
        # Internamente usamos índices de 0 até n - 1.
        a -= 1
        b -= 1

        # Adiciona a rota direcionada a -> b
        g.add_edge(a, b)

    # --------------------------------------------------
    # 1ª DFS: verifica se a cidade 1 alcança todas as demais
    # --------------------------------------------------

    dfs = DirectedDFS(g, 0)

    for v in range(n):
        if not dfs.marked(v):
            print("NO")

            # Cidade 1 não consegue chegar até a cidade v + 1
            print(1, v + 1)
            return

    # --------------------------------------------------
    # 2ª DFS: verifica se todas as cidades alcançam a cidade 1
    # --------------------------------------------------

    reversed_graph = g.reverse()

    dfs_reversed = DirectedDFS(reversed_graph, 0)

    for v in range(n):
        if not dfs_reversed.marked(v):
            print("NO")

            # No grafo reverso:
            # 1 não consegue chegar até v + 1.
            #
            # Portanto, no grafo original:
            # v + 1 não consegue chegar até 1.
            print(v + 1, 1)
            return

    # Se as duas verificações passaram,
    # o dígrafo é fortemente conexo
    print("YES")


if __name__ == "__main__":
    main()