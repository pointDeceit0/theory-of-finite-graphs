from algorithms.max_tree import subgraph
from print_graph import print_graph


def main():
    a = open('algorithms/gr.txt', 'r')

    n = int(a.readline().strip())
    gr = []
    while (s := a.readline().strip()) != 'q':
        s = s.split()
        s[2] = float(s[2])
        gr.append(s)
    
    '''n = int(input('Введите число вершин: '))

    gr = []
    while (inp := input("Введите ребро графа в формате [V1 V2 вес] через пробелы или введите 'q', если больше нет ребер: ")) != 'q':
        inp = inp.strip().split()
        inp[2] = float(inp[2])
        gr.append(inp)'''

    print_graph(gr)
    gr, weight = subgraph(gr, n)
    print_graph(gr)
    print(weight)


if __name__ == "__main__":
    main()