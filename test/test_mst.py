# mst unit tests
import pytest
import numpy as np
from mst import Graph
from sklearn.metrics import pairwise_distances


def check_mst(adj_mat: np.ndarray, 
              mst: np.ndarray, 
              expected_weight: int, 
              allowed_error: float = 0.0001):
    """
    
    Helper function to check the correctness of the adjacency matrix encoding an MST.
    Note that because the MST of a graph is not guaranteed to be unique, we cannot 
    simply check for equality against a known MST of a graph. 

    Arguments:
        adj_mat: adjacency matrix of full graph
        mst: adjacency matrix of proposed minimum spanning tree
        expected_weight: weight of the minimum spanning tree of the full graph
        allowed_error: allowed difference between proposed MST weight and `expected_weight`

    TODO: Add additional assertions to ensure the correctness of your MST implementation. For
    example, how many edges should a minimum spanning tree have? Are minimum spanning trees
    always connected? What else can you think of?

    """

    def approx_equal(a, b):
        return abs(a - b) < allowed_error

    total = 0
    for i in range(mst.shape[0]):
        for j in range(i+1):
            total += mst[i, j]
    assert approx_equal(total, expected_weight), 'Proposed MST has incorrect expected weight'


    # assert shape of the matrices are the same
    assert mst.shape == adj_mat.shape

    # asserts MST has V-1 edges (number of nonzero mst values divided by 2 because mst includes (u,v) and (v,u) edges )
    assert mst.shape[0]-1 == np.count_nonzero(mst)*0.5
    
    # asserts MST is connected
    vertices = set() # set of vertices
    connected = set() # set of vertices connected by MST
    for i in range(adj_mat.shape[0]):
        vertices.add(i)
    for i in range(mst.shape[0]):
        for j in range(mst.shape[1]):
            if j != 0:
                connected.add(i)
    # print(vertices)
    # print(connected)
    assert sorted(connected) == sorted(vertices)

def test_mst_small():
    """
    
    Unit test for the construction of a minimum spanning tree on a small graph.
    
    """
    file_path = './data/small.csv'
    g = Graph(file_path)
    g.construct_mst()
    check_mst(g.adj_mat, g.mst, 8)
    # edit
    # print("mst nonzero", g.mst.nonzero)
    # end edit

test_mst_small()

def test_mst_single_cell_data():
    """
    
    Unit test for the construction of a minimum spanning tree using single cell
    data, taken from the Slingshot R package.

    https://bioconductor.org/packages/release/bioc/html/slingshot.html

    """
    file_path = './data/slingshot_example.txt'
    coords = np.loadtxt(file_path) # load coordinates of single cells in low-dimensional subspace
    dist_mat = pairwise_distances(coords) # compute pairwise distances to form graph
    g = Graph(dist_mat)
    g.construct_mst()
    check_mst(g.adj_mat, g.mst, 57.263561605571695)

test_mst_single_cell_data()

def test_mst_student():
    """
    
    TODO: Write at least one unit test for MST construction.
    
    """
    # test based on implementation of Prim's in Introduction to Algorithms 3e by Cormen, Leiserson, Rivest, and Stein, page 625
    file_path = './data/CLRS_625_undirected.csv'
    g = Graph(file_path)
    g.construct_mst()
    check_mst(g.adj_mat, g.mst, 4+8+2+4+2+1+7+9)

test_mst_student()