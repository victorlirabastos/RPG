# Marco 3 — Aplicação básica de DFS

## Referência e objetivo

O estudo segue [DepthFirstPaths](https://github.com/carubbi/RPG/blob/a3df01a7931344129dc5d7e16f6525ecc24a664b/algs4-java/algs4/DepthFirstPaths.java), de Sedgewick e Wayne: marca o vértice, percorre vizinhos, registra o predecessor de cada novo vértice e aprofunda por recursão.

A DFS serve à análise exigida neste marco. A solução final em Main usa BFS; não executa DFS nem armazena tempos ou predecessores. As tabelas abaixo são evidência de **execução manual**, não saída da Main.

## Ordem de visita e árvore

Origem 0 e a ordem de vizinhos da Bag descrita no [Marco 2](marco-2.md). Primeiras visitas: `0,1,2,3,6,4,5`. Em 3, o primeiro vizinho é 6. Após terminar 6, retorna a 3, segue a 4 e então a 5.

```text
0
└── 1
    └── 2
        └── 3
            ├── 6
            └── 4
                └── 5
```

## Estados, predecessores e tempos

Na referência, `marked` é false até a descoberta e true a partir dela. Na descrição manual, branco indica não descoberto, cinza indica chamada ativa e preto indica chamada terminada. O vetor booleano sozinho não diferencia cinza de preto. A referência básica não mede tempos; o relógio abaixo é uma anotação manual adicional para o requisito do marco.

Começamos o relógio em zero e o incrementamos na descoberta e no término.

| v | Predecessor | Descoberta | Término |
|---|---|---|---|
| 0 | −1 (raiz) | 1 | 14 |
| 1 | 0 | 2 | 13 |
| 2 | 1 | 3 | 12 |
| 3 | 2 | 4 | 11 |
| 4 | 3 | 7 | 10 |
| 5 | 4 | 8 | 9 |
| 6 | 3 | 5 | 6 |

Todos são alcançáveis a partir de 0. Ao terminar, todos estão marcados. O caminho da árvore de 0 a 6 é `0–1–2–3–6`, com 4 arestas.

## Aplicabilidade e adaptação parcial

O HI de 6 é 3, porque a origem 5 está mais perto: `6–3–4–5`. Assim, mesmo nesta árvore, a profundidade da DFS de origem única 0 não calcula o mínimo até todas as origens.

Em grafos com ciclos, a DFS também não garante distância mínima nem para uma origem. Exemplo: arestas `(0,1),(1,2),(0,2)`, visitando 1 antes de 2. A DFS descobre 2 pelo caminho `0–1–2`, apesar da aresta direta `(0,2)`.

A adaptação parcial consiste em usar DFS para alcançabilidade e caminhos; o cálculo final do Horror Index requer a garantia da BFS. Com lista de adjacência, uma DFS tem O(V+E) de tempo e O(V) de espaço adicional, contando a pilha. A BFS tem o mesmo limite de tempo, mas a propriedade necessária de distância mínima.

## Registro da revisão

A versão anterior simulava vizinhos em ordem crescente e visitava 4 antes de 6. Esta versão usa a ordem real da Bag, visitando 6 antes de 4. Os tempos mudam, mas o grafo, a alcançabilidade e a conclusão sobre DFS permanecem os mesmos. A classe auxiliar de demonstração foi retirada do pacote por não ser dependência da solução; a evidência manual completa permanece neste arquivo.
