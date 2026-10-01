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

[Main.java](../src/Main.java) mantém a versão final existente no repositório: classes internas `Bag`, `Graph` e `Queue`, leitura com `BufferedReader`/`StringTokenizer`, BFS no método principal e seleção da resposta. Não depende de arquivos `Graph.java` ou `BreadthFirstPaths.java` externos. O código original foi apenas movido, sem alterar bytes.

A versão de submissão omite `edgeTo`, pois o Kattis pede somente o ID. Os predecessores acima são anotações da simulação manual, seguindo o momento em que cada vértice é descoberto. A solução final não armazena esse vetor. A ordem dos vizinhos é a da Bag do Marco 2.

Os não alcançados permanecem com `Integer.MAX_VALUE`, maior que qualquer distância finita possível (no máximo N−1). Nenhum infinito entra na fila, portanto não há soma de 1 ao sentinela. A varredura de IDs é crescente e só atualiza a resposta com `>`, preservando o menor ID em empates, inclusive de infinito.

## Correção e complexidade

Todas as origens começam no nível zero. Quando a fila processa o nível k, todos os níveis menores já foram processados. Um vértice descoberto recebe k+1, e um caminho mais curto o teria descoberto antes. Logo, cada distância é o mínimo até S. Os vértices não alcançados não têm caminho até S. A varredura final aplica a regra de máximo e desempate do enunciado.

Inicializar o grafo custa O(V), ler arestas O(E) e inicializar as fontes O(H). Uma BFS examina cada vértice no máximo uma vez e cada aresta não direcionada no máximo duas. Como H<V, o tempo total é **O(V+E)**. Espaço adicional da busca: **O(V)**. Espaço total, incluindo o grafo: **O(V+E)**.

## Testes, Accepted e ensaio

[Casos de teste](../dados/casos-de-teste.txt): 2 exemplos oficiais e 8 casos de estudo com entradas e saídas completas. Há ainda descrições reproduzíveis de 3 limites. A Main isolada foi compilada com alvo Java 8 e passou nos 113 casos locais em 10/09/2026: 10 documentados, 3 limites e 100 grafos pequenos aleatórios comparados com Floyd–Warshall (semente 20260908). O registro é histórico; a revisão inclui agora [um executor reproduzível](../testes/verificar.py) e [seu resultado](../testes/resultado.txt), sem incorporá-lo à solução submetida. A comparação independente é validação empírica adicional; a justificativa de correção está acima.

A imagem [accepted.png](../evidencias/accepted.png), preservada sem edição, mostra **Accepted**, Java, 17/17, 0,11 s, submissão [20374292](https://open.kattis.com/submissions/20374292). Os 17 testes pertencem ao Kattis, não são os testes locais. A captura não mostra as entradas nem permite comparar todo o código submetido byte a byte. Não houve nova submissão nesta revisão.

A [apresentação](../apresentacao/apresentacao.pdf) tem oito slides, com capa UNIFOR, identificação e matrículas na subcapa, planejados para 4min50s. Todos os slides têm referências no rodapé. O roteiro e o lembra-memória ficam fora do pacote do repositório. O grupo deve realizar o ensaio oral.

## Diferencial e custo dominante

A escolha relevante é uma única BFS com H origens, evitando H buscas separadas, que poderiam custar O(H(V+E)). O suporte multi-origem já pertence ao algs4; nosso trabalho aplica esse recurso ao índice do problema e integra entrada, infinito e desempate.

A BFS e a construção do grafo têm, ambas, limite O(V+E). São as etapas de maior ordem assintótica da solução, enquanto selecionar o ID custa O(V). Não foi medido o tempo de cada etapa isoladamente. O tempo de 0,11 s da captura é o tempo informado para aquela submissão.

## Referência, alterações e justificativas

Referência: [BreadthFirstPaths](https://github.com/carubbi/RPG/blob/a3df01a7931344129dc5d7e16f6525ecc24a664b/algs4-java/algs4/BreadthFirstPaths.java), do material do professor, baseada em Sedgewick e Wayne. A BFS foi incorporada à Main com as estruturas encadeadas da referência. A leitura atende ao Kattis. A reconstrução de caminhos foi omitida porque a saída pede apenas um ID. A ordem de marcação e atribuição da distância dentro do bloco de descoberta não altera o algoritmo: ambas ocorrem antes de enfileirar.

Mantida a aresta `(3,6)` dos Marcos 1–3, com `pred[6]=3` e caminho `6–3–4–5`. O Main original foi preservado. Na consolidação anterior, as classes auxiliares e os registros separados de testes ficaram fora do pacote. Esta revisão acrescenta o executor e o resultado em testes/, mantendo a solução autossuficiente.

## Revisão do feedback: código, evidências e ensaio

O registro acima da submissão 20374292 descreve a captura anterior, da conta de Vinícius. A evidência efetivamente citada pelo professor é [accepted-20400623.png](../evidencias/accepted-20400623.png): submissão [20400623](https://open.kattis.com/submissions/20400623), conta Victor Lira Bastos, Horror List, Java, Accepted, 17/17, 0,26 s. Ambas foram preservadas e identificadas separadamente. Os imports diferentes na 20400623 impedem atribuir o código integral daquela submissão à Main atual apenas pela captura. Não foi feita nova submissão nem substituição da implementação.

| Trecho da Main | Como demonstrar na instância pequena |
|---|---|
| [Inicialização, linhas 211–223](../src/Main.java#L211) | Todos começam em infinito; 0 e 5 recebem zero e entram na fila antes da expansão. |
| [Laço da busca, linhas 225–234](../src/Main.java#L225) | Retirar 4 descobre 3 com distância 2. Ao processar 2, o vizinho 3 já está marcado; não muda de pai nem de distância. |
| [Marcação, linhas 228–231](../src/Main.java#L228) | Marcar antes de enfileirar impede entradas duplicadas e mantém uma descoberta por vértice. |
| [Seleção, linhas 236–247](../src/Main.java#L236) | As distâncias `[0,1,2,2,1,0,3]` levam a 6. No caso empate-finito, 2 e 3 têm HI=2; `>` mantém 2. |

As adjacências examinadas, pela ordem da fila, são `0:[1]`, `5:[4]`, `1:[2,0]`, `4:[5,3]`, `2:[3,1]`, `3:[6,4,2]`, `6:[3]`. Apenas vizinhos ainda não marcados entram na fila. Isso confere a tabela manual com as 12 entradas da representação. Os predecessores são didáticos; `edgeTo` não existe na Main final.

No caso desconexo documentado, S={0}, HI=[0,1,2,∞,∞]: 3 ganha por ser o menor ID com infinito. A fila só contém distâncias finitas, evitando somar 1 a `Integer.MAX_VALUE`.

Para reproduzir a validação, execute `python3 testes/verificar.py` dentro de `RPG/T1`. O relatório atual registra compilação e 113 resultados; os dez casos originais e os três limites não foram alterados. O roteiro técnico de ensaio e as pendências estão no [registro da revisão](revisao-feedback.md). O ensaio oral continua a ser realizado pelos integrantes; o registro não afirma uma apresentação retroativa dos marcos 2 e 4.
