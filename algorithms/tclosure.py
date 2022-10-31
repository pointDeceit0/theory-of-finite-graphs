import networkx as nx
import matplotlib.pyplot as plt


def print_graph(graph: list[tuple[str, str, int]]) -> None:
    gr = nx.DiGraph()

    gr.add_edges_from(graph)

    nx.draw_circular(gr,
                node_color='green',
                node_size=1000,
                with_labels=True
    )

    plt.show()


def trans_closure(g: list[tuple[str, str]]) -> list[tuple[str, str]]:
    ''' find all unique vertexes in graph '''
    vertexes = set()
    for v1, v2 in g:
        vertexes.add(v1)
        vertexes.add(v2)

    # sort to build a matrix by order of vertexes
    vertexes = sorted(vertexes, key=lambda x: int(x[1:]))

    n = len(vertexes) 
    # forming a dict with idx of each vertex. 
    # It'll be needed to finding connections between vertexes
    vs = {v: i for i, v in enumerate(vertexes)} 
    matrix = [[0] * n for _ in range(n)] 

    # forming primary connections D(0)
    for v1, v2 in g:
        matrix[vs[v1]][vs[v2]] = 1

    # finding all transtitive closures
    for i in range(n):
        for r in range(n):
            for c in range(n):
                matrix[r][c] = max(matrix[r][c], matrix[r][i] * matrix[i][c])
    
    # building a graph using a matrix
    gr = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                gr.append((vertexes[i], vertexes[j]))


    ''' print matrix '''
    print('\t', end='')
    for v in vertexes:
        print(v, end='\t')
    print()
    for r in range(n):
        print(vertexes[r], end='\t')

        for c in range(n):
            print(matrix[r][c], end='\t')
        print()
    
    return gr


        
def main():
    gr = [
        ('v1', 'v2'),
        ('v2', 'v3'),
        ('v3', 'v4'),
        ('v1', 'v13'),
        ('v13', 'v3'),
        ('v13', 'v5'),
        ('v5', 'v6'),
        ('v6', 'v13'),
        ('v6', 'v7'),
        ('v7', 'v12'),
        ('v1', 'v12'),
        ('v12', 'v11'),
        ('v12', 'v8'),
        ('v8', 'v11'),
        ('v8', 'v9'),
        ('v9', 'v10')
    ]

    print_graph(gr)
    gr = trans_closure(gr)
    print_graph(gr)


if __name__ == "__main__":
    main()