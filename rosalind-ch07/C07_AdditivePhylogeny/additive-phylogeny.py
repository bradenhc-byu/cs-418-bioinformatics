from C07_AdditivePhylogeny.dataset import Dataset
from sortedcontainers import SortedDict


# ------------------------------------------------------------------------------
# Performs the Additive Phylogeny algorithm
#
def run_additive_phylogeny(matrix, n):
    if n == 2:
        alist = SortedDict()

    return None

# ------------------------------------------------------------------------------
# Calculates the limb length from the leaf node in row j of a nxn distance
# matrix
#
def get_limb_length(j, distance_matrix):
    length = float("inf")
    for row in range(len(distance_matrix)):
        for col in range(len(distance_matrix[row])):
            i = row
            k = col
            if i != j and j != k and i != k:
                distance = (distance_matrix[i][j]
                            + distance_matrix[j][k]
                            - distance_matrix[i][k]) / 2
                length = min(length,distance)
    return int(length)


################################################################################
# RUN THE PROGRAM
#
data = Dataset()
data.populate("./dataset.txt")
if data.loaded:
    adjacency_list = run_additive_phylogeny(data.distance_matrix,
                                            data.num_leaves)
