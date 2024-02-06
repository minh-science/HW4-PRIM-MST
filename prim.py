import numpy as np
import heapq

def prim_mst(adjacency_matrix):
    """
    Prim's algorithm to find the Minimum Spanning Tree (MST) of a graph represented by an adjacency matrix.

    Parameters:
    - adjacency_matrix: 2D numpy array representing the weighted adjacency matrix.

    Returns:
    - mst_adjacency_matrix: 2D numpy array representing the adjacency matrix of the MST.
    - total_weight: Total weight of the MST.
    """
    num_vertices = len(adjacency_matrix)
    visited = [False] * num_vertices
    pred = [None] * num_vertices
    pi = [float('inf')] * num_vertices

    # Start from any node, let's say the first one (index 0)
    s = 0
    pi[s] = 0

    # Create an empty priority queue (min heap)
    pq = [(0, s)]  # (weight, vertex)

    while pq:
        ce, u = heapq.heappop(pq)

        if visited[u]:
            continue

        visited[u] = True

        for v, edge_weight in enumerate(adjacency_matrix[u]):
            if not visited[v] and edge_weight < pi[v]:
                pi[v] = edge_weight
                pred[v] = u
                heapq.heappush(pq, (edge_weight, v))

    # Build MST adjacency matrix
    mst_adjacency_matrix = np.zeros_like(adjacency_matrix)
    total_weight = 0

    for v in range(0, num_vertices):
        u = pred[v]
        print(u,v)
        mst_adjacency_matrix[u, v] = pi[v]
        mst_adjacency_matrix[v, u] = pi[v]
        total_weight += pi[v]

    return mst_adjacency_matrix, total_weight

# Example usage with an adjacency matrix
adjacency_matrix = np.array([[0, 1, 4, 0],
                             [1, 0, 3, 2],
                             [4, 3, 0, 5],
                             [0, 2, 5, 0]])

mst_matrix, total_weight = prim_mst(adjacency_matrix)
print("Minimum Spanning Tree Adjacency Matrix:\n", mst_matrix)
print("Total Weight of MST:", total_weight)
