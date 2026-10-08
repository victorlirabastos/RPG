# Marco 4 — Implementação final e conclusão

## Problema

O problema utilizado no T2 foi o **Flight Routes Check**, da plataforma CSES:

https://cses.fi/problemset/task/1682

O problema recebe um conjunto de cidades e rotas aéreas direcionadas e solicita verificar se é possível viajar de qualquer cidade para qualquer outra.

Portanto, a propriedade central analisada é a **conectividade forte de um dígrafo**.

---

## Estratégia utilizada

A solução utiliza a cidade `1` como vértice de referência, representada internamente pelo índice `0`.

São realizadas duas buscas em profundidade (DFS):

1. uma DFS no dígrafo original;
2. uma DFS no dígrafo reverso.

### Primeira DFS — grafo original

Executa-se uma DFS a partir da cidade `1`.

Se algum vértice `v` não for visitado, então não existe caminho dirigido:

```text
1 -> v
```

Nesse caso, já existe um contraexemplo válido e a resposta é:

```text
NO
1 v
```

### Segunda DFS — grafo reverso

Se a primeira DFS alcançar todos os vértices, todas as arestas são invertidas.

Uma aresta:

```text
v -> w
```

passa a ser:

```text
w -> v
```

Em seguida, executa-se novamente uma DFS a partir da cidade `1`, agora no grafo reverso.

Se um vértice `v` não for alcançado no grafo reverso, isso significa que, no grafo original, não existe caminho:

```text
v -> 1
```

Assim, a resposta é:

```text
NO
v 1
```

Se todos os vértices forem alcançados nas duas buscas, então qualquer vértice `a` consegue chegar à cidade `1`, e a cidade `1` consegue chegar a qualquer vértice `b`.

Logo:

```text
a -> 1 -> b
```

para quaisquer vértices `a` e `b`.

Portanto, o dígrafo é fortemente conexo e a resposta é:

```text
YES
```

---

## Implementações de referência e adaptações

Foram utilizadas como referência as implementações disponibilizadas pelo professor no repositório `algs4-py`, principalmente:

- `Digraph`;
- `DirectedDFS`.

### Digraph

A implementação `Digraph` foi utilizada como referência para representar o grafo direcionado através de listas de adjacência.

Foram realizadas as seguintes adaptações:

- substituição da estrutura `Bag` por listas nativas do Python;
- manutenção dos atributos `V`, `E` e da lista de adjacência;
- manutenção da inserção direcionada de arestas;
- reutilização da lógica do método `reverse()`;
- remoção de operações que não eram necessárias ao problema, como grau máximo e contagem de auto-laços;
- adaptação da leitura da entrada para o formato utilizado pelo CSES.

Nos códigos-base anteriores do T2, a classe `Graph` representava um grafo não direcionado. Assim, uma aresta entre `v` e `w` era inserida nos dois sentidos.

Na implementação final do dígrafo:

```python
add_edge(v, w)
```

adiciona somente:

```text
v -> w
```

respeitando a direção das rotas aéreas.

### DirectedDFS

A implementação `DirectedDFS` foi utilizada como referência para verificar alcançabilidade em dígrafos.

Nos códigos-base anteriores do T2, a classe `DepthFirstPaths` também armazenava os predecessores através de `edge_to`, permitindo reconstruir os caminhos encontrados.

No `Flight Routes Check`, não é necessário reconstruir o caminho. É necessário apenas determinar se um vértice é alcançável.

Por isso, foram removidos:

- `edge_to`;
- reconstrução de caminhos;
- método `path_to()`.

Foi mantido somente o vetor que registra os vértices visitados.

A implementação de referência utiliza DFS recursiva. Na solução final, a busca foi adaptada para uma versão **iterativa utilizando uma pilha explícita**.

Essa modificação evita problemas com o limite de recursão do Python em entradas grandes, sem alterar a lógica da DFS nem sua complexidade assintótica.

### BreadthFirstPaths

A implementação de BFS construída anteriormente foi mantida como parte dos códigos-base do T2, mas não foi utilizada na solução final.

O problema exige apenas verificar alcançabilidade e conectividade forte, não sendo necessário calcular caminhos mínimos.

---

## Estrutura da implementação final

Durante o desenvolvimento do Marco 4 foram utilizados os seguintes arquivos:

```text
T2/src/
├── digraph.py
├── directed_dfs.py
├── main.py
└── submission.py
```

### `digraph.py`

Responsável por:

- representar o dígrafo através de lista de adjacência;
- adicionar arestas direcionadas;
- construir o grafo reverso.

### `directed_dfs.py`

Responsável por:

- executar DFS direcionada;
- marcar os vértices alcançáveis a partir de uma origem;
- utilizar uma pilha explícita para evitar problemas com recursão.

### `main.py`

Responsável por:

- ler a entrada;
- construir o dígrafo;
- executar a DFS no grafo original;
- construir o grafo reverso;
- executar a segunda DFS;
- produzir `YES` ou um contraexemplo `NO`.

### `submission.py`

Versão consolidada da solução em um único arquivo, utilizada para submissão na plataforma CSES.

---

## Complexidade

A representação utilizada é uma lista de adjacência.

A primeira DFS possui complexidade:

```text
O(V + E)
```

A construção do grafo reverso também percorre todos os vértices e todas as arestas:

```text
O(V + E)
```

A segunda DFS apresenta novamente:

```text
O(V + E)
```

Portanto:

```text
O(V + E) + O(V + E) + O(V + E)
```

resulta em complexidade assintótica:

```text
O(V + E)
```

O espaço utilizado pelas listas de adjacência, vetores de visitados e pilha da DFS é:

```text
O(V + E)
```

---

## Testes realizados

### Teste 1 — Caso mínimo

Entrada:

```text
1 0
```

Saída:

```text
YES
```

O único vértice é alcançável a partir dele mesmo.

---

### Teste 2 — Dígrafo fortemente conexo

Entrada:

```text
4 4
1 2
2 3
3 4
4 1
```

Saída:

```text
YES
```

Todos os vértices conseguem alcançar todos os demais.

---

### Teste 3 — Falha detectada na primeira DFS

Entrada:

```text
4 3
1 2
2 3
4 1
```

Saída:

```text
NO
1 4
```

A cidade `1` não consegue alcançar a cidade `4`.

---

### Teste 4 — Falha detectada através do grafo reverso

Entrada:

```text
3 3
1 2
2 1
1 3
```

Saída:

```text
NO
3 1
```

A cidade `1` consegue alcançar todas as cidades, porém a cidade `3` não consegue retornar para a cidade `1`.

Esse caso demonstra a necessidade da segunda DFS.

---

### Teste 5 — Dígrafo sem arestas

Entrada:

```text
3 0
```

Saída:

```text
NO
1 2
```

Como não existem rotas, a cidade `1` não consegue alcançar a cidade `2`.

---

### Teste 6 — Duas regiões fortemente conexas ligadas em um único sentido

Entrada:

```text
4 5
1 2
2 1
2 3
3 4
4 3
```

Representação simplificada:

```text
1 <-> 2 -> 3 <-> 4
```

A cidade `1` consegue alcançar todos os vértices, porém os vértices `3` e `4` não conseguem retornar para a primeira região.

A solução identifica corretamente que o dígrafo não é fortemente conexo e retorna `NO` acompanhado de um par válido.

---

### Teste 7 — Exemplo do CSES

Entrada:

```text
4 5
1 2
2 3
3 1
1 4
3 4
```

A implementação identifica corretamente que o dígrafo não é fortemente conexo.

O CSES aceita qualquer par `a b` para o qual não exista caminho dirigido de `a` até `b`, portanto a saída não precisa necessariamente coincidir com o par mostrado no exemplo oficial, desde que seja um contraexemplo válido.

---

## Resultado da submissão

A versão consolidada da solução foi submetida à plataforma CSES.

Resultado:

```text
ACCEPTED
```

A implementação foi aprovada nos testes da plataforma.

Evidência:

```text
T2/evidencias/accepted.png
```

---

## Conclusão

A implementação final resolve o `Flight Routes Check` utilizando duas buscas em profundidade.

A primeira DFS verifica se a cidade de referência consegue alcançar todos os vértices.

A segunda DFS é executada sobre o grafo reverso e verifica se todos os vértices conseguem alcançar a cidade de referência no grafo original.

Se as duas condições forem satisfeitas, para quaisquer vértices `a` e `b` existe:

```text
a -> 1 -> b
```

e, portanto, o dígrafo é fortemente conexo.

A estratégia permite resolver o problema sem identificar explicitamente todas as componentes fortemente conexas através do algoritmo completo de Kosaraju.

A solução possui complexidade:

```text
O(V + E)
```

e obteve:

```text
ACCEPTED
```

na plataforma CSES.