import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd


def get_labels(csv_file):
    df = pd.read_csv(csv_file, index_col=0)
    return list(df.index)


def make_label_dict(labels):
    return {i: label for i, label in enumerate(labels)}


def show_graph_with_labels(adjacency_matrix, labels):
    rows, cols = np.where(adjacency_matrix == 1)
    edges = list(zip(rows.tolist(), cols.tolist()))

    gr = nx.DiGraph()  # Using DiGraph since the adjacency matrix seems to imply direction
    gr.add_edges_from(edges)

    plt.figure(figsize=(10, 8))  # Increase figure size for better resolution
    pos = nx.spring_layout(gr, k=0.5)  # Adjust layout spread to reduce overlap
    nx.draw(gr, pos, with_labels=True, labels=labels, node_size=1000, node_color='lightblue', edge_color='gray',
            font_size=12)
    plt.show()


# Load adjacency matrix from CSV
adjacency_df = pd.read_csv('grainWorldAdjacency.csv', index_col=0)
adjacency_matrix = adjacency_df.values

# Generate labels
graph_labels = make_label_dict(get_labels('grainWorldAdjacency.csv'))

# Show graph
show_graph_with_labels(adjacency_matrix, graph_labels)
