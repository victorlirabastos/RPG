# Marco 1 — Modelagem

## Problema, entrada e saída

[Horror List, Kattis](https://open.kattis.com/problems/horror): selecionar o filme mais distante, por relações de similaridade, da lista de filmes considerados ruins pelo grupo. “Horror” não significa necessariamente o gênero terror.

A entrada contém `N H L`, depois `H` IDs distintos da Horror List e `L` pares `a b` de filmes similares.

| Símbolo | Significado | Restrição |
|---|---|---|
| N | Filmes, identificados de 0 a N−1 | 1 ≤ H < N ≤ 1000 |
| H | Quantidade de filmes ruins | IDs distintos, entre 0 e N−1 |
| L | Relações de similaridade | 0 ≤ L ≤ 10000 |
| a, b | Extremidades da relação | 0 ≤ a < b < N |

A saída é um único ID: o filme com maior Horror Index (HI). Em empate, o menor ID.

## Modelagem

- Vértice: um filme.
- Aresta: similaridade entre dois filmes, em ambos os sentidos.
- Grafo não direcionado, não ponderado, sem laços, possivelmente desconexo.
- Origens S: filmes da Horror List.
- `HI(v) = min{dist(v,s) : s ∈ S}`, contando arestas. Origens têm HI 0. Sem caminho até S, HI é infinito.

## Instância pequena comum aos quatro marcos

```text
7 2 6
0 5
0 1
1 2
2 3
3 4
4 5
3 6
```

```text
0 --- 1 --- 2 --- 3 --- 4 --- 5
                  |
                  6
```

`V={0,1,2,3,4,5,6}`, `E={(0,1),(1,2),(2,3),(3,4),(4,5),(3,6)}`, `S={0,5}`.

| Filme | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| HI esperado | 0 | 1 | 2 | 2 | 1 | 0 | 3 |

Saída esperada: `6`. Caminho mínimo de 6 até S: `6–3–4–5`.

## Hipótese inicial e validação

BFS com todas as origens inicialmente na mesma fila deve calcular os índices por níveis. DFS será estudada no Marco 3 para avaliar sua aplicabilidade.

O primeiro exemplo oficial, com `N=6`, `S={0,5,2}` e arestas `(0,1),(1,2),(4,5),(3,5),(0,2)`, tem saída `1`. As entradas completas estão em [casos-de-teste.txt](../dados/casos-de-teste.txt).

## Alterações e justificativas

Mantida a instância original do Marco 1. Corrigidos formatação, trecho incompleto do enunciado e distinção entre filmes ruins e gênero terror. A aresta `(3,6)` será mantida em todos os marcos para permitir comparação direta.

## Referências e registro da consolidação

Referência da disciplina: [T1](https://github.com/carubbi/RPG/blob/a3df01a7931344129dc5d7e16f6525ecc24a664b/mat-didatico/trabalhos/T1.md).
Código de referência: [algs4-java/algs4](https://github.com/carubbi/RPG/blob/a3df01a7931344129dc5d7e16f6525ecc24a664b/algs4-java/algs4), de Robert Sedgewick e Kevin Wayne.
Conteúdo anterior preservado no [histórico do repositório](https://github.com/viniciusfeitosaa/T1-RPG/tree/57d7a58).
Esta consolidação reorganiza o material existente e torna as evidências reproduzíveis, sem substituir o histórico dos marcos.
