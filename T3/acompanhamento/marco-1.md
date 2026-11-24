# T3 — Lost Map

## Marco 1 — Formulação

### 1. Descrição do problema

O problema Lost Map, da plataforma Kattis, consiste em reconstruir um mapa de estradas que interligam um conjunto de vilas, utilizando apenas uma matriz contendo as distâncias entre todos os pares de vilas.

O objetivo é identificar as estradas originais da região, distinguindo conexões diretas de distâncias acumuladas entre diferentes vilas.

### 2. Entrada

A entrada contém um inteiro n, representando a quantidade de vilas, seguido de uma matriz quadrada n × n contendo as distâncias entre elas.

As distâncias são simétricas, positivas entre vilas distintas e iguais a zero na diagonal principal.

### 3. Saída

A saída deverá conter exatamente n − 1 linhas, cada uma composta por dois números inteiros u e v, representando uma estrada original entre duas vilas.

As vilas são numeradas de 1 até n.

### 4. Restrições

- 2 ≤ n ≤ 2500.
- As distâncias entre vilas diferentes são positivas e menores que 10⁷.
- A matriz de distâncias é simétrica.
- A solução possui exatamente n − 1 arestas.

### 5. Modelagem em grafos

O problema será modelado como um grafo completo, conexo, ponderado e não direcionado.

- Vértices: representam as vilas.
- Arestas: representam possíveis conexões entre pares de vilas.
- Pesos: representam as distâncias fornecidas na matriz.
- Representação inicial: matriz de pesos.
- Solução: árvore geradora mínima.

O grafo completo possui n(n − 1)/2 arestas candidatas, enquanto a solução contém exatamente n − 1 arestas.

### 6. Família do problema

O problema pertence à classe de Árvores Geradoras Mínimas (Minimum Spanning Tree — MST).

A MST permite recuperar as estradas originais porque, considerando a estrutura de árvore da rede original e seus pesos positivos, qualquer conexão indireta possui peso superior ao de cada estrada que compõe seu caminho.

A propriedade do corte garante que as estradas originais sejam selecionadas na árvore geradora mínima.

### 7. Estratégia preliminar

Os algoritmos de Prim e Kruskal serão avaliados no Marco 2.

Considerando a densidade do grafo e o formato matricial da entrada, Prim com matriz de adjacência é o candidato preliminar.

A decisão definitiva deverá considerar a implementação de referência algs4 disponibilizada pela disciplina.

### 8. Referências

- Kattis — Lost Map: [https://open.kattis.com/problems/lostmap](https://open.kattis.com/problems/lostmap)
- Ricardo Carubbi — A8: Árvore Geradora Mínima.
- Ricardo Carubbi — A9: Caminhos de Custo Mínimo.
- Sedgewick e Wayne — Algorithms, 4th Edition (algs4).
