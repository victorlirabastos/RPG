#!/usr/bin/env python3
"""Validação externa; somente src/Main.java é submetido ao Kattis."""
from pathlib import Path
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
    print(subprocess.run(['javac', '-version'], text=True, capture_output=True, check=True).stdout.strip())
    with tempfile.TemporaryDirectory(prefix='horror-testes-') as build:
        # -source/-target funcionam também no JDK 8; a Main usa apenas APIs Java 8.
        subprocess.run(['javac', '-encoding', 'UTF-8', '-source', '8', '-target', '8',
                        '-Xlint:-options', '-d', build, str(ROOT / 'src/Main.java')], check=True)
        for nome, dados, esperado in casos:
            run = subprocess.run(['java', '-cp', build, 'Main'], input=dados,
                                 text=True, capture_output=True, timeout=10)
            if run.returncode != 0 or run.stdout.strip() != esperado:
                raise RuntimeError(f'{nome}: esperado={esperado}, recebido={run.stdout!r}\n{run.stderr}\nENTRADA\n{dados}')
            print(f'OK {nome}: {esperado}')
    print('APROVADO: 10 documentados + 3 limites + 100 diferenciais = 113 casos.')
    print('Semente: 20260908. Oráculo: Floyd–Warshall. Main.java preservada.')


if __name__ == '__main__':
    main()
