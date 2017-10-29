from C07_DistanceBetweenLeaves.dataset import Dataset


def get_distance_between_leaves(adjacency_list, num_nodes, num_leaves):
    # Used to calculate the distances
    adjacency_matrix = [[0 for y in range(num_nodes)] for x in range(num_nodes)]
    # Results of the distances. This is what gets returned
    result_matrix = [[0 for y in range(num_leaves)] for x in range(num_leaves)]
    # Construct the adjacency matrix
    for key in adjacency_list.keys():
        for path in adjacency_list[key]:
            adjacency_matrix[key][path[0]] = path[1]
            adjacency_matrix[path[0]][key] = path[1]
    # Construct the result matrix
    for row in range(num_leaves):
        for col in range(row):
            weight = find_node_weight(row,col,adjacency_matrix)
            result_matrix[row][col] = weight
            result_matrix[col][row] = weight

    return result_matrix


def find_node_weight(from_node, to_node, adjacency_matrix):
    for col in range(len(adjacency_matrix[from_node])):
        if adjacency_matrix[from_node][col] == 0:
            continue
        if col == to_node:
            return adjacency_matrix[from_node][col]
        step_weight = adjacency_matrix[from_node][col]
        adjacency_matrix[from_node][col] = 0
        adjacency_matrix[col][from_node] = 0
        next_weight = find_node_weight(col,to_node,adjacency_matrix)
        adjacency_matrix[from_node][col] = step_weight
        adjacency_matrix[col][from_node] = step_weight
        if next_weight != -1:
            return next_weight + step_weight
    return -1


def print_matrix(matrix, write=False):
    print("\n\n")
    writable_file = None
    if write:
        writable_file = open("./output.txt", "w")
    for i in range(len(matrix)):
        line = ""
        for j in range(len(matrix[0])):
            if matrix[i][j] > 99:
                value = str(matrix[i][j])
            elif matrix[i][j] > 9:
                value = str(matrix[i][j]) + " "
            else:
                value = str(matrix[i][j]) + "  "
            if j == len(matrix[0]) - 1:
                line += value
            else:
                line += (value + " ")
        if write:
            writable_file.write(line + "\n")
        print(line)
    if write:
        writable_file.close()

data = Dataset()
data.populate("./dataset.txt")
if data.loaded:
    rmatrix = get_distance_between_leaves(data.adjaceny_list,
                                          data.num_nodes,
                                          data.num_leaves)
    print_matrix(rmatrix, True)

