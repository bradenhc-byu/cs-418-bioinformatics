from C03_EulerianCycle.dataset import Dataset
import numpy


# ------------------------------------------------------------------------------
# Returns the eulerian cycle from a directed graph
def get_eulerian_cycle(graph, num_edges):
    # Get a cycle
    cur_cycle = traverse(graph, [])
    cycle_nodes = len(cur_cycle)
    last_cycle = cur_cycle
    # As long as not all edges have been traversed
    while cycle_nodes - 1 != num_edges:
        cur_cycle = traverse(graph, last_cycle)
        cycle_nodes = len(cur_cycle)
        last_cycle = cur_cycle
    cycle_str = str(cur_cycle[0])
    for i in range(1,len(cur_cycle)):
        cycle_str += "->" + str(cur_cycle[i])
    return cycle_str


# ------------------------------------------------------------------------------
# Creates a new cycle by walking the 'graph' starting at 'start' until all
# possible nodes have been visited. Walks each edge only once
def traverse(graph, last_cycle):
    cycle = last_cycle
    # Find a new node to start from
    if len(last_cycle) != 0:
        # We are not on the first iteration
        pos = 0
        found_node = False
        for node_val in last_cycle:
            for node in graph[node_val]:
                if not node.visited():
                    found_node = True
                    break
            if found_node:
                break
            pos += 1
        start = last_cycle[pos]
        if pos != 0 and pos != len(last_cycle) - 1:
            cycle = rotate(cycle[:-1], pos)
            cycle.append(start)
    else:
        # First iteration. Randomly pick start
        start = numpy.random.randint(0, len(graph))
        cycle.append(start)

    # Start building the new cycle
    cur_node = cycle[-1]
    while True:
        rand_node_index = numpy.random.randint(0, len(graph[cur_node]))
        while graph[cur_node][rand_node_index].visited():
            rand_node_index = numpy.random.randint(0, len(graph[cur_node]))
        graph[cur_node][rand_node_index].visited(True)
        cycle.append(graph[cur_node][rand_node_index].value())
        cur_node = cycle[-1]
        if cur_node == start:
            break
    return cycle


# ------------------------------------------------------------------------------
# Rotates a list by shifting to the left n positions
def rotate(l, n):
    return l[n:] + l[:n]

################################################################################
# RUN THE PROGRAM
#
ds = Dataset()
ds.extract_data_from_file("./dataset.txt")
e_cycle = get_eulerian_cycle(ds.graph(), ds.total_edges())
print(e_cycle)
outfile = open("./output.txt","w")
outfile.write(e_cycle)
outfile.close()