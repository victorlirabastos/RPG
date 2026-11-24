# Marco 1 — Formulação

Recebemos uma tabela que informa a distância entre cada par de vilas. O mapa com as ligações diretas foi perdido. Como todas as vilas se alcançam com a menor quantidade possível de estradas, a rede original é uma árvore. A tarefa é recuperar exatamente as estradas dessa árvore.

| Elemento | Definição |
| --- | --- |
| Entrada | Um inteiro n e n linhas com n inteiros, formando a matriz D. |
| Restrições | 2 ≤ n ≤ 2500, D[i][i] = 0 e 0 < D[i][j] < 10⁷ para i ≠ j, com D[i][j] = D[j][i]. |
| Vértices | Vilas numeradas de 1 a n. |
| Arestas candidatas | Um par não ordenado {i,j} para cada i ≠ j, sem laços. |
| Pesos | w({i,j}) = D[i][j], a distância na rede original. |
| Grafo modelado | Completo, não direcionado e ponderado, com n(n−1)/2 arestas. |
| Saída | n−1 linhas u v com o conjunto de estradas originais. A ordem das linhas e a orientação dos pares são livres. |

## Família e justificativa

O modelo é de **árvore geradora mínima (AGM)**. A entrada fornece distâncias prontas, que se tornam pesos no grafo candidato. O resultado conecta todas as vilas com uma árvore cuja soma desses pesos é mínima. Em A8 (p. 2 e seção 1.4), esse é o objetivo da AGM. Em A9 (p. 2 e 26), uma árvore de caminhos mínimos preserva a distância desde uma origem. Aqui a origem é livre e queremos recuperar as ligações da rede inteira.

Ao remover uma estrada original e da árvore, surgem duas componentes. Todos os caminhos entre as componentes passam por e. Para o par dos extremos de e, o peso é exatamente o comprimento de e. Qualquer outro par que cruza o mesmo corte percorre pelo menos mais uma estrada positiva, então tem peso estritamente maior. Pela propriedade do corte, e pertence a toda AGM. Isso vale para as n−1 estradas originais, portanto a AGM é única mesmo quando há pesos iguais em cortes diferentes.

A promessa de origem em uma árvore torna desnecessário definir saída de impossibilidade. Uma matriz simétrica e positiva arbitrária pode não corresponder a uma árvore e fica fora do problema.

## Fontes e verificação

- [Kattis Lost Map](https://open.kattis.com/problems/lostmap) e [NCNA 2017, pp. 23–24](https://brycesandlund.com/NCNA_2017.pdf#page=23). Conferidos em 24/11/2026. Os limites de entrada, o formato da saída e as duas amostras coincidem.
- Ricardo Carubbi, UNIFOR. A8 — Árvore Geradora Mínima e A9 — Caminhos de Custo Mínimo, Unidade 3.
