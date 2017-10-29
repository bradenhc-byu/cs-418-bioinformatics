from C03_DeBruijnGraphKmerConstruction import dataset
import collections
from sortedcontainers import SortedList


# ------------------------------------------------------------------------------
# Get the composition of k-mers from the string text
def construct_debruijn_graph(kmers):
    d_graph = get_graph(kmers)
    return d_graph


# ------------------------------------------------------------------------------
# Construct an initial deBruijn Graph (before merging nodes)
def get_graph(kmers):
    graph = dict()
    for kmer in kmers:
        node = kmer[0:len(kmer)-1]
        to_node = kmer[1:len(kmer)]
        if node in graph.keys():
            graph[node].add(to_node)
        else:
            graph[node] = SortedList()
            graph[node].add(to_node)
    ordered_graph = collections.OrderedDict(sorted(graph.items()))
    return ordered_graph

################################################################################
# Run the program
#
# Testing Code -----------------------------------------------------------------
test_output_file = open("./test_output.txt")
test_output_lines = test_output_file.readlines()
test_output_file.close()
# ------------------------------------------------------------------------------
testing = False
if testing and len(test_output_lines) == 0:
    testing = False
# ------------------------------------------------------------------------------
ds = dataset.Dataset()
ds.readFile("./dataset.txt")
print("Determining string reconstruction from genome path....")
final_graph = construct_debruijn_graph(ds.kmers)
print("Printing Results")
outfile = open("./output.txt","w")
count = 0
for node,next_nodes in final_graph.items():
    if len(next_nodes) == 0:
        continue
    result = node + " -> " + next_nodes[0]
    for i in range(1, len(next_nodes)):
        result += ("," + next_nodes[i])
    if testing and result != test_output_lines[count].rstrip():
        print(result + "  X " + test_output_lines[count].rstrip())
    else:
        print(result)
    count += 1
    outfile.write(result + "\n")
outfile.close()