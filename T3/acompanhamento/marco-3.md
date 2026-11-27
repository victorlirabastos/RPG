Marco 3 --- Rastreamento manual do Lazy Prim
Problema: H --- Lost Map (Kattis)  
Algoritmo: Prim não otimizado (Lazy Prim)  
Integrantes: Vinicius Alves e Victor Lira
1. Objetivo
Este marco apresenta o funcionamento do algoritmo de Prim não otimizado,
conhecido como Lazy Prim. O foco é identificar as estruturas de
dados, apresentar seus estados iniciais, rastrear as operações e
justificar as decisões tomadas durante a execução.
2. Ideia do algoritmo
O Prim constrói uma árvore geradora mínima (MST): uma árvore que conecta
todos os vértices, sem ciclos, com o menor peso total possível.
O Lazy Prim mantém uma fila de prioridade com as arestas que saem dos
vértices visitados. A cada passo, remove a aresta de menor peso:
Se apenas uma extremidade foi visitada, aceita a aresta e visita o
novo vértice.
Se as duas extremidades já foram visitadas, descarta a aresta, pois
ela formaria um ciclo.
É chamado de Lazy porque arestas que se tornam obsoletas não são
removidas imediatamente da fila. Elas permanecem nela até serem
retiradas e verificadas.
3. Estruturas de dados
---
Estrutura                           Função
---
`marked[]`                          Vetor booleano que indica se cada
vértice já foi visitado.
`pq` (`MinPQ<Edge>`)                Fila de prioridade das arestas
candidatas, ordenadas pelo peso.
`mst` (`Queue<Edge>`)               Armazena as arestas selecionadas
para a árvore geradora mínima.
`weight`                            Acumula o peso total das arestas
selecionadas.
`EdgeWeightedGraph`                 Representa o grafo ponderado.
`Edge`                              Representa uma aresta, suas
extremidades e seu peso.
3.1 Estado inicial
Considerando quatro vértices (`0`, `1`, `2` e `3`):
``` python
marked = [False, False, False, False]
pq = MinPQ()       # vazia
mst = Queue()      # vazia
weight = 0
```
Todos os vértices começam não visitados; a fila de prioridade e a MST
começam vazias; o peso acumulado começa em zero. A execução começa pelo
vértice `0`.
4. Grafo do exemplo
Aresta     Peso
---
0--1          1
0--2          4
1--2          2
1--3          5
2--3          3
``` text
       1
   0-------1
    \     / \
   4 \   / 2 \ 5
      \ /     \
       2-------3
           3
```
5. Rastreamento manual
A fila de prioridade será exibida em ordem crescente de peso.
Etapa 0 --- Inicialização e visita ao vértice 0
O vértice `0` é marcado. As arestas que ligam `0` a vértices ainda não
visitados são inseridas na fila: `0–1` e `0–2`.
`marked = [True, False, False, False]`
`pq = [0–1 (1), 0–2 (4)]`
`mst = []`
`weight = 0`
Justificativa: ambas as arestas partem de um vértice visitado e
chegam a vértices não visitados, portanto são candidatas.
Etapa 1 --- Seleção de 0--1
A menor aresta é `0–1`, de peso `1`. Como `0` está visitado e `1` não, a
aresta é aceita. O vértice `1` é marcado e suas arestas para vértices
não visitados (`1–2` e `1–3`) entram na fila.
`marked = [True, True, False, False]`
`pq = [1–2 (2), 0–2 (4), 1–3 (5)]`
`mst = [0–1 (1)]`
`weight = 1`
Justificativa: a aresta conecta a árvore a um novo vértice, sem
criar ciclo.
Etapa 2 --- Seleção de 1--2
A menor aresta é `1–2`, de peso `2`. Como `1` está visitado e `2` não,
ela é aceita. O vértice `2` é marcado e a aresta `2–3`, de peso `3`, é
inserida.
`marked = [True, True, True, False]`
`pq = [2–3 (3), 0–2 (4), 1–3 (5)]`
`mst = [0–1 (1), 1–2 (2)]`
`weight = 3`
Justificativa: a aresta conecta um novo vértice sem formar ciclo.
Etapa 3 --- Seleção de 2--3
A menor aresta é `2–3`, de peso `3`. Como `2` está visitado e `3` não,
ela é aceita e o vértice `3` é marcado.
`marked = [True, True, True, True]`
`pq = [0–2 (4), 1–3 (5)]`
`mst = [0–1 (1), 1–2 (2), 2–3 (3)]`
`weight = 6`
Justificativa: todos os vértices estão conectados. A MST possui
`V - 1 = 3` arestas.
Etapa 4 --- Descarte de 0--2
A aresta `0–2`, de peso `4`, é retirada da fila. Seus dois extremos já
estão visitados. Adicioná-la criaria um ciclo, então ela é descartada.
`marked = [True, True, True, True]`
`pq = [1–3 (5)]`
`mst = [0–1 (1), 1–2 (2), 2–3 (3)]`
`weight = 6`
Etapa 5 --- Descarte de 1--3
A aresta `1–3`, de peso `5`, também possui os dois extremos visitados e
é descartada.
`marked = [True, True, True, True]`
`pq = []`
`mst = [0–1 (1), 1–2 (2), 2–3 (3)]`
`weight = 6`
Justificativa dos descartes: as arestas ligam vértices que já
pertencem à árvore. Incluí-las criaria ciclos e não conectaria novos
vértices.
Resultado
A MST contém:
`0–1`, peso `1`;
`1–2`, peso `2`;
`2–3`, peso `3`.
Peso total: `1 + 2 + 3 = 6`.
A árvore conecta os quatro vértices, possui três arestas e não contém
ciclos.
6. Explicação individual de uma etapa do código algs4
Uma etapa central do Lazy Prim é retirar a menor aresta da fila e
verificar se ela ainda pode ser utilizada.
``` java
Edge e = pq.delMin();
int v = e.either();
int w = e.other(v);

if (marked[v] && marked[w])
    continue;
```
Explicação:
`pq.delMin()` remove e retorna a aresta de menor peso.
`e.either()` obtém uma das extremidades da aresta.
`e.other(v)` obtém a outra extremidade.
`marked[v] && marked[w]` verifica se os dois vértices já foram
visitados.
`continue` descarta a aresta e passa à próxima iteração.
Essa verificação caracteriza o Lazy Prim: uma aresta pode permanecer na
fila mesmo depois de se tornar desnecessária. Ela só é descartada quando
chega sua vez de ser retirada. Se não for descartada, será adicionada à
MST, seu peso será acumulado e o vértice ainda não visitado será
explorado.
7. Relação com Lost Map
No problema Lost Map, cada vértice representa uma localidade e a
matriz de entrada informa as distâncias entre todos os pares de
vértices.
Podemos considerar cada par como uma aresta candidata, atribuindo a ela
o valor da matriz, e executar um algoritmo de árvore geradora mínima. A
MST recupera as conexões da árvore original: em uma árvore com pesos
positivos, a distância entre dois vértices é a soma dos pesos das
arestas do caminho entre eles, e as arestas originais formam uma árvore
de peso total mínimo entre as arestas candidatas.
No Lazy Prim, as arestas candidatas são organizadas na fila de
prioridade. O algoritmo seleciona as menores que conectam novos vértices
e descarta as que formariam ciclos.
8. Complexidade
Na implementação Lazy Prim, as arestas candidatas são inseridas e
removidas da fila de prioridade. Cada operação de inserção ou remoção
custa `O(log E)`.
Tempo: `O(E log E)`.
Espaço auxiliar: `O(E)` para a fila de arestas, além das
estruturas de marcação e resultado.
No Lost Map, a matriz representa uma aresta candidata para cada par de
vértices. Assim, o grafo completo possui `E = V(V - 1)/2` arestas.
Executar Lazy Prim sobre essas arestas pode exigir espaço e tempo
consideráveis.
9. Conclusão
O rastreamento mostra que o Lazy Prim constrói a árvore geradora mínima
selecionando a menor aresta disponível que conecta um vértice visitado a
outro ainda não visitado.
A fila de prioridade mantém as arestas candidatas, `marked[]` controla
os vértices visitados e `mst` registra as arestas escolhidas. Arestas
cujos dois extremos já foram visitados são descartadas quando removidas
da fila, evitando ciclos.
No exemplo, o algoritmo seleciona `0–1`, `1–2` e `2–3`, obtendo peso
total `6`.
Referências
Repositório indicado pelo grupo:
https://github.com/carubbi/RPG/tree/main/algs4-py
Princeton Algorithms --- Minimum Spanning Trees:
https://algs4.cs.princeton.edu/43mst/
Implementação de referência `LazyPrimMST`:
https://algs4.cs.princeton.edu/43mst/LazyPrimMST.java
Observação: o trecho de código segue a implementação de referência
do Lazy Prim da biblioteca algs4 de Princeton. A pasta específica
`algs4-py` do repositório indicado não pôde ser inspecionada diretamente
nesta conversa; portanto, nomes e sintaxe podem variar na versão Python
utilizada pelo grupo.   