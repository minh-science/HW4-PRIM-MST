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
        self.mst_edges = [] # store edges of MST 

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

        # initialize S and T
        S = [] # spanning tree set   
        T = [] # atttachment cost

        # code for Prim's without using heapq (based on the lecture)
        # pi = {v:float('inf')  for v in V}
        # pred = {v: None for v in V}
        # pi[0] = 0 
        # print(pred)
        # print("this is pi", pi)


        # create empty priority queue
        pq = []

        # add (weight = 0, (u = 0, v = 0)) to priority queue as the source node 
        heapq.heappush(pq, ( matrix[0][0] , (0,0) )  ) 

        # create empty MST with same dimensions as the adjacency matrix
        self.mst = np.zeros_like(self.adj_mat)

        # go through terms in priority queue and builds the MST 
        while len(pq) != 0: 
            pop = heapq.heappop(pq) # removes lowest weight term from priority queue
            # print(pq)
            # print("pop:", pop)
            w = pop[0] # weight of lowest weight term (highest priority) in priority queue
            u, v = pop[1] # gets edge of lowest weight term
            # print("u,v,w:",u, v, w)

            # add all edges that are connected to u and not in S to the priority queue
            if v not in S: # check if destination node is in explored set S
                for v_i in V: # goes through all verticies in V, v_i is the edge (v,v_i) that v may be connected to 
                    pi_v = matrix[v][v_i] 
                    if pi_v > 0: # only adds (pi_v, (v, v_i)) if v (the node being added to the explored set) is connected to v_i (a possible frontier node)
                        heapq.heappush(pq, ( pi_v , (v, v_i) )  ) # pushes to priority queue

            # if u is in the explored set and if v is not in the explored set, add to the minimum spanning tree (priority is assured via the priority queue)
            if u in S: 
                if v not in S: 
                    self.mst[v,u] = w # assigns weight to edge
                    self.mst[u,v] = w # MST is symmetric for an undirected graph 
                    T.append(w)
                    self.mst_edges.append( (u,v) ) 
            
            S.append(v) # adds the explored vertex v to the explored set S
            
                            
        # print(self.mst)      
        # print(T)
        total = 0            
        for i in range(self.mst.shape[0]):
            for j in range(i+1):
                total += self.mst[i, j]
        # print(total)

        


# file_path = './data/small.csv'
# g = Graph(file_path)
# mst = g.construct_mst()
# print("construct mst: \n", mst)
