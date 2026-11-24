# Marco 2 — Escolha do algoritmo

**Decisão:** adaptar o Eager Prim do algs4 Python para trabalhar diretamente sobre a matriz de distâncias. A variante matricial conserva a melhor ligação por vértice e encontra o próximo vértice por varredura.

## ESTUDO 2.0 — comparar, justificar e conferir

Partimos de três perguntas do guia da Unidade 3. Qual é a decisão gulosa? Que estrutura permite executá-la? Qual operação domina o custo?

| Estratégia | Decisão e estrutura | Tempo total no Lost Map | Espaço auxiliar | Espaço total |
| --- | --- | --- | --- | --- |
| Kruskal | Processa arestas por peso, aceitando as que ligam componentes distintas em union-find. O algs4 Python usa uma fila de arestas. | O(n² + E log E) = O(n² log n) | O(E+n) = O(n²) | O(n²) |
| Lazy Prim | Seleciona a menor aresta na fila, descartando as que já têm os dois extremos na árvore. | O(n² + E log E) = O(n² log n) | O(E+n) = O(n²) | O(n²) |
| Eager Prim | Guarda a melhor ligação por vértice externo, com fila indexada e diminuição de chave. | O(n² + E log n) = O(n² log n) | O(n) | O(n²) |
| Prim matricial | Guarda a mesma melhor ligação por vértice e usa duas varreduras por inclusão. | Θ(n²) | Θ(n) | Θ(n²) |

Os custos de Kruskal, Lazy Prim e Eager Prim na tabela descrevem as variantes clássicas com as estruturas corretas, conforme A8 (pp. 35–58) e algs4. A leitura da matriz custa Θ(n²). O grafo completo tem E = n(n−1)/2, chegando a 3.123.750 arestas para n = 2500. O espaço auxiliar exclui a representação do grafo, que é quadrática no problema. Partindo da matriz, materializar uma lista de adjacência para chamar o algs4 adicionaria Θ(n²) de memória à entrada, inclusive para Eager Prim.

No Prim matricial, cada uma das n iterações varre até n posições para escolher o vértice externo de menor chave e percorre uma linha para atualizar as conexões. Os vetores de chaves, pais e marcação ocupam Θ(n). A matriz de entrada domina o espaço total. Para a integração, ler linha a linha e considerar armazenamento inteiro compacto evita manter a entrada tokenizada inteira junto com a matriz.

## Por que a escolha é correta

Iniciamos pela vila 1. Para cada vértice fora da árvore parcial, mantemos o menor peso de uma aresta que o liga à árvore e o pai que fornece essa ligação. A menor dessas chaves dá a menor aresta cruzando o corte. A propriedade do corte torna segura a inclusão. A linha do vértice recém-incluído permite atualizar o invariante. Após n−1 inclusões de arestas, obtemos a AGM única demonstrada no [Marco 1](marco1.md).

A chave do Prim é o peso de uma única ligação. O `distTo` do Dijkstra em A9 (pp. 21–26) acumula o comprimento de um caminho desde a origem.

## Instância pequena

A primeira amostra do Kattis é um K₄ com pesos:

| Vila | 1 | 2 | 3 | 4 |
| --- | ---: | ---: | ---: | ---: |
| 1 | 0 | 1 | 1 | 2 |
| 2 | 1 | 0 | 2 | 3 |
| 3 | 1 | 2 | 0 | 3 |
| 4 | 2 | 3 | 3 | 0 |

Começando em 1, as chaves de 2, 3 e 4 são 1, 1 e 2. Com desempate pelo menor ID, entram 2, 3 e 4, nessa ordem. As linhas de 2 e 3 oferecem à vila 4 peso 3, que não melhora sua ligação de peso 2. Saem os pares `1 2`, `1 3` e `1 4`, com peso total 4. Por exemplo, a distância indireta 2–4 é 1 + 2 = 3. O verificador recompõe todos os pares de distâncias da árvore resultante.

## Referência Python e execução

O material da disciplina disponibiliza `algs4-py/algs4/prim_mst.py` com `edgeTo`, `distTo`, `marked` e `IndexMinPQ`. O cabeçalho menciona Lazy Prim, mas o código mantém uma chave por vértice e tenta diminuí-la, caracterizando Eager Prim. Também estão disponíveis `kruskal_mst.py` e `lazy_prim_mst.py`. A adaptação planejada preserva os vetores do Eager Prim e substitui `EdgeWeightedGraph` pela matriz e `IndexMinPQ` pela seleção linear.

A porta Python de referência falhou com `TypeError` nas duas amostras oficiais. `IndexMinPQ.contains(i)` testa se o índice aparece em `keys`, que guarda pesos. Um peso igual a um índice pode simular presença na fila. A chamada seguinte a `decrease_key` pode então comparar `None` com um inteiro. A implementação consultada também percorre `keys` nesse teste e copia a fila na extração. Por isso, o limite clássico do Eager Prim pressupõe uma fila indexada funcional e não descreve diretamente essa porta. Até uma execução completa do código consultado pode incorrer em Θ(n) por consulta de presença, além dos custos de heap.

O [registro de execução](../evidencias/validacao-marco2.txt) mostra que o protótipo matricial, Kruskal e Lazy Prim recuperaram os pares esperados nos cinco casos pequenos. O protótipo também recompôs as cinco matrizes. O caso gerado com n = 2500 fica para a fase de testes. Nenhuma solução foi submetida ao Kattis neste marco.

Reprodução com Python 3, a partir de `T3/`. Informe o caminho da pasta `algs4-py` do material da disciplina na revisão `a3df01a7931344129dc5d7e16f6525ecc24a664b` do repositório `carubbi/RPG`.

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/caminho/para/algs4-py python3 evidencias/validar-marco2.py
```

### Fontes

- Ricardo Carubbi, UNIFOR. A8 — Árvore Geradora Mínima, seções 1.4, 2 e 3.
- Ricardo Carubbi, UNIFOR. A9 — Caminhos de Custo Mínimo, seções 1.1 e 1.14.
- Ricardo Carubbi, UNIFOR. Guia de Estudos AV3, Unidade 3.
- [Princeton algs4, seção 4.3 — Minimum Spanning Trees](https://algs4.cs.princeton.edu/43mst/).
