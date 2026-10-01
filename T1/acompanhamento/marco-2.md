# Marco 2 — Representação computacional

## Representação escolhida e referência

Em [Main.java](../src/Main.java), `Graph` armazena `List<Integer>[] adj`, com uma `ArrayList<Integer>` por vértice. A referência é [Graph de Sedgewick e Wayne](https://github.com/carubbi/RPG/blob/a3df01a7931344129dc5d7e16f6525ecc24a664b/algs4-java/algs4/Graph.java), disponibilizada pelo professor. A adaptação substitui Bag por ArrayList da biblioteca padrão, mantendo o vetor de listas, V, E e inserção nos dois sentidos. A iteração segue a ordem de inserção, não sua inversa.

Listas ocupam O(V+E), enquanto uma matriz reservaria O(V²). Inserir ao final de uma ArrayList custa O(1) amortizado. Não há classe Bag na implementação entregue.

## Leitura e construção passo a passo

`Scanner.nextInt()` lê N, H, L, os H IDs e os L pares, independentemente das quebras de linha entre inteiros. A Main processa uma instância por execução, sem rótulos ENTRADA/SAIDA. Para a entrada do [Marco 1](marco-1.md), N=7, H=2, L=6 e `horrorList=[0,5]`.

`new Graph(N)` cria sete listas vazias, inclusive para eventuais isolados. Cada `addEdge(v,w)` executa `adj[v].add(w)`, `adj[w].add(v)` e incrementa E uma vez.

| Par lido | Listas alteradas após inserir | E acumulado |
|---|---|---|
| 0 1 | 0: [1]; 1: [0] | 1 |
| 1 2 | 1: [0,2]; 2: [1] | 2 |
| 2 3 | 2: [1,3]; 3: [2] | 3 |
| 3 4 | 3: [2,4]; 4: [3] | 4 |
| 4 5 | 4: [3,5]; 5: [4] | 5 |
| 3 6 | 3: [2,4,6]; 6: [3] | 6 |

## Adjacências e medidas estruturais

```text
0: 1
1: 0 2
2: 1 3
3: 2 4 6
4: 3 5
5: 4
6: 3
```

| Vértice | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| Grau | 1 | 2 | 2 | 3 | 2 | 1 | 1 |

Ordem V=7, tamanho E=6, grau mínimo 1 e máximo 3. Soma dos graus 12=2E. A instância é conexa e tem V−1 arestas, portanto é uma árvore. O problema geral admite ciclos e desconexão.

## Validação e custo

Cada relação aparece em ambas as listas e todos os sete vértices estão representados. As seis inserções produzem exatamente as adjacências acima e a soma 12. O caso `instancia-pequena` do [executor](../testes/verificar.py) confirma a saída 6; os casos desconexo e sem-arestas cobrem vértices sem acesso às fontes. A validação estrutural adicional do executor confere as listas reais de Graph e os vetores da BFS.

A construção leva O(V+E) no total, considerando inserções amortizadas. Percorrer todas as listas também custa O(V+E), com V listas e 2E entradas. A Main pressupõe as restrições válidas do Kattis: Graph não implementa validação explícita de IDs em addEdge; BreadthFirstPaths valida as origens e os vértices consultados. Isso não equivale a validar todo o arquivo de entrada.

## Registro da correção

A implementação entregue é o arquivo integral fornecido da submissão 20400623. A documentação foi alinhada a essa implementação, sem modificar o código submetido. Os Marcos 3 e 4 usam a ordem de adjacência acima.
