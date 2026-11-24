# T3 — Lost Map

## Problema

O [Kattis Lost Map](https://open.kattis.com/problems/lostmap) pede para recuperar as estradas originais entre vilas a partir da matriz de distâncias entre todos os pares. A saída tem n − 1 pares de vilas numeradas de 1 a n.

## Integrantes e linguagem

- **Integrantes e matrículas:** a confirmar.
- **Linguagem:** Python 3, com a biblioteca padrão.

## Execução

A partir de `T3/`, execute o comando abaixo com um arquivo no formato de entrada do Kattis. Os blocos de [casos-de-teste.txt](dados/casos-de-teste.txt) incluem entradas e saídas que podem ser copiadas separadamente.

```sh
python3 src/main.py < entrada.txt
```

## Modelagem, algoritmo e correção esperada

Cada vila é um vértice. Cada par de vilas define uma aresta candidata, sem direção, cujo peso é a distância da matriz. A rede original conecta todas as vilas com n − 1 estradas e é uma árvore.

O Prim matricial guarda, para cada vila fora da árvore parcial, o peso e o pai da ligação mais leve até ela. A menor chave identifica uma aresta segura pelo corte entre a árvore parcial e as demais vilas. Para ver por que a AGM recupera as estradas originais, remova uma estrada da árvore original. Ela é a ligação estritamente mais leve entre as duas componentes resultantes, porque qualquer outro par que cruza o corte percorre essa estrada e ao menos um trecho positivo adicional. Logo, toda AGM contém cada estrada original.

## Referência e adaptação

A referência da disciplina é a classe Eager Prim em `algs4-py/algs4/prim_mst.py`, revisão `a3df01a7931344129dc5d7e16f6525ecc24a664b` de `carubbi/RPG`. A adaptação conserva os estados de `marked`, `distTo` e `edgeTo` em vetores de marcação, chaves e pais. Substitui a fila indexada por uma varredura das chaves e o grafo explícito pela matriz lida linha a linha. A escolha aproveita a densidade do grafo completo e evita materializar ou ordenar suas arestas. A entrada e a saída seguem o formato do Kattis, com os pares convertidos para numeração de 1 a n.

## Complexidade e casos especiais

O tempo total é Θ(n²), incluindo leitura, seleção e atualização. A matriz de inteiros ocupa Θ(n²) de espaço total e os vetores usam Θ(n) de espaço auxiliar. Em empate, a seleção segue a ordem dos IDs. Uma instância com duas vilas produz um único par. A entrada do problema sempre provém de uma árvore com estradas positivas, portanto não há caso de impossibilidade previsto.

## Testes e evidência do Accepted

- [Casos de teste](dados/casos-de-teste.txt)
- [Validação local e estado da submissão](evidencias/README.md)
- [Acompanhamento dos marcos](acompanhamento/marcos.md)

## Uso de IA

O Codex auxiliou na documentação, na adaptação do Prim matricial e na validação local.
