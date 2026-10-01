#!/usr/bin/env python3
"""Validação externa; somente src/Main.java é submetido ao Kattis."""
from pathlib import Path
import hashlib
import random
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def entrada(n, fontes, arestas):
    return f'{n} {len(fontes)} {len(arestas)}\n' + ' '.join(map(str, fontes)) + '\n' + ''.join(f'{a} {b}\n' for a, b in arestas)


def oracle(n, fontes, arestas):
    # Floyd–Warshall é independente da BFS da Main.
    inf = float('inf')
    d = [[0 if u == v else inf for v in range(n)] for u in range(n)]
    for u, v in arestas:
        d[u][v] = d[v][u] = 1
    for k in range(n):
        for u in range(n):
            for v in range(n):
                d[u][v] = min(d[u][v], d[u][k] + d[k][v])
    hi = [min(d[v][s] for s in fontes) for v in range(n)]
    return str(max(range(n), key=lambda v: (hi[v], -v)))


ESTRUTURAS = r"""
import java.util.*;
class ConferirEstruturas {
    static void check(boolean ok, String message) {
        if (!ok) throw new AssertionError(message);
    }
    public static void main(String[] args) {
        Graph g = new Graph(7);
        int[][] edges = {{0,1},{1,2},{2,3},{3,4},{4,5},{3,6}};
        for (int[] e : edges) g.addEdge(e[0],e[1]);
        String[] expected = {"[1]","[0, 2]","[1, 3]","[2, 4, 6]","[3, 5]","[4]","[3]"};
        check(g.V()==7 && g.E()==6, "V/E");
        for (int v=0;v<7;v++) {
            List<Integer> actual = new ArrayList<>();
            for (int w:g.adj(v)) actual.add(w);
            check(actual.toString().equals(expected[v]), "adj "+v);
        }
        BreadthFirstPaths bfs = new BreadthFirstPaths(g, Arrays.asList(0,5));
        int[] dist = {0,1,2,2,1,0,3}, pred = {0,0,1,4,5,0,3};
        for (int v=0;v<7;v++) {
            check(bfs.hasPathTo(v), "marked "+v);
            check(bfs.distTo(v)==dist[v], "distTo "+v);
            check(bfs.edgeTo(v)==pred[v], "edgeTo "+v);
        }
        Graph disconnected = new Graph(5);
        disconnected.addEdge(0,1); disconnected.addEdge(1,2);
        BreadthFirstPaths other = new BreadthFirstPaths(disconnected, Arrays.asList(0));
        for (int v=3;v<5;v++) {
            check(!other.hasPathTo(v) && other.distTo(v)==Integer.MAX_VALUE && other.edgeTo(v)==0,
                  "inalcancavel "+v);
        }
        System.out.println("OK estruturas: adjacências, V/E, marked, distTo, edgeTo e não alcançados.");
    }
}
"""


def main():
    texto = (ROOT / 'dados/casos-de-teste.txt').read_text(encoding='utf-8')
    casos = re.findall(r'^CASO ([^\n]+)\nENTRADA\n(.*?)\nSAIDA\n(\d+)\nFIM', texto, re.M | re.S)
    if len(casos) != 10:
        raise RuntimeError(f'Esperados 10 casos documentados; encontrados {len(casos)}')
    casos = [(nome, dados + '\n', saida) for nome, dados, saida in casos]
    casos += [('limite-L1', entrada(1000, [0], [(i, i+1) for i in range(999)]), '999'),
              ('limite-L2', entrada(1000, list(range(999)), []), '999')]
    arestas = [(0, v) for v in range(1, 1000)]
    for u in range(1, 1000):
        for v in range(u+1, 1000):
            if len(arestas) == 10000:
                break
            arestas.append((u, v))
        if len(arestas) == 10000:
            break
    casos.append(('limite-L3', entrada(1000, [0], arestas), '1'))
    rng = random.Random(20260908)
    for i in range(100):
        n = rng.randint(2, 15)
        h = rng.randint(1, n-1)
        fontes = rng.sample(range(n), h)
        arestas = [(u,v) for u in range(n) for v in range(u+1,n) if rng.random() < 0.22]
        casos.append((f'aleatorio-{i+1:03d}', entrada(n, fontes, arestas), oracle(n, fontes, arestas)))
    print('Código: src/Main.java; referência: arquivo fornecido da submissão 20400623.')
    print('SHA-256: ' + hashlib.sha256((ROOT / 'src/Main.java').read_bytes()).hexdigest())
    print(subprocess.run(['javac', '-version'], text=True, capture_output=True, check=True).stdout.strip())
    with tempfile.TemporaryDirectory(prefix='horror-testes-') as build:
        # -source/-target funcionam também no JDK 8; a Main usa apenas APIs Java 8.
        subprocess.run(['javac', '-encoding', 'UTF-8', '-source', '8', '-target', '8',
                        '-Xlint:-options', '-d', build, str(ROOT / 'src/Main.java')], check=True)
        # Verifica os dados usados nos Marcos 2 e 4 diretamente nas classes entregues.
        probe = Path(build) / 'ConferirEstruturas.java'
        probe.write_text(ESTRUTURAS, encoding='utf-8')
        subprocess.run(['javac', '-encoding', 'UTF-8', '-cp', build, '-d', build, str(probe)], check=True)
        subprocess.run(['java', '-cp', build, 'ConferirEstruturas'], check=True)
        for nome, dados, esperado in casos:
            run = subprocess.run(['java', '-cp', build, 'Main'], input=dados,
                                 text=True, capture_output=True, timeout=10)
            if run.returncode != 0 or run.stdout.strip() != esperado:
                raise RuntimeError(f'{nome}: esperado={esperado}, recebido={run.stdout!r}\n{run.stderr}\nENTRADA\n{dados}')
            print(f'OK {nome}: {esperado}')
    print('APROVADO: 10 documentados + 3 limites + 100 diferenciais = 113 casos.')
    print('Semente: 20260908. Oráculo: Floyd–Warshall. Main.java integral fornecida; sem alterações no código.')


if __name__ == '__main__':
    main()
