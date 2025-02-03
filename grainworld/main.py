import networkx as nx
import numpy as np

# Example adjacency matrix (NumPy array)
adj_matrix = np.array([[0, 1, 0],
                       [1, 0, 1],
                       [0, 1, 0]])

# Create a graph object from the adjacency matrix
graph = nx.from_numpy_array(adj_matrix)

# Calculate degree centrality
degree_centrality = nx.degree_centrality(graph)

# Convert the centrality dictionary to a matrix (NumPy array)
num_nodes = len(graph.nodes)
centrality_matrix = np.zeros((num_nodes, num_nodes))

for node, centrality in degree_centrality.items():
    centrality_matrix[node, node] = centrality

print("Adjacency Matrix:")
print(adj_matrix)
print("\nDegree Centrality Matrix:")
print(centrality_matrix)

# Calculate other centralities
betweenness_centrality = nx.betweenness_centrality(graph)
closeness_centrality = nx.closeness_centrality(graph)
eigenvector_centrality = nx.eigenvector_centrality(graph)

print("\nBetweenness Centrality:", betweenness_centrality)
print("Closeness Centrality:", closeness_centrality)
print("Eigenvector Centrality:", eigenvector_centrality)
