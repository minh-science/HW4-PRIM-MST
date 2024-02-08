# create undirected graph from graph in Introduction to Algorithms 3e by Cormen, Leiserson, Rivest, and Stein, page 625
import numpy as np
matrix = np.loadtxt("CLRS_625.csv", delimiter=',') # csv with edges and weights as adjacency list
# print(matrix)
t_matrix = np.transpose(matrix) # easier to transpose matrix and add to original instead of writing entire matrix by hand 
# print(t_matrix)
undirected = matrix + t_matrix
print(undirected)
np.savetxt("CLRS_625_undirected.csv", undirected, delimiter=",")