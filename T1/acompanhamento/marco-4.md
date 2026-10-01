# Marco 4 — Aplicação básica de BFS e conclusão

## Execução manual multi-origem

Usamos a instância dos Marcos 1–3, com aresta `(3,6)` e origens `S={0,5}`. As duas origens recebem distância zero e entram na fila antes de qualquer expansão.

| Vértice retirado | Novos vértices | Fila depois |
|---|---|---|
| inicialização | 0, 5 (distância 0) | [0,5] |
| 0 | 1 (distância 1) | [5,1] |
| 5 | 4 (distância 1) | [1,4] |
| 1 | 2 (distância 2) | [4,2] |
| 4 | 3 (distância 2) | [2,3] |
| 2 | nenhum | [3] |
| 3 | 6 (distância 3) | [6] |
| 6 | nenhum | [] |

| Filme | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| Distância / HI | 0 | 1 | 2 | 2 | 1 | 0 | 3 |
| Predecessor | −1 | 0 | 1 | 4 | 5 | −1 | 3 |

Níveis: `{0,5}`, `{1,4}`, `{2,3}`, `{6}`. A floresta de predecessores contém `0–1–2` e `5–4–3–6`. Caminho de 6 até a origem mais próxima: `6–3–4–5`, três arestas. Resposta: **6**.

## DFS versus BFS

| Propriedade | DFS | BFS |
|---|---|---|
| Controle | Recursão ou pilha | Fila FIFO |
| Exploração | Aprofunda antes de retornar | Níveis de distância |
| Alcançabilidade e predecessores | Sim | Sim |
| Primeiro caminho é mínimo em grafo não ponderado | Sem garantia | Sim |
| Tempo com lista de adjacência | O(V+E) | O(V+E) |

A escolha da BFS decorre da garantia de distâncias mínimas, não de uma complexidade assintótica melhor que DFS.

## Referência, adaptação e integração

`BreadthFirstPaths(Graph, Iterable<Integer> sources)` da referência já oferece múltiplas origens. Preservamos a inicialização conjunta e a atualização `distTo[w] = distTo[v]+1`, marcando ao inserir na fila.

[Main.java](../src/Main.java) é o arquivo integral fornecido da submissão 20400623. Ele reúne as classes Main, Graph e BreadthFirstPaths no mesmo arquivo, usa Scanner para entrada, List/ArrayList para adjacências e Queue/ArrayDeque para a fila FIFO. Não depende de algs4 ou de arquivos Java externos.

A Main chama o construtor multi-origem de BreadthFirstPaths. A classe mantém `marked`, `edgeTo` e `distTo`; ao descobrir w a partir de v, grava `edgeTo[w]=v`, `distTo[w]=distTo[v]+1`, marca w e o enfileira. Os predecessores da tabela são reais para os vértices descobertos. O símbolo −1 nas raízes é apenas notação didática de ausência de pai: o vetor Java começa com zeros e não grava −1. Na instância, o vetor bruto é `edgeTo=[0,0,1,4,5,0,3]`. Para raízes e não alcançados, o valor padrão 0 não representa uma aresta de predecessor. O código oferece `edgeTo(v)`, mas não reconstrói nem imprime caminhos.

A ordem dos vizinhos é a da ArrayList do Marco 2. Após a busca, todos os sete vértices desta instância têm `marked=true`.

Os não alcançados permanecem com `Integer.MAX_VALUE`, maior que qualquer distância finita possível (no máximo N−1). Nenhum infinito entra na fila, portanto não há soma de 1 ao sentinela. A varredura de IDs é crescente e só atualiza a resposta com `>`, preservando o menor ID em empates, inclusive de infinito.

## Correção e complexidade

Todas as origens começam no nível zero. Quando a fila processa o nível k, todos os níveis menores já foram processados. Um vértice descoberto recebe k+1, e um caminho mais curto o teria descoberto antes. Logo, cada distância é o mínimo até S. Os vértices não alcançados não têm caminho até S. A varredura final aplica a regra de máximo e desempate do enunciado.

Inicializar o grafo custa O(V), ler arestas O(E) e inicializar as fontes O(H). Uma BFS examina cada vértice no máximo uma vez e cada aresta não direcionada no máximo duas. Como H<V, o tempo total é **O(V+E)**. Espaço adicional da busca: **O(V)**. Espaço total, incluindo o grafo: **O(V+E)**.

## Testes, Accepted e ensaio

O [executor](../testes/verificar.py) recompila a Main fornecida com alvo Java 8 e executa os 10 casos de [casos-de-teste.txt](../dados/casos-de-teste.txt), 3 limites e 100 grafos pequenos comparados com Floyd–Warshall (semente 20260908). A revisão final obteve **113/113 casos aprovados**, além da conferência estrutural das adjacências e dos vetores reais da BFS. O registro está em [resultado.txt](../testes/resultado.txt).

A imagem [accepted.png](../evidencias/accepted.png), sem edição, mostra a submissão [20400623](https://open.kattis.com/submissions/20400623) de **Victor Lira Bastos: Horror List, Java, Accepted, 17/17, 0,26 s**. O código integral foi fornecido e copiado byte a byte para a entrega. Os 17 testes do Kattis são distintos dos testes locais. Não houve nova submissão nesta revisão.

A [apresentação](../apresentacao/apresentacao.pdf) conserva oito slides e o formato UNIFOR, atualizados para essa implementação e evidência. O [roteiro de ensaio](revisao-feedback.md) prevê 4min50s. A documentação não comprova apresentação passada dos marcos nem substitui o ensaio dos integrantes.

## Diferencial, adaptações e custo dominante

A única BFS com H origens evita H buscas separadas, que poderiam custar O(H(V+E)). O suporte multi-origem já pertence ao [BreadthFirstPaths de Sedgewick e Wayne](https://github.com/carubbi/RPG/blob/a3df01a7931344129dc5d7e16f6525ecc24a664b/algs4-java/algs4/BreadthFirstPaths.java). A adaptação usa coleções Java padrão, entrada Scanner e seleção do ID conforme o problema. Os vetores e a descoberta por níveis foram preservados.

A construção com ArrayList custa O(V+E) no total por inserções amortizadas O(1). As operações de ArrayDeque também têm custo O(1) amortizado. Construção e BFS têm o mesmo limite O(V+E); selecionar o ID custa O(V). Não houve medição isolada por etapa. Os 0,26 s pertencem ao registro do Kattis, não ao tempo dos testes locais.

## Conferência com o código

| Trecho | Demonstração na instância |
|---|---|
| Construtor multi-origem e bfs(Graph, Iterable) | Distâncias começam em infinito; 0 e 5 recebem zero e entram na fila antes da expansão. |
| Bloco `if (!marked[w])` | Ao retirar 4, descobre 3, grava edgeTo[3]=4 e distTo[3]=2. Quando 2 examina 3, a marca impede nova descoberta. |
| Marcação antes de queue.add(w) | Cada vértice entra na fila uma vez, considerando fontes distintas como exige o enunciado. |
| Laço final da Main | Começa com result=0, examina IDs de 1 a N−1 e só substitui com `>`; retorna 6. |

As adjacências examinadas pela ordem da fila são `0:[1]`, `5:[4]`, `1:[0,2]`, `4:[3,5]`, `2:[1,3]`, `3:[2,4,6]`, `6:[3]`, totalizando 12 entradas. A ordem de retirada é `0,5,1,4,2,3,6`.

No caso empate-finito, 2 e 3 têm HI=2 e vence 2. No caso desconexo, S={0}, HI=[0,1,2,∞,∞], e vence 3. A fila só recebe vértices de distância finita, evitando overflow por soma ao sentinela. Os vértices desconexos permanecem `marked=false`, `distTo=Integer.MAX_VALUE` e `edgeTo=0` sem significado de pai.

Para reproduzir: `python3 testes/verificar.py`, dentro de `RPG/T1`. A comparação diferencial valida a implementação empiricamente; a prova por níveis justifica o algoritmo.
