# Marco 3 — Aplicação básica de DFS

## Referência e objetivo

O estudo segue [DepthFirstPaths](https://github.com/carubbi/RPG/blob/a3df01a7931344129dc5d7e16f6525ecc24a664b/algs4-java/algs4/DepthFirstPaths.java), de Sedgewick e Wayne: marca o vértice, percorre vizinhos, registra o predecessor de cada novo vértice e aprofunda por recursão.

A DFS serve à análise exigida neste marco. A solução final em Main usa BFS; não executa DFS nem armazena tempos de DFS. Ela armazena os predecessores da BFS em `edgeTo`. As tabelas abaixo são evidência de **execução manual**, não saída da Main.

## Ordem de visita e árvore

Origem 0 e a ordem de inserção dos vizinhos na ArrayList descrita no [Marco 2](marco-2.md). Primeiras visitas: `0,1,2,3,4,5,6`. Em 3, ignora 2 já descoberto, visita 4 e depois 5. Após terminar 5 e 4, retorna a 3 e visita 6.

```text
0
└── 1
    └── 2
        └── 3
            ├── 4
            │   └── 5
            └── 6
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
| 4 | 3 | 5 | 8 |
| 5 | 4 | 6 | 7 |
| 6 | 3 | 9 | 10 |

Todos são alcançáveis a partir de 0. Ao terminar, todos estão marcados. O caminho da árvore de 0 a 6 é `0–1–2–3–6`, com 4 arestas.

## Aplicabilidade e adaptação parcial

O HI de 6 é 3, porque a origem 5 está mais perto: `6–3–4–5`. Assim, mesmo nesta árvore, a profundidade da DFS de origem única 0 não calcula o mínimo até todas as origens.

Em grafos com ciclos, a DFS também não garante distância mínima nem para uma origem. Exemplo: arestas `(0,1),(1,2),(0,2)`, visitando 1 antes de 2. A DFS descobre 2 pelo caminho `0–1–2`, apesar da aresta direta `(0,2)`.

A adaptação parcial consiste em usar DFS para alcançabilidade e caminhos; o cálculo final do Horror Index requer a garantia da BFS. Com lista de adjacência, uma DFS tem O(V+E) de tempo e O(V) de espaço adicional, contando a pilha. A BFS tem o mesmo limite de tempo, mas a propriedade necessária de distância mínima.

## Registro da revisão

A simulação foi recalculada para a ArrayList da submissão 20400623: 4 e 5 são visitados antes de 6. Os tempos mudam em relação à representação anterior; o grafo, a alcançabilidade e a conclusão sobre DFS permanecem. Não foi acrescentada DFS à Main.

## Rastreamento de cada mudança de estado

Vetor na ordem `[0,1,2,3,4,5,6]`: B = branco, C = cinza, P = preto. A pilha lista as chamadas ainda ativas, da raiz ao topo, **depois** de cada evento. Inicialmente todos estão B e `pred=-1`. Cada descoberta fixa o predecessor da tabela anterior; um vizinho já descoberto não recebe outro predecessor.

| Tempo | Evento | Estados 0 a 6 | Pilha ativa |
|---|---|---|---|
| 0 | inicialização | B B B B B B B | [] |
| 1 | descobre 0 | C B B B B B B | [0] |
| 2 | descobre 1 por 0 | C C B B B B B | [0,1] |
| 3 | descobre 2 por 1 | C C C B B B B | [0,1,2] |
| 4 | descobre 3 por 2 | C C C C B B B | [0,1,2,3] |
| 5 | descobre 4 por 3 | C C C C C B B | [0,1,2,3,4] |
| 6 | descobre 5 por 4 | C C C C C C B | [0,1,2,3,4,5] |
| 7 | termina 5 | C C C C C P B | [0,1,2,3,4] |
| 8 | termina 4 | C C C C P P B | [0,1,2,3] |
| 9 | descobre 6 por 3 | C C C C P P C | [0,1,2,3,6] |
| 10 | termina 6 | C C C C P P P | [0,1,2,3] |
| 11 | termina 3 | C C C P P P P | [0,1,2] |
| 12 | termina 2 | C C P P P P P | [0,1] |
| 13 | termina 1 | C P P P P P P | [0] |
| 14 | termina 0 | P P P P P P P | [] |

Na varredura de 6, o vizinho 3 já está cinza: não há chamada recursiva. Analogamente, 5 ignora 4. Os vértices 1, 2, 3 e 4 examinam e ignoram seus pais antes de aprofundar nos filhos, conforme a ordem da ArrayList. São as arestas de retorno ao pai no grafo não direcionado, não novos filhos da árvore. O relógio só avança nos eventos de descoberta/término.

Pseudocódigo da instrumentação manual, baseado em `DepthFirstPaths`:

```text
visitar(v):
    estado[v] = CINZA; descoberta[v] = ++tempo
    para w na ordem de G.adj(v):
        se estado[w] == BRANCO:
            pred[w] = v
            visitar(w)
    estado[v] = PRETO; termino[v] = ++tempo
```

Validação: há 14 eventos distintos (duas vezes V), seis arestas de árvore (V−1), e para todo filho w de v vale `d[v] < d[w] < f[w] < f[v]`. Os intervalos de 4 `[5,8]` e 6 `[9,10]` são separados e estão dentro de 3 `[4,11]`. Seguir os predecessores de 5 produz `5,4,3,2,1,0`, comprovando alcançabilidade, mas não o HI: 5 já pertence à Horror List e seu HI é zero.

Em uma instância desconexa, a DFS iniciada em 0 deixa brancos os vértices fora de sua componente; seus tempos ficam indefinidos e pred=-1. Para medir alcançabilidade até qualquer origem, poderíamos iniciar DFS em cada fonte ainda não marcada, compartilhando as marcas. Isso encontra a união das componentes das fontes, mas não garante as menores distâncias. Para Horror List, mantemos a BFS multi-origem.
