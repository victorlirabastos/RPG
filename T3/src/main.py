"""Reconstrói as estradas originais com Prim matricial."""

from array import array
import sys


def estradas_originais(matriz):
    n = len(matriz)
    marcado = [False] * n
    distancia = [float("inf")] * n
    pai = [-1] * n
    distancia[0] = 0

    for _ in range(n):
        escolhido = -1
        menor = float("inf")
        for vila in range(n):
            if not marcado[vila] and distancia[vila] < menor:
                escolhido = vila
                menor = distancia[vila]

        marcado[escolhido] = True
        if pai[escolhido] != -1:
            yield pai[escolhido] + 1, escolhido + 1

        for vila, peso in enumerate(matriz[escolhido]):
            if not marcado[vila] and peso < distancia[vila]:
                distancia[vila] = peso
                pai[vila] = escolhido


def main():
    entrada = sys.stdin.buffer
    n = int(entrada.readline())
    matriz = [array("I", map(int, entrada.readline().split())) for _ in range(n)]
    sys.stdout.writelines(f"{u} {v}\n" for u, v in estradas_originais(matriz))


if __name__ == "__main__":
    main()
