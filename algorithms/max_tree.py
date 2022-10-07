def max_subgraph(graph: list[list[str, str, int]]) -> list[tuple[str, str, float]]:
    "Prim's algorithm"

    e = sorted(graph, reverse=True, key=lambda x: x[2])
    
    ans, bouquet = [], set()
    for _, v in enumerate(e):
        # check for a cycle
        if not (v[0] in bouquet and v[1] in bouquet): 
            ans.append(tuple(v))
            bouquet.add(v[0])
            bouquet.add(v[1])

    return ans

def main():
    n = int(input('Input number of vertexes: '))

    
    gr = []
    for _ in range(n):
        inp = input("Input edge of graph in format [vertex_1 vertex2 weight] by space: ").strip().split()
        inp[2] = float(inp[2])
        gr.append(inp)

    print(max_subgraph(gr))



if __name__ == "__main__":
    main()