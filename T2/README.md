# T2 — Flight Routes Check

**Linguagem:** Python
**Problema:** [CSES Flight Routes Check](https://cses.fi/problemset/task/1682)

## Visão geral

A solução verifica se um dígrafo é fortemente conexo. Ela executa uma busca em profundidade a partir da cidade 1 no grafo original e outra no grafo reverso. Se uma das buscas não alcançar todas as cidades, retorna um par que demonstra a falta de conectividade.

## Navegação

- [Marcos 1–4](acompanhamento/): modelagem, propriedade estrutural, estratégia e conclusão.
- [Código-fonte](src/): módulos Python e solução consolidada para submissão.
- [Casos de teste](dados/casos-de-teste.txt): entradas pequenas com saídas esperadas.
- [Evidência da submissão](evidencias/accepted.png): captura do resultado no CSES.
- [Apresentação](apresentacao/README.md): situação do PDF da apresentação.

## Código-fonte

- [main.py](src/main.py): programa principal, que importa os módulos locais.
- [digraph.py](src/digraph.py): representação do dígrafo e construção do reverso.
- [directed_dfs.py](src/directed_dfs.py): busca iterativa e consulta de alcançabilidade.
- [submission.py](src/submission.py): versão consolidada em um único arquivo.
- [graph.py](src/graph.py), [depth_first_paths.py](src/depth_first_paths.py) e [breadth_first_paths.py](src/breadth_first_paths.py): implementações de referência mantidas no projeto.

## Executar

Requer Python 3. A partir desta pasta, execute:

```sh
python3 src/main.py
```

Informe a entrada do problema pelo terminal. Para testar, use individualmente as entradas de [casos-de-teste.txt](dados/casos-de-teste.txt) e compare com as saídas esperadas. Para submeter ao CSES, use o conteúdo de `src/submission.py`.

## Acompanhamento

Os registros dos quatro marcos estão publicados em [acompanhamento/](acompanhamento/). A apresentação em PDF ainda não consta no workspace; a situação está registrada em [apresentacao/](apresentacao/README.md).
