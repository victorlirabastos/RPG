Marco 1 — Modelagem e análise inicial
O problema escolhido foi o CSES Flight Routes Check.
O problema apresenta n cidades e m rotas aéreas de mão única. O objetivo é verificar se é possível viajar de qualquer cidade para qualquer outra cidade, utilizando uma ou mais rotas.
A entrada começa com dois valores, n e m, representando respectivamente a quantidade de cidades e a quantidade de rotas aéreas. Em seguida, são fornecidas m linhas, cada uma contendo dois valores a e b, indicando que existe um voo da cidade a para a cidade b.
As restrições permitem até 100000 cidades e 200000 rotas, o que exige uma solução eficiente.
A saída deve ser YES caso seja possível viajar entre quaisquer duas cidades. Caso contrário, a saída deve ser NO, seguida de duas cidades a e b tais que não exista caminho da cidade a até a cidade b.
Na modelagem em grafos, cada cidade é representada por um vértice e cada rota aérea é representada por uma aresta dirigida. Portanto, o problema é representado por um grafo dirigido e não ponderado, pois as rotas possuem direção e não existem pesos associados às arestas.
A principal propriedade estrutural analisada é a forte conectividade. Um grafo dirigido é fortemente conexo quando, para quaisquer dois vértices u e v, existe um caminho de u até v e também um caminho de v até u.
O principal resultado de aprendizagem trabalhado no problema é a análise de conectividade em grafos dirigidos, envolvendo conceitos de alcançabilidade, forte conectividade e aplicação de algoritmos de busca como DFS ou BFS.
Como hipótese inicial de solução, pode-se escolher uma cidade de referência, como a cidade 1, e executar uma DFS ou BFS no grafo original. Essa primeira busca verifica se a cidade 1 consegue alcançar todas as demais cidades.
Em seguida, todas as arestas do grafo são invertidas, formando o grafo transposto. Uma nova DFS ou BFS é executada a partir da cidade 1. Essa segunda busca verifica, de forma equivalente, se todas as cidades conseguem chegar até a cidade 1 no grafo original.
Se todos os vértices forem visitados nas duas buscas, o grafo é fortemente conexo e a resposta é YES. Caso contrário, é possível identificar um par de cidades sem caminho entre elas e retornar NO.
Como instância pequena, podemos considerar quatro cidades e cinco rotas:
4 5
1 2
2 3
3 1
1 4
3 4
As cidades 1, 2 e 3 formam um ciclo e conseguem alcançar umas às outras. A cidade 4, porém, recebe rotas, mas não possui caminho de volta para as demais.
Por exemplo, é possível chegar da cidade 1 até a cidade 4, mas não é possível chegar da cidade 4 até a cidade 1.
Assim, uma saída válida seria:
NO
4 1
Com isso, o problema pode ser entendido como uma verificação de forte conectividade em um grafo dirigido. A estratégia inicial consiste em realizar duas buscas, uma no grafo original e outra no grafo com as arestas invertidas, com complexidade esperada de O(n + m).
