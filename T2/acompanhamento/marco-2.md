# Marco 2 — Componentes Conexas

## 1. Caso particular

Foi construído um caso particular com grafo simples, não dirigido, com:

- V = 6
- E = 5

Conjunto de vértices:

V = {0, 1, 2, 3, 4, 5}

Conjunto de arestas:

E = {
(0,1),
(1,2),
(2,0),
(3,4),
(4,5)
}

Representação do grafo:

      0
     / \
    1---2

    3---4---5

O grafo possui duas componentes conexas:

C0 = {0,1,2}

C1 = {3,4,5}

---

## 2. Listas de adjacência

A representação por listas de adjacência é:

0: [1, 2]

1: [0, 2]

2: [0, 1]

3: [4]

4: [3, 5]

5: [4]

Como o grafo é não dirigido, cada aresta aparece nas listas de adjacência dos dois vértices envolvidos.

---

## 3. Excentricidade, raio, diâmetro e centro

A distância entre dois vértices é definida como o comprimento do caminho mais curto entre eles.

A excentricidade de um vértice é a maior distância desse vértice até os demais vértices da mesma componente.

### Componente C0 = {0,1,2}

Distâncias:

d(0,1) = 1

d(0,2) = 1

d(1,2) = 1

Excentricidades:

exc(0) = 1

exc(1) = 1

exc(2) = 1

Logo:

raio(C0) = 1

diâmetro(C0) = 1

vértices centrais = {0,1,2}

centro(C0) = {0,1,2}

### Componente C1 = {3,4,5}

Distâncias:

d(3,4) = 1

d(4,5) = 1

d(3,5) = 2

Excentricidades:

exc(3) = 2

exc(4) = 1

exc(5) = 2

Logo:

raio(C1) = 1

diâmetro(C1) = 2

vértice central = 4

centro(C1) = {4}

---

## 4. Rastreamento manual do algoritmo de componentes conexas

O algoritmo utiliza DFS recursiva.

Estruturas iniciais:

marked = [False, False, False, False, False, False]

id = [-1, -1, -1, -1, -1, -1]

count = 0

### Primeira DFS

O primeiro vértice não visitado é 0.

DFS(0)

0 é marcado e recebe id 0.

A DFS visita 1.

1 é marcado e recebe id 0.

A DFS visita 2.

2 é marcado e recebe id 0.

Após o término:

marked = [True, True, True, False, False, False]

id = [0, 0, 0, -1, -1, -1]

Primeira componente:

C0 = {0,1,2}

count = 1

### Segunda DFS

Os vértices 1 e 2 já estão marcados.

O próximo vértice não visitado é 3.

DFS(3)

3 é marcado e recebe id 1.

A DFS visita 4.

4 é marcado e recebe id 1.

A DFS visita 5.

5 é marcado e recebe id 1.

Ao final:

marked = [True, True, True, True, True, True]

id = [0, 0, 0, 1, 1, 1]

Segunda componente:

C1 = {3,4,5}

count = 2

---

## 5. Lógica de identificação das componentes

O algoritmo percorre todos os vértices do grafo.

Quando encontra um vértice ainda não visitado, inicia uma nova DFS.

Todos os vértices alcançados por essa DFS recebem o mesmo identificador de componente.

Quando a DFS termina, o contador de componentes é incrementado.

No exemplo:

id = [0, 0, 0, 1, 1, 1]

Logo:

- 0, 1 e 2 pertencem à componente 0;
- 3, 4 e 5 pertencem à componente 1.

---

## 6. Complexidade

### Tempo

A complexidade do algoritmo é:

Θ(V + E)

Isso ocorre porque cada vértice é visitado e as listas de adjacência são percorridas durante a DFS.

### Espaço

O espaço extra utilizado é:

Θ(V)

As principais estruturas são:

- vetor marked;
- vetor id;
- pilha de chamadas da DFS.

---

## 7. Consultas de conectividade

Após a identificação das componentes, basta comparar os identificadores de dois vértices.

Exemplo:

id[0] = 0

id[2] = 0

Logo, 0 e 2 estão conectados.

Outro exemplo:

id[0] = 0

id[4] = 1

Logo, 0 e 4 não estão conectados.

A consulta:

connected(v, w)

possui custo:

Θ(1)

pois basta comparar:

id[v] == id[w]