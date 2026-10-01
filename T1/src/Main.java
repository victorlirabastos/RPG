import java.util.ArrayList;
import java.util.List;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Scanner;

public class Main { // Classe principal do programa.

    public static void main(String[] args) { // Método inicial executado pelo Java.

        // Cria o Scanner para ler os dados fornecidos pelo Kattis.
        Scanner scanner = new Scanner(System.in);


        // Lê a quantidade total de filmes.
        int N = scanner.nextInt();

        // Lê a quantidade de filmes pertencentes à Horror List.
        int H = scanner.nextInt();

        // Lê a quantidade de relações de similaridade.
        int L = scanner.nextInt();


        // Cria o grafo contendo N vértices.
        Graph graph = new Graph(N);


        // Cria uma lista para armazenar os filmes da Horror List.
        List<Integer> horrorList = new ArrayList<>();


        // Lê os H filmes pertencentes à Horror List.
        for (int i = 0; i < H; i++) {

            // Lê o identificador de um filme horrível.
            int horrorMovie = scanner.nextInt();

            // Adiciona esse filme ao conjunto de origens da BFS.
            horrorList.add(horrorMovie);
        }


        // Lê todas as relações de similaridade.
        for (int i = 0; i < L; i++) {

            // Lê o primeiro filme da relação.
            int v = scanner.nextInt();

            // Lê o segundo filme da relação.
            int w = scanner.nextInt();

            // Adiciona uma aresta não direcionada entre os dois filmes.
            graph.addEdge(v, w);
        }


        // Executa a BFS utilizando todos os filmes da Horror List como origens.
        BreadthFirstPaths bfs = new BreadthFirstPaths(graph, horrorList);


        // Inicialmente considera o filme 0 como candidato à resposta.
        int result = 0;


        // Percorre todos os filmes em ordem crescente de identificador.
        for (int v = 1; v < N; v++) {

            // Verifica se o Horror Index de v é maior que o do candidato atual.
            if (bfs.distTo(v) > bfs.distTo(result)) {

                // Caso seja maior, v passa a ser o novo candidato.
                result = v;
            }
        }


        // Imprime o identificador do filme com maior Horror Index.
        System.out.println(result);


        // Fecha o Scanner.
        scanner.close();
    }
}

class Graph { // Classe que representa um grafo não direcionado.

    // Número de vértices do grafo.
    private final int V;

    // Número de arestas do grafo.
    private int E;

    // Vetor de listas de adjacência.
    private List<Integer>[] adj;


    // Construtor do grafo.
    @SuppressWarnings("unchecked")
    public Graph(int V) {

        // Armazena a quantidade de vértices.
        this.V = V;

        // Inicialmente o grafo não possui arestas.
        this.E = 0;

        // Cria um vetor com uma lista para cada vértice.
        adj = (List<Integer>[]) new List[V];

        // Percorre todos os vértices.
        for (int v = 0; v < V; v++) {

            // Cria uma lista de adjacência vazia para cada vértice.
            adj[v] = new ArrayList<>();
        }
    }


    // Retorna o número de vértices.
    public int V() {

        // Retorna V.
        return V;
    }


    // Retorna o número de arestas.
    public int E() {

        // Retorna E.
        return E;
    }


    // Adiciona uma aresta não direcionada entre v e w.
    public void addEdge(int v, int w) {

        // Adiciona w à lista de vizinhos de v.
        adj[v].add(w);

        // Adiciona v à lista de vizinhos de w.
        adj[w].add(v);

        // Incrementa a quantidade de arestas.
        E++;
    }


    // Retorna todos os vizinhos de um vértice.
    public Iterable<Integer> adj(int v) {

        // Retorna a lista de adjacência de v.
        return adj[v];
    }
}

class BreadthFirstPaths { // Classe responsável pela Busca em Largura.

    // Representa uma distância infinita para vértices que não foram alcançados.
    private static final int INFINITY = Integer.MAX_VALUE;

    // marked[v] indica se o vértice v já foi visitado pela BFS.
    private boolean[] marked;

    // edgeTo[v] guarda o predecessor de v no menor caminho encontrado.
    private int[] edgeTo;

    // distTo[v] guarda a menor distância entre v e alguma origem.
    private int[] distTo;


    // Construtor utilizado quando existe apenas uma origem.
    public BreadthFirstPaths(Graph graph, int s) {

        // Cria o vetor de vértices visitados com tamanho igual ao número de vértices.
        marked = new boolean[graph.V()];

        // Cria o vetor de predecessores.
        edgeTo = new int[graph.V()];

        // Cria o vetor de distâncias.
        distTo = new int[graph.V()];

        // Verifica se o vértice de origem é válido.
        validateVertex(s);

        // Executa a BFS a partir de uma única origem.
        bfs(graph, s);
    }


    // Construtor utilizado quando existem várias origens.
    // Este será utilizado no problema Horror List.
    public BreadthFirstPaths(Graph graph, Iterable<Integer> sources) {

        // Cria o vetor que marca os vértices visitados.
        marked = new boolean[graph.V()];

        // Cria o vetor de predecessores.
        edgeTo = new int[graph.V()];

        // Cria o vetor de distâncias.
        distTo = new int[graph.V()];

        // Inicializa todas as distâncias como infinito.
        for (int v = 0; v < graph.V(); v++) {

            // Indica que inicialmente nenhum vértice possui distância conhecida.
            distTo[v] = INFINITY;
        }

        // Verifica se o conjunto de origens é válido.
        validateVertices(sources);

        // Executa a BFS utilizando múltiplas origens.
        bfs(graph, sources);
    }


    // BFS tradicional com apenas uma origem.
    private void bfs(Graph graph, int s) {

        // Cria uma fila FIFO para controlar a ordem de visitação.
        Queue<Integer> queue = new ArrayDeque<>();

        // Inicializa todas as distâncias como infinito.
        for (int v = 0; v < graph.V(); v++) {

            // Nenhum vértice possui distância conhecida inicialmente.
            distTo[v] = INFINITY;
        }

        // A distância da origem até ela mesma é zero.
        distTo[s] = 0;

        // Marca a origem como visitada.
        marked[s] = true;

        // Coloca a origem na fila.
        queue.add(s);

        // Continua enquanto ainda existirem vértices a serem processados.
        while (!queue.isEmpty()) {

            // Remove da fila o vértice que entrou primeiro.
            int v = queue.remove();

            // Percorre todos os vizinhos do vértice v.
            for (int w : graph.adj(v)) {

                // Verifica se o vizinho ainda não foi visitado.
                if (!marked[w]) {

                    // Registra v como predecessor de w.
                    edgeTo[w] = v;

                    // A distância de w é a distância de v mais uma aresta.
                    distTo[w] = distTo[v] + 1;

                    // Marca w como visitado.
                    marked[w] = true;

                    // Coloca w na fila para que seus vizinhos sejam analisados depois.
                    queue.add(w);
                }
            }
        }
    }


    // BFS com múltiplas origens.
    // Esta é a versão utilizada pelo Horror List.
    private void bfs(Graph graph, Iterable<Integer> sources) {

        // Cria a fila FIFO utilizada pela BFS.
        Queue<Integer> queue = new ArrayDeque<>();

        // Percorre todos os filmes que pertencem à Horror List.
        for (int s : sources) {

            // Marca cada filme da Horror List como já visitado.
            marked[s] = true;

            // Todo filme pertencente à Horror List possui Horror Index zero.
            distTo[s] = 0;

            // Coloca todas as origens inicialmente na mesma fila.
            queue.add(s);
        }

        // Continua enquanto houver vértices aguardando processamento.
        while (!queue.isEmpty()) {

            // Remove o vértice mais antigo da fila.
            int v = queue.remove();

            // Percorre todos os vizinhos de v.
            for (int w : graph.adj(v)) {

                // Só processa o vizinho se ele ainda não tiver sido visitado.
                if (!marked[w]) {

                    // Guarda v como predecessor de w.
                    edgeTo[w] = v;

                    // Calcula a menor distância de w até alguma origem.
                    distTo[w] = distTo[v] + 1;

                    // Marca w como visitado.
                    marked[w] = true;

                    // Adiciona w à fila.
                    queue.add(w);
                }
            }
        }
    }


    // Informa se existe caminho entre alguma origem e o vértice v.
    public boolean hasPathTo(int v) {

        // Verifica se o vértice recebido é válido.
        validateVertex(v);

        // Retorna true se o vértice tiver sido visitado.
        return marked[v];
    }


    // Retorna a menor distância até alguma das origens.
    public int distTo(int v) {

        // Verifica se o vértice é válido.
        validateVertex(v);

        // Retorna a distância armazenada pela BFS.
        return distTo[v];
    }


    // Retorna o predecessor de um vértice.
    // Este método é útil para demonstrarmos edgeTo no Marco 4.
    public int edgeTo(int v) {

        // Verifica se o vértice é válido.
        validateVertex(v);

        // Retorna o predecessor armazenado.
        return edgeTo[v];
    }


    // Verifica se um vértice pertence ao intervalo válido do grafo.
    private void validateVertex(int v) {

        // Obtém o número total de vértices.
        int V = marked.length;

        // Verifica se v está fora do intervalo de 0 até V - 1.
        if (v < 0 || v >= V) {

            // Interrompe o programa caso o vértice seja inválido.
            throw new IllegalArgumentException(
                    "vertex " + v + " is not between 0 and " + (V - 1)
            );
        }
    }


    // Valida o conjunto de vértices utilizados como origem.
    private void validateVertices(Iterable<Integer> vertices) {

        // Verifica se o conjunto recebido é nulo.
        if (vertices == null) {

            // Não é possível executar a BFS sem conjunto de origens.
            throw new IllegalArgumentException("argument is null");
        }

        // Conta quantas origens existem.
        int vertexCount = 0;

        // Percorre todas as origens.
        for (Integer v : vertices) {

            // Incrementa a quantidade de origens.
            vertexCount++;

            // Verifica se alguma origem é nula.
            if (v == null) {

                // Interrompe caso exista um valor inválido.
                throw new IllegalArgumentException("vertex is null");
            }

            // Verifica se o identificador da origem pertence ao grafo.
            validateVertex(v);
        }

        // Verifica se nenhuma origem foi informada.
        if (vertexCount == 0) {

            // Interrompe porque a BFS precisa de pelo menos uma origem.
            throw new IllegalArgumentException("zero vertices");
        }
    }
}
