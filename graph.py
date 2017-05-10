import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(graph, label):
    # create directed networkx graph
    G = nx.Graph()

    # add edges
    G.add_edges_from(graph)
    # graph_pos = nx.shell_layout(G)
    # graph_pos = nx.spectral_layout(G)
    graph_pos = nx.spring_layout(G)
    # graph_pos = nx.random_layout(G)

    # draw nodes, edges and labels
    nx.draw_networkx_nodes(G, graph_pos, node_size=1000, node_color='blue', alpha=0.3)

    # we can now added edge thickness and edge color
    nx.draw_networkx_edges(G, graph_pos, width=2, alpha=0.3, edge_color='green')
    nx.draw_networkx_labels(G, graph_pos, font_size=12, font_family='sans-serif')

    nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=label)

    plt.show()


label = {
    ('Hambalang', 'Andi'): 1,
    ('Andi', 'Hambalang'): 3,
    ('Hambalang', 'Wafid Muharram'): 2,
    ('Andi', 'Andi Malarangeng'): 1,
    ('Andi Malarangeng', 'Wafid Muharram'): 1,
    ('Wafid Muharram', 'Andi'): 1
}

graph = [
    ('Hambalang', 'Andi'), ('Andi', 'Hambalang'), ('Hambalang', 'Wafid Muharram'), ('Andi', 'Andi Malarangeng'),
    ('Andi Malarangeng', 'Wafid Muharram'), ('Wafid Muharram', 'Andi')
]

draw_graph(graph, label)
