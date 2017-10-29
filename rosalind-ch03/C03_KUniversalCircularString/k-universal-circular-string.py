from C03_KUniversalCircularString.dataset import Dataset
import random


def reconstruct_string_from_graph(graph, k):
    path = get_eulerian_cycle(graph)
    print(path)
    sequence = str(path[0])
    for i in range(1,len(path)-(k-1)):
        sequence += str(path[i][-1])
    return sequence


def get_eulerian_cycle(graph):
    # Choose a random start node
    start = random.choice(list(graph.keys()))

    # Initialize the stack and path. Stack keeps track of progress through the
    # graph. Path will be the result.
    path = [start]
    edges_left = True

    # Traverse the graph
    while edges_left:
        # Still have edges, rotate the path
        node = None
        if len(path) > 1:
            pos = 0
            for visited_node in path:
                if graph[visited_node]:
                    start = visited_node
                    break
                pos += 1
            if pos != 0 and pos != len(path) - 1:
                path = rotate(path[:-1], pos)
                path.append(start)
        while node != start:
            node = path[-1]
            next_node_index = random.randint(0, len(graph[node]) - 1)
            path.append(graph[node][next_node_index])
            del graph[node][next_node_index]
            node = path[-1]
        edges_left = False
        for key in graph.keys():
            if graph[key]:
                edges_left = True

    # Return the path
    return path


# ------------------------------------------------------------------------------
# Rotates a list by shifting to the left n positions
def rotate(l, n):
    return l[n:] + l[:n]


################################################################################
# RUN THE MAIN PROGRAM
#
data = Dataset()
data.populate("./dataset.txt")
if data.contents_loaded:
    reconstruced_string = reconstruct_string_from_graph(data.graph,data.k)
    print(reconstruced_string)
    outfile = open("./output.txt", "w")
    outfile.write(reconstruced_string)
    outfile.close()
