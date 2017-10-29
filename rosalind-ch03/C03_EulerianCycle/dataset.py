import os.path


class Node:

    def __init__(self, _value=None, _visited=False):
        self.__value = _value
        self.__visited = _visited

    def visited(self, _visited=None):
        if _visited is None:
            return self.__visited
        else:
            self.__visited = _visited

    def value(self, _value=None):
        if _value is None:
            return self.__value
        else:
            self.__value = _value

    def __str__(self):
        return "Node(value=" + str(self.__value) \
               + ",visited=" + str(self.__visited) + ")"


class Dataset():

    def __init__(self):
        self.__directed_graph = dict()
        self.__total_edges = 0

    def extract_data_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                for line in file:
                    components = line.rstrip().split(" -> ")
                    node_val = int(components[0])
                    to_nodes = []
                    to_nodes_str = components[1].split(",")
                    for to_node in to_nodes_str:
                        node = Node(int(to_node))
                        to_nodes.append(node)
                        self.__total_edges += 1
                    self.__directed_graph[node_val] = to_nodes

                file.close()

    def graph(self):
        return self.__directed_graph

    def total_edges(self):
        return self.__total_edges
