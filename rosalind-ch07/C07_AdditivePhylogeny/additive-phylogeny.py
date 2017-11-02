from C07_AdditivePhylogeny.dataset import Dataset
from sortedcontainers import SortedDict
import numpy


# ------------------------------------------------------------------------------
# Performs the Additive Phylogeny algorithm
#
def run_additive_phylogeny(matrix, n):
    # Base case, when we have 2 x 2 matrix
    if n == 1:
        alist = SortedDict()
        length = get_limb_length(matrix, n)
        alist[0] = list()
        alist[0].append((n, length))
        alist[n] = list()
        alist[n].append((0, length))
        return alist

    limb_length = get_limb_length(matrix, n)
    for j in range(0, n-1):
        matrix[j][n] = matrix[j][n] - limb_length
        matrix[n][j] = matrix[j][n]

    # Find i,n,k such that D[i,k] = D[i,n] + D[n,k]
    i = 0
    k = 0
    for row in range(0,n-1):
        i = row
        for col in range(0, n-1):
            k = col
            if matrix[i][k] == matrix[i][n] + matrix[n][k]:
                break

    # Get the value of x
    x = matrix[i][n]

    # Remove the nth row and column from the matrix
    numpy.delete(matrix, n, axis=0)
    numpy.delete(matrix, n, axis=1)

    # Recurse
    alist = run_additive_phylogeny(matrix, n-1)

    # Get the potentially new node in the tree
    node = i
    while node != k:
        x -= alist[node][0]
        if x < 0:
            v = len(alist.keys())
            alist[v] = list()
            # TODO: create a new node 'v' and link it back into the tree
            break
        node = alist[node][0]

    return alist


# ------------------------------------------------------------------------------
# Calculates the limb length from the leaf node in row j of a nxn distance
# matrix
#
def get_limb_length(D, n):
    length = float("inf")
    for row in range(len(D)):
        for col in range(len(D[row])):
            i = row
            k = col
            if i != n and n != k and i != k:
                distance = (D[i][n]
                            + D[n][k]
                            - D[i][k]) / 2
                length = min(length,distance)
    return int(length)


# ------------------------------------------------------------------------------
# Gets the weight of one node to another based on the given adjacency matrix
#
def find_node_weight(from_node, to_node, adjacency_matrix):
    for col in range(len(adjacency_matrix[from_node])):
        if adjacency_matrix[from_node][col] == 0:
            continue
        if col == to_node:
            return adjacency_matrix[from_node][col]
        step_weight = adjacency_matrix[from_node][col]
        adjacency_matrix[from_node][col] = 0
        adjacency_matrix[col][from_node] = 0
        next_weight = find_node_weight(col, to_node, adjacency_matrix)
        adjacency_matrix[from_node][col] = step_weight
        adjacency_matrix[col][from_node] = step_weight
        if next_weight != -1:
            return next_weight + step_weight
    return -1


################################################################################
# RUN THE PROGRAM
#
data = Dataset()
data.populate("./dataset.txt")
if data.loaded:
    adjacency_list = run_additive_phylogeny(data.distance_matrix,
                                            data.num_leaves)
