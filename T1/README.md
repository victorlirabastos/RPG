# T1 — Horror List

**Disciplina:** Resolução de Problemas com Grafos, UNIFOR.  
**Professor:** Prof. Me. Ricardo Carubbi.  
**Integrantes:** Victor Lira - 1920409; Vinícius Feitosa - 2110882.  
**Linguagem:** Java.  
**Problema:** [Kattis Horror List](https://open.kattis.com/problems/horror).

## Problema, modelagem e algoritmo

Temos N filmes, uma lista S de H filmes considerados ruins e L relações de similaridade. Cada filme é um vértice e cada similaridade uma aresta não direcionada, sem peso. O grafo pode ser desconexo.

Para cada filme, calculamos a **menor distância até algum filme da lista**: `HI(v) = min dist(v,s), s ∈ S`. Depois escolhemos o **maior desses índices**. Em empate, o menor ID. Um filme sem caminho até S tem índice infinito. Assim, primeiro minimizamos a distância de cada candidato até a lista e depois maximizamos o índice entre candidatos.

A solução usa **BFS multi-origem**: todos os filmes de S entram inicialmente na mesma fila FIFO, com distância zero. A descoberta por níveis garante as menores distâncias. A DFS estudada no Marco 3 encontra caminhos e alcançabilidade, mas não garante caminhos mínimos em um grafo não ponderado geral.

## Estrutura da entrega

A entrega está em `T1/` dentro do repositório `victorlirabastos/RPG`:

```text
T1/
├── README.md
├── acompanhamento/
│   ├── marco-1.md
│   ├── marco-2.md
│   ├── marco-3.md
│   ├── marco-4.md
│   └── revisao-feedback.md
├── src/
│   └── Main.java
├── evidencias/
│   ├── accepted.png
│   └── accepted-20400623.png
├── apresentacao/
│   └── apresentacao.pdf
├── dados/
│   └── casos-de-teste.txt
└── testes/
    ├── verificar.py
    └── resultado.txt
```

`Main.java` é autossuficiente. As classes necessárias `Bag`, `Graph` e `Queue` já estão dentro dele. O executor em `testes/` valida a solução e não é enviado ao Kattis. O PPTX editável e o material de estudo também ficam fora deste pacote.

## Compilação e execução

Requer JDK 8 ou superior. Para obter a entrega e entrar na pasta correta:

```sh
git clone https://github.com/victorlirabastos/RPG.git
cd RPG/T1
```

Se já está na raiz do repositório RPG, execute `cd T1`. Todos os comandos abaixo partem de `RPG/T1`:

```sh
mkdir -p build
javac -encoding UTF-8 -d build src/Main.java
java -cp build Main
```

Depois do último comando, cole **somente a entrada de um caso** de [casos-de-teste.txt](dados/casos-de-teste.txt). Não cole rótulos como ENTRADA/SAIDA. O programa imprime o ID e termina. Execute novamente para outro caso. Alternativamente, salve essa entrada em um arquivo temporário e use `java -cp build Main < entrada.txt`.

Exemplo de entrada:

```text
7 2 6
0 5
0 1
1 2
2 3
3 4
4 5
3 6
```

Saída: `6`. A pasta `build` e qualquer entrada temporária são geradas apenas para execução local e não integram a entrega. No Kattis, enviar somente `src/Main.java`, classe principal `Main`.

## Representação e implementação de referência

A representação é `Bag<Integer>[]`: uma lista encadeada de vizinhos por vértice. A relação `(a,b)` insere b na lista de a e a na lista de b. A `Bag` insere no início, então a iteração ocorre na ordem inversa de inserção.

A referência é **Robert Sedgewick e Kevin Wayne, Algorithms, 4ª edição**, na versão disponibilizada pelo professor: [Graph](https://github.com/carubbi/RPG/blob/a3df01a7931344129dc5d7e16f6525ecc24a664b/algs4-java/algs4/Graph.java), [Bag](https://github.com/carubbi/RPG/blob/a3df01a7931344129dc5d7e16f6525ecc24a664b/algs4-java/algs4/Bag.java), [Queue](https://github.com/carubbi/RPG/blob/a3df01a7931344129dc5d7e16f6525ecc24a664b/algs4-java/algs4/Queue.java), [BreadthFirstPaths](https://github.com/carubbi/RPG/blob/a3df01a7931344129dc5d7e16f6525ecc24a664b/algs4-java/algs4/BreadthFirstPaths.java) e [DepthFirstPaths](https://github.com/carubbi/RPG/blob/a3df01a7931344129dc5d7e16f6525ecc24a664b/algs4-java/algs4/DepthFirstPaths.java).

A conferência comparou construção do grafo, inserção de arestas, operações de bolsa/fila e o núcleo da BFS. O código segue essa metodologia; é uma adaptação para o problema, não uma cópia integral da biblioteca algs4.

| O que foi mantido ou adaptado | Motivo |
|---|---|
| Graph com Bag por vértice e inserção da aresta nos dois sentidos | Representar similaridade bidirecional |
| Queue encadeada e marcação antes de enfileirar | Explorar em ordem de distância sem visitas repetidas |
| BFS multi-origem já oferecida na referência | Calcular o mínimo até toda a Horror List em uma única busca |
| Leitura de N, H, L, das origens e dos pares com BufferedReader/StringTokenizer | Atender ao formato específico do Kattis |
| Classes reunidas em Main e BFS integrada ao método principal | Enviar um arquivo sem dependência da biblioteca algs4 |
| Omissão de edgeTo e reconstrução de caminhos na solução final | O enunciado pede apenas o ID escolhido |
| Integer.MAX_VALUE para não alcançados | Representar índice infinito |
| Varredura crescente de IDs, atualizando apenas com `>` | Escolher o maior índice e preservar o menor ID em empates |

O ponto relevante da solução é usar todas as origens juntas, evitando uma busca independente para cada filme ruim. Isso **não é uma invenção de algoritmo**: a referência já oferece o recurso. A adaptação é sua aplicação ao Horror Index, seguida das regras de infinito e desempate.

## Complexidade: de onde vem O(V+E)

Aqui V=N, E=L e H<V.

| Etapa | Tempo no pior caso | Motivo |
|---|---|---|
| Criar listas e ler as relações | O(V+E) | V listas e duas inserções por aresta |
| Inicializar distâncias e fontes | O(V+H) = O(V) | Vetores de V posições e H fontes |
| Executar BFS | O(V+E) | Cada vértice enfileirado no máximo uma vez e cada aresta examinada no máximo duas vezes |
| Escolher a resposta | O(V) | Uma varredura dos IDs |

A BFS é a etapa central e uma das mais custosas assintoticamente; **a construção tem o mesmo limite O(V+E)**. Não houve medição isolada que permita afirmar qual consumiu mais tempo real. Somando as etapas, o total permanece **O(V+E)**. Os laços da BFS não multiplicam V por E, porque não percorremos todas as arestas novamente para cada vértice, apenas sua lista de vizinhos.

**Espaço do grafo:** O(V+E), com V listas e 2E entradas. **Espaço adicional da busca:** O(V), pelos vetores e pela fila. **Espaço total:** O(V+E). O algoritmo trabalha com inteiros limitados pelo enunciado.

## Marcos, testes e evidências

- [Marco 1](acompanhamento/marco-1.md): enunciado, restrições, modelagem e hipótese.
- [Marco 2](acompanhamento/marco-2.md): representação real da solução e medidas estruturais.
- [Marco 3](acompanhamento/marco-3.md): execução manual da DFS, tempos, predecessores e aplicabilidade.
- [Marco 4](acompanhamento/marco-4.md): BFS, escolha, integração, correção e validação.

[Casos de teste](dados/casos-de-teste.txt) contém 10 entradas completas: 2 exemplos oficiais e 8 casos de estudo, incluindo a instância dos marcos. Também registra a construção e o resultado esperado de 3 casos de limite. Em 10/09/2026, a Main isolada passou nos 10 casos, nos 3 limites e em 100 grafos pequenos aleatórios (semente 20260908) comparados com Floyd–Warshall, totalizando 113 execuções. Esse registro histórico foi preservado. A revisão acrescenta um executor reproduzível e seu resultado atual, sem depender do executor antigo. Floyd–Warshall serviu apenas à verificação externa, não à solução submetida.

### Evidência avaliada pelo professor: submissão de Victor

![Accepted de Victor, submissão 20400623](evidencias/accepted-20400623.png)

A captura citada no feedback corresponde à submissão [20400623](https://open.kattis.com/submissions/20400623), na conta Victor Lira Bastos: **Horror List, Java, Accepted, 17/17, 0,26 s**. Foi copiada sem edição da evidência do repositório da dupla. Os imports visíveis (`ArrayList`, `ArrayDeque`, `Scanner`) diferem da Main atual. Portanto, ela comprova o Accepted dessa submissão, mas não comprova identidade com `src/Main.java`. O código integral dessa submissão não está disponível nas capturas.

### Evidência anterior preservada

![Accepted anterior, submissão 20374292](evidencias/accepted.png)

A captura anterior, na conta Vinícius Feitosa, registra a submissão [20374292](https://open.kattis.com/submissions/20374292): **Accepted, Java, 17/17**, com tempo de **0,11 s**. Os 17 testes são do avaliador Kattis, distintos dos testes locais. A captura não revela as entradas nem o código completo submetido. Não houve nova submissão nesta revisão.

### Reexecutar a validação

Com Python 3 e o JDK disponíveis, dentro de `RPG/T1`:

```sh
python3 testes/verificar.py
```

O executor compila a Main em uma pasta temporária, lê os dez casos diretamente do arquivo preservado, gera os três limites e os cem grafos com a semente documentada, e compara os aleatórios com Floyd–Warshall. Uma divergência termina com erro e mostra a entrada. Resultado desta revisão: [testes/resultado.txt](testes/resultado.txt).

## Apresentação

[Apresentação em PDF](apresentacao/apresentacao.pdf): oito slides no visual institucional: capa com logo UNIFOR, subcapa com identificação e matrículas, Introdução, Objetivo, Modelagem do problema como um grafo, Representação computacional, DFS x BFS e Validação. Todos os slides incluem referências no rodapé. Roteiro planejado para 4min50s, com margem até 5 minutos. [Template de referência](https://github.com/carubbi/RPG/blob/a3df01a7931344129dc5d7e16f6525ecc24a664b/mat-didatico/trabalhos/template/template_UNIFOR.pptx).

O PDF foi preservado como material anterior e sua referência à submissão 20374292 é histórica. Para a entrega corrigida, use a evidência 20400623 acima e a distinção entre versões. O [registro da revisão](acompanhamento/revisao-feedback.md) contém um roteiro técnico para ensaio.

## Uso de IA

Foi utilizado **ChatGPT e Codex, da OpenAI**, como apoio ao estudo, à organização e revisão dos documentos, à conferência de consistência, aos testes locais e à preparação da apresentação. O código final preexistente `Main.java` e a captura de Accepted foram preservados sem alteração. Cada integrante deve compreender, testar e justificar o material apresentado.

## Registro da consolidação

A consolidação anterior partiu do pacote de entrega existente. A Main permanece idêntica ao código preservado do commit [57d7a58](https://github.com/viniciusfeitosaa/T1-RPG/tree/57d7a58). A instância comum mantém a aresta `(3,6)`. A ordem manual da DFS foi normalizada para a ordem de iteração da Bag da solução final, evitando tabelas de duas representações diferentes. Referências a auxiliares retirados foram substituídas pelas explicações e tabelas contidas nos próprios marcos.


A revisão motivada pelo feedback está detalhada em [revisao-feedback.md](acompanhamento/revisao-feedback.md), com comparação dos repositórios, alterações, validação e pendências.
