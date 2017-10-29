from C03_EulerianPath.dataset_oo import Dataset
import numpy


# ------------------------------------------------------------------------------
# Returns the eulerian path from a directed graph
#
def get_eulerian_path(graph):
    path = []
    # Find the start node by finding which Node has an out degree greater than
    # the in degree
    start = graph.get_start_node()
    path.append(start)
    # Keep searching for a path that covers all
    while graph.has_unvisited_paths():
        # If we have an invalid path, randomly select a node that has unvisited
        # paths in the current path and backtrack to it
        if len(path) > 1:
            index = numpy.random.randint(0,len(path))
            random_node = path[index]
            while not graph.node_has_unvisited_paths(random_node):
                index = numpy.random.randint(0, len(path))
                random_node = path[index]
            random_next_node = numpy\
                               .random\
                               .choice(graph.get_available_paths(random_node))
            for i in range(index,len(path)-1):
                graph.at(path[i]).unvisit_path(path[i+1])
            path = path[0:index]
            path.append(random_node)
            graph.cross_path(random_node, random_next_node)
            path.append(random_next_node)
        # Until we hit a node that cannot be crossed, walk the graph
        while graph.node_has_unvisited_paths(path[-1]):
            # Pick a path to take
            next_node = numpy.random.choice(graph.get_available_paths(path[-1]))
            graph.cross_path(path[-1], next_node)
            path.append(next_node)
    # We have a path
    return path_to_string(path)


# ------------------------------------------------------------------------------
# Function for printing the contents of the path as num->num
#
def path_to_string(path):
    path_str = str(path[0])
    for i in range(1, len(path)):
        path_str += ("->" + str(path[i]))
    return path_str
################################################################################
# RUN THE PROGRAM
#
ds = Dataset()
ds.extract_data_from_file("./dataset.txt")
e_path = get_eulerian_path(ds.graph)
print(e_path)
outfile = open("./output.txt","w")
outfile.write(e_path)
outfile.close()
