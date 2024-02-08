import numpy as np
import heapq
from typing import Union

class Graph:

    def __init__(self, adjacency_mat: Union[np.ndarray, str]):
        """
    
        Unlike the BFS assignment, this Graph class takes an adjacency matrix as input. `adjacency_mat` 
        can either be a 2D numpy array of floats or a path to a CSV file containing a 2D numpy array of floats.

        In this project, we will assume `adjacency_mat` corresponds to the adjacency matrix of an undirected graph.
    
        """
        if type(adjacency_mat) == str:
            self.adj_mat = self._load_adjacency_matrix_from_csv(adjacency_mat)
        elif type(adjacency_mat) == np.ndarray:
            self.adj_mat = adjacency_mat
        else: 
            raise TypeError('Input must be a valid path or an adjacency matrix')
        self.mst = None
        # store edges of MST 
        self.mst_edges = []

    def _load_adjacency_matrix_from_csv(self, path: str) -> np.ndarray:
        with open(path) as f:
            return np.loadtxt(f, delimiter=',')

    def construct_mst(self):
        """
    
        TODO: Given `self.adj_mat`, the adjacency matrix of a connected undirected graph, implement Prim's 
        algorithm to construct an adjacency matrix encoding the minimum spanning tree of `self.adj_mat`. 
            
        `self.adj_mat` is a 2D numpy array of floats. Note that because we assume our input graph is
        undirected, `self.adj_mat` is symmetric. Row i and column j represents the edge weight between
        vertex i and vertex j. An edge weight of zero indicates that no edge exists. 
        
        This function does not return anything. Instead, store the adjacency matrix representation
        of the minimum spanning tree of `self.adj_mat` in `self.mst`. We highly encourage the
        use of priority queues in your implementation. Refer to the heapq module, particularly the 
        `heapify`, `heappop`, and `heappush` functions.

        """

        matrix = self.adj_mat
        # print(matrix.shape)

        # initlize vertices
        V = [i for i in range(self.adj_mat.shape[0])]
        # print("this is V:", V)

        # initalize edges 
        E = []
        for i in range(0,self.adj_mat.shape[0]):
            for j in range(0, self.adj_mat.shape[0]):
                E.append((i,j))
        # print("this is E:", E)'
                

        # s is the first node in V
        s = 0 

        # initialize S and T
        S = [] # spanning tree set   
        T = [] # atttachment cost

        pi = {v:float('inf')  for v in V}
        pred = {v: None for v in V}
        pi[0] = 0 
        # print(pred)
        # print("this is pi", pi)

        pq = [(0, 0)] # tuple: (weight, neighbor)

        # create empty priority queue
        pq1 = []
        
        heapq.heappush(pq1, ( matrix[s][s] , (s,s) )  )
        self.mst = np.zeros_like(self.adj_mat)

        # # print("pq1", pq1)
        while len(pq1) != 0:
            pop = heapq.heappop(pq1)
            # print(pq1)
            # print("pop:", pop)
            w = pop[0]
            u, v = pop[1]
            # print("u,v,w:",u, v, w)
            # if u in S:
            #     print("wheee")            
            if v not in S:
                for v_i in V:
                    pi_v = matrix[v][v_i]
                    if pi_v > 0:
                        heapq.heappush(pq1, ( pi_v , (v, v_i) )  )
                        # self.mst[v,u] = w
            if u in S:
                if v not in S:
                    self.mst[v,u] = w
                    self.mst[u,v] = w
                    T.append(w)
                    # print(T)
                    self.mst_edges.append( (u,v) )
            S.append(v)
            
# heapq, heap-push, make sure it works and removes from the queue properly       
                            
        # print(self.mst)      
        # print(T)
        total = 0            
        for i in range(self.mst.shape[0]):
            for j in range(i+1):
                total += self.mst[i, j]
        # print(total)

        


file_path = './data/small.csv'
g = Graph(file_path)
mst = g.construct_mst()
# print("construct mst: \n", mst)
