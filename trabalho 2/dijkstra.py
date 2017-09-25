from queue import PriorityQueue

def tratar_vertices(entrada):
    vertices = [e.strip().lower() for e in entrada.split(',') if len(e.strip().lower()) >= 1]
    return vertices if len(vertices) == len(set(vertices)) else None


def tratar_arestas(entrada, vertices):
    arestas = [[x.strip().lower() for x in e.split(',')] for e in entrada.split(';')]
    s_vertices = {x for e in arestas for x in e[:-1]}
    if s_vertices.issubset(set(vertices)):
        for e in arestas:
            try:
                e[2] = int(e[2])
            except (IndexError, ValueError):
                break
        else:
            return arestas
    return None


def lista_adjacencia(vertices, arestas, orientado):
    adjacencias = []
    for v in vertices:
        adjacencias.append([])
        for e in arestas:
            if v == e[0]:
                adjacencias[-1].append(e[1:3])
            elif v == e[1] and not orientado:
                adjacencias[-1].append([e[0], e[2]])
    return adjacencias


def dijkstra(origem, vertices, arestas, adjacencias):
    dist = []
    caminho = []
    visitou = []
    for i in range(len(vertices)):
        dist.append(float('inf'))
        caminho.append(None)
        visitou.append(False)
    dist[vertices.index(origem)] = 0
    pq = PriorityQueue()
    pq.put((0, origem))
    while not pq.empty():
        u = pq.get()[1]
        visitou[vertices.index(u)] = True
        for v, dist_v in adjacencias[vertices.index(u)]:
            alt = dist[vertices.index(u)] + dist_v
            if alt < dist[vertices.index(v)]:
                dist[vertices.index(v)] = alt
                caminho[vertices.index(v)] = u
            if not visitou[vertices.index(v)]:
                pq.put((dist[vertices.index(v)], v))
    return dist, caminho


if __name__ == '__main__':
    orientado = input('Grafo orientado (s/n): ').strip()[0].lower() == 's'

    vertices = None
    while not vertices:
        vertices = tratar_vertices(input('Vertices (a,b,c,...): '))

    arestas = None
    while not arestas:
        arestas = tratar_arestas(input('Arestas (a,b,1;a,c,2;b,c,3;...): '), vertices)

    while True:
        origem = input('Vértice inicial (origem): ').strip().lower()
        if origem in vertices:
            break

    adjacencias = lista_adjacencia(vertices, arestas, orientado)

    print('Vértice'.rjust(10)+'Distância'.rjust(10)+'Caminho'.rjust(10))
    for v, distancia, caminho in zip(vertices, *dijkstra(origem, vertices,arestas,adjacencias)):
        print(str(v).rjust(10)+str(distancia).rjust(10)+str(caminho).rjust(10))
