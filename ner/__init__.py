import nltk
import networkx as nx
import matplotlib.pyplot as plt


def remove_non_ascii(text):
    return ''.join(i for i in text if ord(i) < 128)


def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences


def extract_names(document):
    names = []
    sentences = ie_preprocess(document)
    for tagged_sentence in sentences:
        for chunk in nltk.ne_chunk(tagged_sentence):
            if type(chunk) == nltk.tree.Tree:
                if chunk.label() == 'PERSON':
                    names.append(' '.join([c[0] for c in chunk]))
    return names


def extract_organizations(document):
    organizations = []
    sentences = ie_preprocess(document)
    for tagged_sentence in sentences:
        for chunk in nltk.ne_chunk(tagged_sentence):
            if type(chunk) == nltk.tree.Tree:
                if chunk.label() == 'ORGANIZATION':
                    organizations.append(' '.join([c[0] for c in chunk]))
    return organizations


def draw_graph(graph, label):
    G = nx.Graph()
    G.add_edges_from(graph)
    graph_pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, graph_pos, node_size=1000, node_color='orange', alpha=0.3)
    nx.draw_networkx_edges(G, graph_pos, width=2, alpha=0.3, edge_color='black')
    nx.draw_networkx_labels(G, graph_pos, font_size=12, font_family='sans-serif')
    nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=label)
    plt.show()