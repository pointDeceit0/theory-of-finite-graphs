class DisconnectedGraph(Exception):
    pass


def subgraph(graph: list[list[str, str, int]], n: int, reverse=False) -> tuple[list[tuple[str, str, float]], int]:
    "Prim's algorithm"
    '''
    m - number of edges
    Time complexity  --- O(m)

    reverse: False - standart min subgraph
             True - max subgraph
    '''

    e = sorted(graph, reverse=reverse, key=lambda x: x[2])
    print(e)
    
    unselected = e[1::].copy()
    ans, bouquet = [e[0]], {e[0][0], e[0][1]}
    while len(unselected) or len(bouquet) != n:
        for _, v in enumerate(unselected):
            if v[0] in bouquet and v[1] in bouquet:
                unselected.remove(v)
                break
            elif v[0] in bouquet or v[1] in bouquet:
                ans.append(v)
                bouquet.add(v[0])
                bouquet.add(v[1])
                unselected.remove(v)
                break
        else:
            ans.append(unselected[0])
            bouquet.add(unselected[0][0])
            bouquet.add(unselected[0][1])
            unselected.append(unselected[0])
    
    weight = sum([v[2] for _, v in enumerate(ans)])
    
    return (ans, weight)


def main():
    a = open('algorithms/gr.txt', 'r')

    n = int(a.readline().strip())
    gr = []
    while (s := a.readline().strip()) != 'q':
        s = s.split()
        s[2] = float(s[2])
        gr.append(s)

    print(subgraph(gr, n))
    
    '''n = int(input('Input number of vertexes: '))

    
    gr = []
    while (inp := input("Input edge of graph in format [vertex_1 vertex2 weight] by space OR input q if there's no edges : ")) != 'q':
        inp = inp.strip().split()
        inp[2] = float(inp[2])
        gr.append(inp)

    print(subgraph(gr, n))
'''


if __name__ == "__main__":
    main()