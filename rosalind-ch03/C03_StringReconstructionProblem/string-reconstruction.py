from C03_StringReconstructionProblem.dataset import Dataset
from collections import defaultdict


def reconstruct_string_from_graph(graph):
    path = get_eulerian_path(graph)
    sequence = path[0]
    for i in range(1,len(path)):
        sequence += path[i][-1]
    return sequence


def get_eulerian_path(graph, link_start_end=False):
    # Getting the start node by calculating in degrees and out degrees of
    # each node
    in_degrees = defaultdict(int)
    out_degrees = defaultdict(int)
    for key in graph.keys():
        out_degrees[key] = len(graph[key])
        for node in graph[key]:
            in_degrees[node] += 1
    start = -1
    end = -1
    for key in graph.keys():
        if in_degrees[key] < out_degrees[key]:
            start = key
        if in_degrees[key] > out_degrees[key]:
            end = key
    # Add a link to the start and end
    if link_start_end:
        if start != -1 and end != -1:
            graph[start].append(end)

    # Initialize the stack and path. Stack keeps track of progress through the
    # graph. Path will be the result.
    stack = [start]
    path = []

    # Traverse the graph
    while stack:
        node = stack[-1]
        if node not in graph.keys():
            path.append(stack.pop())
            continue
        if graph[node]:
            next_node = graph[node][0]
            stack.append(next_node)
            del graph[node][0]
        else:
            path.append(stack.pop())

    # Return the path
    return list(reversed(path))


# ------------------------------------------------------------------------------
# Prints the string representation of a path
#
def path_to_string(path):
    count = 0
    s = ""
    for n in path:
        s += str(n) + ("->" if count < len(path) else "")
    return s

################################################################################
# RUN THE MAIN PROGRAM
#
data = Dataset()
data.read_data_from_file("./dataset.txt")
if data.contents_loaded:
    print(data.graph)
    reconstruced_string = reconstruct_string_from_graph(data.graph)
    print(reconstruced_string)
    outfile = open("./output.txt", "w")
    outfile.write(reconstruced_string)
    outfile.close()
