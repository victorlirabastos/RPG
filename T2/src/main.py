from graph import Graph
from depth_first_paths import DepthFirstPaths
from breadth_first_paths import BreadthFirstPaths


def main():
    # -----------------------------
    # 1. Construção do grafo
    # -----------------------------

    # Cria um grafo com 7 vértices:
    # 0, 1, 2, 3, 4, 5 e 6
    g = Graph(7)

    # Adiciona as arestas do grafo
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(1, 6)

    # -----------------------------
    # 2. Exibição do grafo
    # -----------------------------

    print("Grafo:")
    print(g)

    print("\nGrau do vértice 1:", g.degree(1))
    print("Maior grau:", g.max_degree())
    print("Número de auto-laços:", g.number_of_self_loops())

    # -----------------------------
    # 3. Definição da origem
    # -----------------------------

    origem = 0

    # -----------------------------
    # 4. Busca em Profundidade - DFS
    # -----------------------------

    dfs = DepthFirstPaths(g, origem)

    print("\nDFS:")

    for v in range(g.V):

        if dfs.has_path_to(v):

            caminho = list(dfs.path_to(v))

            print(
                f"{origem} até {v}: {caminho}"
            )

        else:

            print(
                f"{origem} e {v}: não conectados"
            )

    # -----------------------------
    # 5. Busca em Largura - BFS
    # -----------------------------

    bfs = BreadthFirstPaths(g, origem)

    print("\nBFS:")

    for v in range(g.V):

        if bfs.has_path_to(v):

            caminho = list(bfs.path_to(v))

            print(
                f"{origem} até {v}: {caminho}"
            )

        else:

            print(
                f"{origem} e {v}: não conectados"
            )


if __name__ == "__main__":
    main()