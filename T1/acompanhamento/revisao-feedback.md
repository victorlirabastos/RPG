# Revisão do T1 a partir do feedback

## Fontes e preservação

Fonte principal: `FeedBack T1.pdf`, relatório fornecido por Victor, páginas 4–9 (emitido em 30/09/2026). O PDF contém informações acadêmicas pessoais e não integra esta entrega pública; os requisitos pertinentes estão mapeados abaixo.

Bases comparadas:

- [RPG de Victor, ff9976492dc2a6493d898558ceb4553c0e59ac38](https://github.com/victorlirabastos/RPG/tree/ff9976492dc2a6493d898558ceb4553c0e59ac38).
- [T1-RPG da dupla, f67e97543781506aecc4dc126b6ce189decac049](https://github.com/viniciusfeitosaa/T1-RPG/tree/f67e97543781506aecc4dc126b6ce189decac049), consultado somente como referência.

A revisão altera apenas o RPG de Victor. O commit-base preserva integralmente o estado anterior. Nenhum arquivo anterior foi excluído; Main.java, Marco 1, os casos de teste, a apresentação e accepted.png foram mantidos byte a byte. A revisão não atribui autoria individual com base apenas no conteúdo coincidente dos repositórios.

## Diagnóstico e plano executado

| Item | Comparação e correção |
|---|---|
| Representação | Na dupla, Marco 2 descreve ArrayList, mas a Main usa Bag/Graph. No RPG isso já estava alinhado; acrescentamos leitura vinculada ao código, seis passos de construção e validação. |
| DFS | O RPG já tinha árvore, tempos e predecessores na ordem real da Bag. Acrescentamos todos os estados branco/cinza/preto, pilha, retornos, pseudocódigo e conferência dos intervalos. |
| BFS | Na dupla, Marco 4 usa a ligação 2–6 e classes externas, divergindo da instância original e da Main. O RPG já preserva 3–6, pred[6]=3 e classes internas. Mantivemos e completamos a ligação com o código, desempates, infinito, testes e submissão. |
| Caminhos | A dupla contém `scr`; o RPG já contém `src`. O README do RPG ainda chamava a pasta de T1-RPG e dizia apenas “a partir da raiz”. Corrigimos para clone do RPG, `cd RPG/T1`, comandos e estrutura atuais. |
| Accepted | O feedback avalia 20400623, conta Victor, 0,26 s. O RPG tinha 20374292, conta Vinícius, 0,11 s. Preservamos a anterior e adicionamos a captura de Victor como accepted-20400623.png; README e Marco 4 distinguem as duas. |
| Reprodutibilidade | Os dez casos são idênticos nos dois repositórios. Preservamos o arquivo e acrescentamos executor dos 10 casos, 3 limites e 100 grafos diferenciais conforme a geração já documentada. |
| Referência e adaptações | Mantidas Graph/Bag/Queue e BFS multi-origem do algs4, com as justificativas de integração, infinito, omissão de caminhos e desempate. |

O feedback registra ausência de apresentação dos Marcos 2 e 4. Documentar agora atende à orientação de registro; não comprova apresentação passada nem altera automaticamente a avaliação.

## Identidade das implementações e das evidências

Nas duas bases, Main.java tem o mesmo objeto Git `1b1c7ff71497a0caff3f88c26189b3540e0d5bcc`: as estruturas Bag/Graph/Queue são internas e a leitura usa BufferedReader/StringTokenizer. A captura 20374292 mostra esses mesmos imports, mas não todo o código.

A captura 20400623 mostra ArrayList/List/ArrayDeque/Queue/Scanner. Ela foi copiada integralmente do arquivo `evidencias/Screenshot 2026-09-08 at 22.47.17.png` da base da dupla; o objeto Git é `ff448c0e21c9b3be15764583f61d148d0289f17a`. Nenhum número ou resultado da imagem foi editado. Essa evidência comprova a submissão citada pelo professor, sem demonstrar que seu código integral coincide com a Main preservada.

Não foi reconstruída uma implementação a partir de imports, nem copiada uma implementação alternativa sobre a Main. Caso a entrega deva conter exatamente o código da submissão 20400623, Victor precisará disponibilizar o arquivo integral pelo Kattis; então será necessário compará-lo, validar e ajustar a documentação correspondente.

## Validação reproduzível

Dentro de `RPG/T1`, executar:

```sh
python3 testes/verificar.py
```

Requisitos: Python 3 e JDK 8 ou superior. O executor não usa pacotes Python externos. A Main é compilada com alvo Java 8 em pasta temporária, removida automaticamente. O resultado desta revisão está em [resultado.txt](../testes/resultado.txt). São 113 casos: 10 entradas preservadas, 3 limites determinísticos e 100 grafos com semente 20260908 comparados com Floyd–Warshall. Isso não é uma nova submissão ao Kattis e não substitui a prova de correção do Marco 4.

A conferência dos rastreamentos verificou as adjacências, predecessores, tempos da DFS e níveis da BFS na instância original com aresta 3–6. A solução Java não registra esses rastreamentos; eles são instrumentos didáticos separados.

## Roteiro técnico para os integrantes

1. **Problema e modelo (45 s):** diferenciar a menor distância de cada filme até S da escolha do maior HI; mostrar 3–6 e as origens 0 e 5.
2. **Representação (50 s):** abrir Graph.addEdge e Bag.add; explicar duas entradas por relação, ordem inversa de inserção e soma dos graus 12.
3. **DFS (60 s):** mostrar a pilha chegando a 6, o retorno a 3 e a descoberta de 4; explicar d[6]=5, f[6]=6 e por que profundidade não é HI.
4. **BFS e adaptação (80 s):** começar com fila [0,5], retirar 4 e descobrir 3; mostrar que a Main omite edgeTo e por que basta distTo para selecionar o ID.
5. **Validação e conclusão (55 s):** demonstrar empate e infinito, justificar O(V+E), executar os testes e distinguir as duas submissões.

Total previsto: 4min50s. É um roteiro para ensaio, não comprovação de ensaio realizado.

Perguntas para praticar: por que marcar antes de enfileirar? Por que o laço aninhado não custa O(VE)? O que acontece com um isolado? Por que `>` e não `>=`? Qual adaptação é do grupo e qual já existe no algs4? As respostas estão nos Marcos 2–4 e devem ser demonstradas na Main.

## Itens que dependem de ação humana

- Ensaiar e explicar os marcos, especialmente os procedimentos de DFS e BFS solicitados pelo professor.
- Encaminhar ao professor o link do T1 corrigido e solicitar a análise conforme as regras da disciplina.
- Se for exigida identidade exata entre a Main entregue e a submissão 20400623, fornecer o código integral dessa submissão para comparação. A captura sozinha não resolve essa identificação.
- O PDF da apresentação foi preservado; sua referência à 20374292 permanece como registro anterior. Na reapresentação, explicitar a distinção documentada ou atualizar os slides a partir do arquivo editável.
