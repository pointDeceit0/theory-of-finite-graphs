class DisconnectedGraph(Exception):
    pass


def max_subgraph(graph: list[list[str, str, int]], n: int) -> list[tuple[str, str, float]]:
    "Prim's algorithm"

    e = sorted(graph, reverse=True, key=lambda x: x[2])
    
    ans, bouquet = [], set()
    for i, v in enumerate(e):
        # check for a cycle
        if not (v[0] in bouquet and v[1] in bouquet): 
            for j in range(i + 1, len(e)):
                if v[0] in e[j] or v[1] in e[j]:
                    ans.append(tuple(v))
                    break
            else:
                raise DisconnectedGraph

            bouquet.add(v[0])
            bouquet.add(v[1])

    return ans

def main():
    n = int(input('Input number of vertexes: '))

    
    gr = []
    while (inp := input("Input edge of graph in format [vertex_1 vertex2 weight] by space OR input q if there's no edges : ")) != 'q':
        inp = inp.strip().split()
        inp[2] = float(inp[2])
        gr.append(inp)

    print(max_subgraph(gr))



if __name__ == "__main__":
    main()