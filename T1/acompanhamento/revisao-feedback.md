# Revisão final do T1 a partir do feedback

## Origem e escopo

Esta revisão continua a auditoria registrada a partir de `FeedBack T1.pdf`, páginas 4–9, emitido em 30/09/2026. O relatório pessoal não integra a entrega pública. O estado anterior do RPG está preservado no commit [6fbd655](https://github.com/victorlirabastos/RPG/tree/6fbd6553d7ee1b7b75302d67aec739bc238503fa). Somente o repositório `victorlirabastos/RPG` foi alterado; o repositório da dupla permaneceu intocado.

## Código integral obtido e divergência resolvida

Victor forneceu o `Main.java` integral identificado como o código da submissão Kattis **20400623**. O anexo da conversa foi recuperado e copiado byte a byte para `T1/src/Main.java`, sem reconstrução a partir de imports e sem mudanças no código. O caminho `/mnt/data/Main.java` pertencia à conversa de origem; nesta revisão foi usado o mesmo anexo recuperado pelo aplicativo.

SHA-256 do arquivo fornecido e da cópia entregue:

```text
5da8ee9517cb2f1e67d6181f449dc0f7ee75c0db63bd83d30d86893317809be4
```

A implementação real usa Scanner, List/ArrayList, Queue/ArrayDeque e BreadthFirstPaths com marked/edgeTo/distTo. README, Marcos 2–4 e apresentação foram alinhados a ela. A divergência entre o código anterior e a evidência foi resolvida pela adoção integral do arquivo fornecido. A identificação da submissão vem do arquivo informado por Victor e da captura; não houve novo download autenticado do Kattis nem nova submissão.

A única evidência final é [accepted.png](../evidencias/accepted.png), a imagem original de Victor, sem edição: **20400623, Horror List, Java, Accepted, 17/17, 0,26 s**. A evidência de outro integrante foi retirada da entrega final e permanece apenas no histórico Git.

## Auditoria dos requisitos

| Requisito do feedback | Correção e evidência atual |
|---|---|
| Estrutura e execução | Pasta src e comandos a partir de RPG/T1 consistentes; Main autossuficiente. |
| Marco 2 | ArrayList em ordem de inserção, leitura Scanner, seis inserções, adjacências, graus, soma 12=2E, validação e custo amortizado. |
| Marco 3 | DFS manual 0,1,2,3,4,5,6, árvore, pais, 14 eventos, cores, pilha e intervalos recalculados; limites da DFS explicitados. |
| Marco 4 | Fila multi-origem, níveis, distâncias, marked e edgeTo reais, raízes sem pai e zeros padrão diferenciados, comparação DFS/BFS, correção, infinito e desempate. |
| Referência e adaptações | Sedgewick/Wayne e material do professor citados; coleções Java padrão, entrada, integração e seleção justificadas. Multi-origem já existe na referência. |
| Código e Accepted | Main idêntica ao anexo fornecido, SHA-256 registrado, somente evidência 20400623. |
| Testes reproduzíveis | 113 casos reexecutados no novo código, mais verificação das estruturas e vetores; relatório atualizado. |
| Complexidade | O(V+E) no total, listas e fila com operações amortizadas, O(V) adicional da BFS. Sem atribuir custo empírico a uma etapa não medida. |
| Apresentação | Oito slides institucionais, adjacências corrigidas, implementação e evidência de Victor, roteiro de 4min50s. |
| Uso de IA | README declara apoio de ChatGPT/Codex e preservação integral do arquivo fornecido. |

## Validação reproduzível

Dentro de `RPG/T1`, executar `python3 testes/verificar.py`, com Python 3 e JDK 8 ou superior. O executor compila em pasta temporária, testa 10 casos documentados, 3 limites e 100 grafos diferenciais com semente 20260908 e oráculo Floyd–Warshall. Também confere a ordem efetiva de Graph.adj, E, as distâncias, marcas e predecessores de BreadthFirstPaths, inclusive fontes e não alcançados. O [resultado](../testes/resultado.txt) identifica o código por SHA-256.

A simulação DFS é didática, externa à Main. Descoberta/término: 0=(1,14), 1=(2,13), 2=(3,12), 3=(4,11), 4=(5,8), 5=(6,7), 6=(9,10). A BFS mantém HI=[0,1,2,2,1,0,3] e resposta 6.

## Roteiro de até cinco minutos

| Slides | Conteúdo | Tempo |
|---|---|---|
| 1–2 | Capa e identificação | 15 s |
| 3–4 | Problema, mínimo até S e máximo entre candidatos | 45 s |
| 5 | Modelo, origens e aresta 3–6 | 40 s |
| 6 | Scanner, ArrayList, duas inserções e O(V+E) | 55 s |
| 7 | DFS, fila multi-origem, marked/edgeTo/distTo e níveis | 80 s |
| 8 | 113 testes, Accepted, infinito e desempate | 55 s |

Total planejado: **4min50s**, com 10 s de margem. Não é uma medição de ensaio realizado. Treinar as respostas: por que marcar antes de enfileirar? Por que O(V+E) e não O(VE)? O que significa edgeTo=0 numa raiz? Por que `>` preserva o menor ID?

## Pendências manuais

- Ensaiar a apresentação e demonstrar compreensão dos Marcos 2–4 dentro de cinco minutos.
- Encaminhar o link final ao professor e solicitar a análise conforme as regras da disciplina.
- O registro escrito não comprova apresentação anterior dos Marcos 2 e 4 nem altera automaticamente a avaliação.
