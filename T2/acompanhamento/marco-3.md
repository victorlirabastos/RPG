# Marco 3 — Estratégia Algorítmica

## Problema

O problema escolhido para o T2 é **Flight Routes Check**, da plataforma CSES.

O problema fornece um conjunto de cidades e rotas aéreas direcionadas. Cada cidade é representada por um vértice e cada rota `a → b` por uma aresta direcionada.

O objetivo é determinar se é possível viajar de qualquer cidade para qualquer outra cidade.

Caso isso seja possível, a saída deve ser:

YES

Caso contrário, deve ser informado:

NO
a b

onde não existe caminho direcionado da cidade `a` até a cidade `b`.

---

## 1. Propriedade estrutural central

A propriedade estrutural central do problema é a **conectividade forte**.

Um digrafo é fortemente conexo quando, para quaisquer dois vértices `u` e `v`, existem caminhos direcionados:

u → v

e

v → u

Portanto, o problema pode ser interpretado como:

> Verificar se o digrafo formado pelas cidades e rotas é fortemente conexo.

Equivalentemente, um digrafo é fortemente conexo quando todos os seus vértices pertencem a uma única componente fortemente conexa — SCC (*Strongly Connected Component*).

---

## 2. Critério utilizado

Uma forma geral de identificar componentes fortemente conexas é o algoritmo de Kosaraju-Sharir.

Entretanto, o problema Flight Routes Check não exige identificar todas as SCCs. É necessário apenas verificar se o grafo inteiro é fortemente conexo e, caso não seja, apresentar um par de cidades que demonstre a falha de alcançabilidade.

Por isso, será utilizada uma estratégia mais direta baseada em duas buscas em profundidade.

Escolhe-se uma cidade de referência `s`.

### Primeira DFS — grafo original

Executa-se uma DFS a partir de `s` no grafo original `G`.

Se existir algum vértice `v` não visitado, então:

s não alcança v

e uma resposta válida é:

NO
s v

### Segunda DFS — grafo reverso

Se todos os vértices forem alcançados na primeira DFS, constrói-se o grafo reverso `Gᴿ`, no qual cada aresta:

u → v

é substituída por:

v → u

Executa-se então outra DFS a partir de `s` em `Gᴿ`.

Se algum vértice `v` não for visitado em `Gᴿ`, isso significa que não existe caminho:

s → v em Gᴿ

o que equivale a dizer que, no grafo original:

v → s não existe

Portanto, uma resposta válida é:

NO
v s

Caso todos os vértices sejam alcançados nas duas buscas, o grafo é fortemente conexo e a resposta é:

YES

---

## 3. Justificativa do critério

Após a primeira DFS, caso todos os vértices tenham sido visitados, sabemos que:

s → v

para todo vértice `v`.

Após a segunda DFS no grafo reverso, caso todos os vértices também sejam visitados, sabemos que:

s → v em Gᴿ

para todo `v`.

Como as arestas de `Gᴿ` possuem sentido contrário às de `G`, isso equivale a:

v → s em G

para todo `v`.

Assim, para quaisquer dois vértices `a` e `b`, existe o caminho:

a → s → b

Logo, qualquer vértice alcança qualquer outro vértice, garantindo que o digrafo é fortemente conexo.

---

## 4. Implementações de referência da algs4

As implementações Python disponibilizadas pelo professor foram utilizadas como referência para definir a estratégia.

### `digraph.py`

Responsável pela representação de grafos direcionados através de lista de adjacência.

Será a principal referência para adaptar a representação atual do projeto.

Adaptações previstas:

- representar as rotas como arestas direcionadas;
- inserir uma aresta apenas no sentido `v → w`;
- disponibilizar a construção do grafo reverso através da operação `reverse()`.

A classe `Graph` utilizada anteriormente no projeto representa grafos não direcionados, adicionando cada aresta nos dois sentidos. Por isso, será necessária sua adaptação para um `Digraph`.

---

### `directed_dfs.py`

Implementa DFS para determinar alcançabilidade em um digrafo.

Será a principal referência para as duas buscas previstas na solução.

A estrutura central utilizada será:

- vetor `marked`;
- DFS recursiva;
- teste de alcançabilidade a partir de uma origem.

A implementação do projeto já possui uma DFS baseada na mesma lógica, porém aplicada a grafos não direcionados.

Para o Flight Routes Check, não é necessário recuperar os caminhos através de `edge_to` ou `path_to`. O vetor `marked` é suficiente para identificar vértices não alcançados.

---

### `depth_first_order.py`

Implementa pré-ordem, pós-ordem e pós-ordem reversa de uma DFS.

É utilizada pelo algoritmo de Kosaraju-Sharir.

Será mantida como referência conceitual para o estudo das componentes fortemente conexas, mas não é necessária na estratégia final das duas DFS.

---

### `kosaraju_scc.py`

Implementa o algoritmo de Kosaraju-Sharir para identificar todas as componentes fortemente conexas de um digrafo.

O algoritmo foi estudado para compreender a estrutura do problema e a relação entre SCCs e conectividade forte.

Entretanto, não será necessário implementá-lo integralmente, pois o Flight Routes Check exige apenas verificar se existe uma única componente fortemente conexa e fornecer um par de vértices quando isso não ocorre.

---

## 5. Instância pequena

Considere o seguinte digrafo com cinco cidades:

Arestas:

1 → 2  
2 → 1  
2 → 3  
3 → 4  
4 → 5  
5 → 4

Representação:

1 → 2 → 3 → 4 ⇄ 5
↑   |
└───┘

As componentes fortemente conexas podem ser observadas como:

{1, 2}

{3}

{4, 5}

Portanto, o grafo não é fortemente conexo.

---

## 6. Rastreamento manual da estratégia

Será utilizada a cidade:

s = 1

### 6.1 Primeira DFS em G

Estado inicial:

marked = [F, F, F, F, F]

A busca ocorre na seguinte sequência:

1 → 2 → 3 → 4 → 5

Estados:

Visita 1:

marked = [T, F, F, F, F]

Visita 2:

marked = [T, T, F, F, F]

Visita 3:

marked = [T, T, T, F, F]

Visita 4:

marked = [T, T, T, T, F]

Visita 5:

marked = [T, T, T, T, T]

Ao final da primeira DFS:

marked = [T, T, T, T, T]

Todos os vértices são alcançáveis a partir de `1`.

Entretanto, isso ainda não garante conectividade forte, pois é necessário verificar se todos também conseguem alcançar `1`.

---

## 7. Construção do grafo reverso

As arestas são invertidas:

Original:

1 → 2  
2 → 1  
2 → 3  
3 → 4  
4 → 5  
5 → 4

Reverso:

2 → 1  
1 → 2  
3 → 2  
4 → 3  
5 → 4  
4 → 5

Listas de adjacência do grafo reverso:

1: [2]  
2: [1]  
3: [2]  
4: [3, 5]  
5: [4]

---

## 8. Segunda DFS em Gᴿ

O vetor `marked` é reinicializado:

marked = [F, F, F, F, F]

A DFS começa novamente em `1`.

Visita 1:

marked = [T, F, F, F, F]

De `1`, é possível alcançar `2`.

Visita 2:

marked = [T, T, F, F, F]

A partir de `2`, apenas `1` é alcançável, mas ele já foi visitado.

Resultado final:

marked = [T, T, F, F, F]

O vértice `3`, por exemplo, não foi alcançado no grafo reverso.

Logo:

1 não alcança 3 em Gᴿ

Isso equivale a:

3 não alcança 1 em G

Portanto, uma resposta válida é:

NO
3 1

---

## 9. Decisões do algoritmo

A estratégia pode ser resumida da seguinte forma:

1. Escolher uma origem `s`.
2. Executar DFS em `G`.
3. Se existir `v` não visitado:
   - retornar `NO`;
   - informar `s v`.
4. Caso contrário, construir `Gᴿ`.
5. Reinicializar as estruturas de visita.
6. Executar DFS em `Gᴿ` a partir de `s`.
7. Se existir `v` não visitado:
   - retornar `NO`;
   - informar `v s`.
8. Caso todos os vértices sejam visitados nas duas buscas:
   - retornar `YES`.

---

## 10. Complexidade de tempo

O grafo é representado utilizando listas de adjacência.

Uma DFS visita cada vértice no máximo uma vez e percorre as arestas presentes nas listas de adjacência.

Portanto:

DFS = O(V + E)

São realizadas duas DFS:

O(V + E) + O(V + E)

A construção do grafo reverso também percorre vértices e arestas:

O(V + E)

Logo:

O(V + E) + O(V + E) + O(V + E)

Ignorando fatores constantes, a complexidade total permanece:

O(V + E)

---

## 11. Complexidade de memória

É importante separar a memória utilizada para representar o grafo da memória auxiliar do algoritmo.

### Representação do grafo

O grafo original utiliza lista de adjacência:

O(V + E)

O grafo reverso também utiliza lista de adjacência:

O(V + E)

Portanto, a representação continua assintoticamente:

O(V + E)

mesmo mantendo `G` e `Gᴿ` simultaneamente.

### Memória auxiliar

O vetor:

marked

possui uma posição para cada vértice:

O(V)

A DFS recursiva também pode utilizar uma pilha de chamadas de tamanho:

O(V)

no pior caso.

As demais variáveis possuem custo constante.

Portanto, a memória auxiliar é:

O(V)

Assim:

Representação do grafo: O(V + E)

Memória auxiliar: O(V)

---

## 12. Estratégia final

A estratégia escolhida para o Flight Routes Check será baseada em:

- representação por lista de adjacência;
- digrafo e grafo reverso;
- DFS para teste de alcançabilidade;
- duas buscas a partir de uma mesma origem.

O algoritmo de Kosaraju-Sharir foi utilizado como referência para compreender componentes fortemente conexas, porém a solução adotada é mais direta porque o problema exige apenas determinar se todo o grafo forma uma única SCC.

Complexidade final:

Tempo: O(V + E)

Representação: O(V + E)

Memória auxiliar: O(V)