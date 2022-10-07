import networkx as nx
import matplotlib.pyplot as plt


def print_graph(graph: list[tuple[str, str, int]]) -> None:
    gr = nx.Graph()

    gr.add_weighted_edges_from(graph)

    nx.draw_circular(gr,
                node_color='red',
                node_size=1000,
                with_labels=True
    )

    plt.show()
