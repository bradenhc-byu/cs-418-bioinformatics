from C03_StringReconstructionFromReadPairs.dataset import Dataset
from collections import defaultdict


# ------------------------------------------------------------------------------
# Reconstructs a genome sequence from a list of (k,d)-mer pairs
#
def read_pair_reconstruction(pairs,k,d):
    # First, construct the DeBruijn Graph
    dgraph = get_paired_debruijn_graph(pairs,k)
    # Find a Eulerian Path through the graph
    epath = get_eulerian_path(dgraph)
    print(epath)
    # Walk the path and then backtrack to fill in the missing nucleotides
    result_prefix = epath[0][0]
    for i in range(1,len(epath)):
        result_prefix += epath[i][0][-1]
    result_suffix = epath[-1][1]
    i = -2
    while d >= 0:
        result_suffix = epath[i][1][0] + result_suffix
        i -= 1
        d -= 1
    return result_prefix + result_suffix


# ------------------------------------------------------------------------------
# Takes a list of pairs of kmers and constructs the paired DeBruijn Graph
#
def get_paired_debruijn_graph(pairs,k):
    graph = defaultdict(list)
    for pair in pairs:
        from_graph_pair = (pair[0][:k-1], pair[1][:k-1])
        to_graph_pair = (pair[0][1:], pair[1][1:])
        graph[from_graph_pair].append(to_graph_pair)
    return graph


# ------------------------------------------------------------------------------
# Given a DeBruijn Graph, return the Eulerian Path through the graph
#
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
################################################################################
# RUN THE PROGRAM
#
data = Dataset()
data.populate("./dataset.txt")
if data.contents_loaded:
    final_result = read_pair_reconstruction(data.pairs, data.k, data.d)
    print(final_result)
    print("GTGGTCGTGAGATGTTGA")
    outfile = open("./output.txt", "w")
    outfile.write(final_result)
    outfile.close()
