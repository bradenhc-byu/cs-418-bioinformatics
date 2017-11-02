from C07_LimbLengthProblem.dataset import Dataset


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
    l = get_limb_length(data.j_row, data.distance_matrix)
    print l
