"""Valida casos pequenos com as versões Python de referência da disciplina."""

from pathlib import Path

from algs4.edge import Edge
from algs4.edge_weighted_graph import EdgeWeightedGraph
from algs4.kruskal_mst import KruskalMST
from algs4.lazy_prim_mst import LazyPrimMST
from algs4.prim_mst import PrimMST


def verificar_distancias(matriz, estradas):
    vizinhos = [[] for _ in matriz]
    for u, v in estradas:
        vizinhos[u - 1].append(v - 1)
        vizinhos[v - 1].append(u - 1)

    for origem, linha in enumerate(matriz):
        distancias = [None] * len(matriz)
        distancias[origem] = 0
        pilha = [origem]
        while pilha:
            u = pilha.pop()
            for v in vizinhos[u]:
                if distancias[v] is None:
                    distancias[v] = distancias[u] + matriz[u][v]
                    pilha.append(v)
        assert distancias == linha


def prim_matricial(matriz):
    """Protótipo de estudo que opera sobre a matriz já carregada."""
    n = len(matriz)
    marcado = [False] * n
    distancia = [float("inf")] * n
    pai = [None] * n
    distancia[0] = 0
    for _ in range(n):
        u = min((v for v in range(n) if not marcado[v]), key=distancia.__getitem__)
        marcado[u] = True
        for v, peso in enumerate(matriz[u]):
            if not marcado[v] and peso < distancia[v]:
                distancia[v] = peso
                pai[v] = u
    return {tuple(sorted((u + 1, v + 1))) for v, u in enumerate(pai) if u is not None}


def main():
    arquivo = Path(__file__).resolve().parents[1] / "dados/casos-de-teste.txt"
    algoritmos = (KruskalMST, LazyPrimMST, PrimMST)
    for bloco in arquivo.read_text(encoding="utf-8").split("\nCaso ")[1:]:
        if "\nEntrada:\n" not in bloco:
            continue
        titulo, conteudo = bloco.split("\nEntrada:\n")
        entrada, saida = conteudo.split("\nSaída esperada:\n")
        n, *linhas = entrada.strip().splitlines()
        n = int(n)
        matriz = [list(map(int, linha.split())) for linha in linhas]
        esperadas = {tuple(sorted(map(int, linha.split()))) for linha in saida.splitlines() if linha}
        assert len(matriz) == n and len(esperadas) == n - 1
        grafo = EdgeWeightedGraph(n)
        for u, linha in enumerate(matriz):
            assert len(linha) == n and linha[u] == 0
            for v in range(u + 1, n):
                assert 0 < linha[v] < 10**7 and linha[v] == matriz[v][u]
                grafo.add_edge(Edge(u, v, linha[v]))
        verificar_distancias(matriz, esperadas)
        peso = sum(matriz[u - 1][v - 1] for u, v in esperadas)
        print(f"Caso {titulo} — {n - 1} estradas, peso {peso}")
        obtidas = prim_matricial(matriz)
        assert obtidas == esperadas
        verificar_distancias(matriz, obtidas)
        print("  Prim matricial e reconstrução da matriz: OK")
        for algoritmo in algoritmos:
            try:
                arestas = algoritmo(grafo).edges()
            except (TypeError, ValueError, IndexError) as erro:
                print(f"  {algoritmo.__name__}: {type(erro).__name__}: {erro}")
                continue
            pares = [tuple(sorted((e.v + 1, e.w + 1))) for e in arestas]
            estado = "OK" if len(pares) == n - 1 and set(pares) == esperadas else f"divergência: {pares}"
            print(f"  {algoritmo.__name__}: {estado}")


if __name__ == "__main__":
    main()
