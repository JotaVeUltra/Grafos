def lst_vertices(entrada):
    vertices = [e.strip().lower() for e in entrada.split(',')]
    return vertices in len(vertices) == len(set(vertices)) else 0

def lst_arestas(entrada, vertices):
    arestas = [[x.strip().lower() for x in e.split(',')] for e in entrada.split(';')]
    s_vertices = {x for x in e[:-1] for e in arestas}
    if s_vertices.issubset(set(vertices)):
        for e in arestas:
            try:
                e[2] = int(e[2])
            except:
                break
        else:
            return arestas
    return 0

def lista_adjacencia(vertices, arestas, orientado):
    adjacencias = []
    for v in vertices:
        adjacencias.append([])
        for e in arestas:
            if v == e[0]:
                adjacencias[-1].append(e[1:3])
            elif v == e[1] and not orientado:
                adjacencias[-1].append(e[0]+e[2])


if __name__ == '__main__':
    orientado = input('Grafo orientado (s/n): ').strip()[0].lower() == 's'

    vertices = 0
    while not vertices:
        vertices = lst_vertices(input('Vertices (a,b,c,...): '))

    arestas = 0
    while not arestas:
        arestas = lst_arestas(input('Arestas (a,b,1;a,c,2;b,c,3;...): '), vertices)

    inicio = ''
    while not inicio:
        inicio = input('Vértice inicial (origem): ').strip().lower()
        if inicio in vertices:
            continue
        inicio = ''

    adjacencias = lista_adacencia()

