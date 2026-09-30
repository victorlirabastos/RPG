# Marco 2 — Representação computacional

## Representação escolhida e construção

Em [Main.java](../src/Main.java), cada filme corresponde a uma posição de `Bag<Integer>[] adj`, dentro da classe Graph. Cada Bag é uma lista simplesmente encadeada, seguindo Sedgewick e Wayne. A lista de adjacência usa O(V+E) de espaço, enquanto uma matriz reservaria O(V²).

A Main lê N, H, L, os H IDs distintos da Horror List e L relações. `new Graph(N)` cria uma Bag vazia por filme. `addEdge(a,b)` insere b na lista de a e a na lista de b, pois a similaridade vale nos dois sentidos. As operações add de Bag custam O(1).

## Instância pequena e ordem efetiva da Bag

Usando a entrada do [Marco 1](marco-1.md), na ordem em que as arestas aparecem, a iteração da Bag produz:

```text
0: 1
1: 2 0
2: 3 1
3: 6 4 2
4: 5 3
5: 4
6: 3
```

A Bag insere no início. Por isso a relação lida por último aparece primeiro na respectiva lista. A representação anterior dos marcos listava os mesmos vizinhos em ordem crescente; nesta consolidação a ordem da execução manual foi alinhada à estrutura realmente usada na Main. O conjunto de arestas e os índices não mudam.

| Vértice | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| Grau | 1 | 2 | 2 | 3 | 2 | 1 | 1 |

Ordem 7, tamanho 6, grau mínimo 1 e máximo 3. Soma dos graus 12=2×6, consistente com duas entradas por relação. A instância é conexa e tem V−1 arestas, portanto é uma árvore. O grafo geral do Horror List pode ter ciclos e ser desconexo.

## Validação e justificativa

Cada par da entrada aparece em ambas as listas. Não há vértice ausente. A soma dos graus confirma 12 entradas para 6 relações. A Main isolada retorna 6 para essa instância, como esperado.

A construção inteira leva O(V+E). Percorrer todos os vizinhos do grafo pela lista também leva O(V+E). A lista armazena apenas relações existentes e serve diretamente à BFS.

## Referência e alterações

Referência: [Graph](https://github.com/carubbi/RPG/blob/a3df01a7931344129dc5d7e16f6525ecc24a664b/algs4-java/algs4/Graph.java) e [Bag](https://github.com/carubbi/RPG/blob/a3df01a7931344129dc5d7e16f6525ecc24a664b/algs4-java/algs4/Bag.java), de Robert Sedgewick e Kevin Wayne, disponibilizadas pelo professor.

Mantidos o vetor de Bag, validação dos vértices e addEdge nos dois sentidos. A adaptação mantém as estruturas da referência e reúne as classes dentro da Main, eliminando dependências externas. Não foi preciso alterar o código final para esta consolidação. A tabela acima documenta sua ordem real de iteração.
