def lst_vertices(entrada):
    vertices = [e.strip() for e in entrada.split(',')]
    return vertices if len(vertices) == len(set(vertices)) else 0


def lst_arestas(entrada, vertices, valorado):
    arestas = [[x.strip() for x in e.split(',')] for e in entrada.split(';')]
    for e in arestas:
        if valorado == 's':
            if len(e) is not 3:
                break
        else:
            if len(e) is not 2:
                break

        existe_v = False
        for v0 in e[:-1]:
            for v1 in vertices:
                if v0 == v1:
                    existe_v = True
                    break
        if not existe_v:
            break
    else:
        return arestas
    return 0


def rep_lista_arestas(arestas, valorado):
    print('lista de arestas')
    print('v1'.rjust(3) + 'v2'.rjust(3), end='')
    if valorado == 's':
        print('x'.rjust(3))
    else:
        print()
    print('-----------')
    for e in arestas:
        for i in e:
            print(i.rjust(3), end='')
        print()


def rep_lista_adjacencia(arestas, vertices, orientado, valorado):
    print('lista de adjacência')
    for v in vertices:
        print(v+'-> ', end='')
        if orientado == 's':
            for e in arestas:
                if v == e[0]:
                    if valorado == 's':
                        print(e[1]+','+e[2]+'-> ', end='')
                    else:
                        print(e[1] + '-> ', end='')
        else:
            for e in arestas:
                if v == e[0]:
                    if valorado == 's':
                        print(e[1]+','+e[2]+'-> ', end='')
                    else:
                        print(e[1] + '-> ', end='')
                elif v == e[1]:
                    if valorado == 's':
                        print(e[0] + ',' + e[2] + '-> ', end='')
                    else:
                        print(e[0] + '-> ', end='')
        print('!#')


def rep_matriz_adjacencia(vertices, arestas, orientado):
    print('matriz de adjacência')
    print(''.rjust(3), end='')
    for v in vertices:
        print(v.rjust(3), end='')
    print()

    for v0 in vertices:
        print(v0.rjust(3), end='')
        for v1 in vertices:
            adjacente = '0'
            for e in arestas:
                if orientado == 's':
                    if e[0] == v0 and e[1] == v1:
                        adjacente = '1'
                else:
                    if (e[0] == v0 and e[1] == v1) or (e[0] == v1 and e[1] == v0):
                        adjacente = '1'
            print(adjacente.rjust(3), end='')
        print()


def rep_matriz_incidencia(vertices, arestas, orientado):
    print('matriz de incidência')
    print(''.rjust(3), end='')
    for i in range(1, len(arestas)+1):
        print('e{}'.format(i).rjust(3), end='')
    print()

    for v in vertices:
        print(v.rjust(3), end='')
        for e in arestas:
            if orientado == 's':
                if v == e[0]:
                    print('1'.rjust(3), end='')
                elif v == e[1]:
                    print('-1'.rjust(3), end='')
                else:
                    print('0'.rjust(3), end='')
            else:
                if v == e[0] == e[1]:
                    print('2'.rjust(3), end='')
                elif v == e[0] or v == e[1]:
                    print('1'.rjust(3), end='')
                else:
                    print('0'.rjust(3), end='')
        print()


if __name__ == '__main__':
    orientado = ''
    while orientado not in ('s', 'n'):
        orientado = input('Grafo orientado (s/n): ').strip()[0].lower()
    valorado = ''
    while valorado not in ('s', 'n'):
        valorado = input('Grafo valorado (s/n): ').strip()[0].lower()
    vertices = 0
    while not vertices:
        vertices = lst_vertices(input('Vertices (a,b,c,...):'))
    arestas = 0
    # print(vertices)
    while not arestas:
        if valorado == 's':
            arestas = lst_arestas(input('Arestas (a,b,1;a,c,2;b,c,3;...)'), vertices, valorado)
        else:
            arestas = lst_arestas(input('Arestas (a,b;a,c;b,c;...)'), vertices, valorado)

    # print(arestas)

    rep_lista_arestas(arestas, valorado)
    print()
    rep_lista_adjacencia(arestas, vertices, orientado, valorado)
    print()
    rep_matriz_adjacencia(vertices, arestas, orientado)
    print()
    rep_matriz_incidencia(vertices, arestas, orientado)
