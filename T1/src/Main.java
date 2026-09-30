import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Iterator;
import java.util.NoSuchElementException;

public class Main {
    private static final int INFINITY = Integer.MAX_VALUE;

    // Estrutura de dados Bag (Bolsa) de Robert Sedgewick representada como lista simplesmente encadeada
    private static class Bag<Item> implements Iterable<Item> {
        private Node<Item> first;    // início da bolsa
        private int n;               // número de elementos

        private static class Node<Item> {
            private Item item;
            private Node<Item> next;
        }

        public Bag() {
            first = null;
            n = 0;
        }

        public boolean isEmpty() {
            return first == null;
        }

        public int size() {
            return n;
        }

        public void add(Item item) {
            Node<Item> oldfirst = first;
            first = new Node<Item>();
            first.item = item;
            first.next = oldfirst;
            n++;
        }

        public Iterator<Item> iterator() {
            return new LinkedIterator(first);
        }

        private class LinkedIterator implements Iterator<Item> {
            private Node<Item> current;

            public LinkedIterator(Node<Item> first) {
                current = first;
            }

            public boolean hasNext() {
                return current != null;
            }

            public Item next() {
                if (!hasNext()) throw new NoSuchElementException();
                Item item = current.item;
                current = current.next;
                return item;
            }
        }
    }

    // Estrutura de Grafo Não-Direcionado de Robert Sedgewick por Lista de Adjacência (usando Bag)
    private static class Graph {
        private final int V;
        private int E;
        private Bag<Integer>[] adj;

        @SuppressWarnings("unchecked")
        public Graph(int V) {
            if (V < 0) throw new IllegalArgumentException("O número de vértices deve ser não-negativo");
            this.V = V;
            this.E = 0;
            adj = (Bag<Integer>[]) new Bag[V];
            for (int v = 0; v < V; v++) {
                adj[v] = new Bag<Integer>();
            }
        }

        public int V() {
            return V;
        }

        public int E() {
            return E;
        }

        public void addEdge(int v, int w) {
            validateVertex(v);
            validateVertex(w);
            E++;
            adj[v].add(w);
            adj[w].add(v);
        }

        public Iterable<Integer> adj(int v) {
            validateVertex(v);
            return adj[v];
        }

        private void validateVertex(int v) {
            if (v < 0 || v >= V)
                throw new IllegalArgumentException("Vértice " + v + " inválido");
        }
    }

    // Estrutura de Fila FIFO de Robert Sedgewick representada como lista simplesmente encadeada
    private static class Queue<Item> implements Iterable<Item> {
        private Node<Item> first;    // início da fila
        private Node<Item> last;     // fim da fila
        private int n;               // número de elementos

        private static class Node<Item> {
            private Item item;
            private Node<Item> next;
        }

        public Queue() {
            first = null;
            last  = null;
            n = 0;
        }

        public boolean isEmpty() {
            return first == null;
        }

        public int size() {
            return n;
        }

        public void enqueue(Item item) {
            Node<Item> oldlast = last;
            last = new Node<Item>();
            last.item = item;
            last.next = null;
            if (isEmpty()) first = last;
            else           oldlast.next = last;
            n++;
        }

        public Item dequeue() {
            if (isEmpty()) throw new NoSuchElementException("Fila sob fluxo negativo (underflow)");
            Item item = first.item;
            first = first.next;
            n--;
            if (isEmpty()) last = null;
            return item;
        }

        public Iterator<Item> iterator() {
            return new LinkedIterator(first);
        }

        private class LinkedIterator implements Iterator<Item> {
            private Node<Item> current;

            public LinkedIterator(Node<Item> first) {
                current = first;
            }

            public boolean hasNext() {
                return current != null;
            }

            public Item next() {
                if (!hasNext()) throw new NoSuchElementException();
                Item item = current.item;
                current = current.next;
                return item;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        // Leitor rápido de entrada (E/S rápida para evitar TLE)
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = null;

        String line = reader.readLine();
        if (line == null) return;
        tokenizer = new StringTokenizer(line);

        int N = Integer.parseInt(tokenizer.nextToken());
        int H = Integer.parseInt(tokenizer.nextToken());
        int L = Integer.parseInt(tokenizer.nextToken());

        int[] horrorList = new int[H];
        line = reader.readLine();
        if (line != null) {
            tokenizer = new StringTokenizer(line);
            for (int i = 0; i < H; i++) {
                horrorList[i] = Integer.parseInt(tokenizer.nextToken());
            }
        }

        Graph G = new Graph(N);
        for (int i = 0; i < L; i++) {
            line = reader.readLine();
            if (line != null) {
                tokenizer = new StringTokenizer(line);
                int u = Integer.parseInt(tokenizer.nextToken());
                int v = Integer.parseInt(tokenizer.nextToken());
                G.addEdge(u, v);
            }
        }

        // BFS Multi-Fonte
        boolean[] marked = new boolean[N];
        int[] distTo = new int[N];
        for (int v = 0; v < N; v++) {
            distTo[v] = INFINITY;
        }

        Queue<Integer> q = new Queue<Integer>();
        for (int s : horrorList) {
            marked[s] = true;
            distTo[s] = 0;
            q.enqueue(s);
        }

        while (!q.isEmpty()) {
            int v = q.dequeue();
            for (int w : G.adj(v)) {
                if (!marked[w]) {
                    marked[w] = true;
                    distTo[w] = distTo[v] + 1;
                    q.enqueue(w);
                }
            }
        }

        // Integração e Lógica de Desempate Final (Menor ID em caso de empate de maior Horror Index)
        int bestMovie = -1;
        int maxHorrorIndex = -1;

        for (int v = 0; v < N; v++) {
            if (distTo[v] > maxHorrorIndex) {
                maxHorrorIndex = distTo[v];
                bestMovie = v;
            }
        }

        System.out.println(bestMovie);
    }
}