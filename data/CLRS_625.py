import numpy as np
matrix = np.loadtxt("CLRS_625.csv", delimiter=',')
# print(matrix)
t_matrix = np.transpose(matrix)
# print(t_matrix)
undirected = matrix + t_matrix
print(undirected)
np.savetxt("CLRS_625_undirected.csv", undirected, delimiter=",")