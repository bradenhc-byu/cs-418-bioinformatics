import os.path
from collections import defaultdict


class NodeData:

    def __init__(self, _value=None):
        self.value = _value
        self.paths = defaultdict(bool)
        self.in_degree = 0
        self.out_degree = 0

    def value(self, _value=None):
        if _value is None:
            return self.value
        else:
            self.value = _value

    def add_path(self, to_node):
        self.paths[to_node] = False
        self.out_degree += 1

    def add_in_degree(self):
        self.in_degree += 1

    def get_paths(self):
        return self.paths

    def get_unvisited_paths(self):
        unvisited = list()
        for node in self.paths.keys():
            if not self.paths[node]:
                unvisited.append(node)
        return unvisited

    def has_unvisited_paths(self):
        for node in self.paths.keys():
            if not self.paths[node]:
                return True
        return False

    def take_path(self, to_node):
        if to_node not in self.paths.keys():
            return None
        self.paths[to_node] = True
        return to_node

    def unvisit_all_paths(self):
        for node in self.paths.keys():
            self.paths[node] = False

    def unvisit_path(self, node):
        if node in self.paths.keys():
            self.paths[node] = False


class Graph:

    def __init__(self):
        self.nodes = defaultdict(NodeData)
        self.total_edges = 0

    def add_path(self, from_node, to_node):
        self.nodes[from_node].add_path(to_node)
        self.nodes[to_node].add_in_degree()
        self.total_edges += 1

    def get_paths(self, from_node):
        if from_node not in self.nodes.keys():
            return None
        return self.nodes[from_node].get_paths()

    def get_nodes(self):
        return self.nodes.keys()

    def at(self, node):
        if node in self.nodes.keys():
            return self.nodes[node]

    def get_available_paths(self, from_node):
        if from_node not in self.nodes.keys():
            return None
        return self.nodes[from_node].get_unvisited_paths()

    def node_has_unvisited_paths(self, from_node):
        if from_node not in self.nodes.keys():
            return False
        return self.nodes[from_node].has_unvisited_paths()

    def has_unvisited_paths(self):
        for from_node in self.nodes.keys():
            if self.nodes[from_node].has_unvisited_paths():
                return True
        return False

    def unvisit_all(self):
        for from_node in self.nodes.keys():
            self.nodes[from_node].unvisit_all_paths()

    def cross_path(self, from_node, to_node):
        if from_node not in self.nodes.keys():
            return None
        return self.nodes[from_node].take_path(to_node)

    def get_total_edges(self):
        return self.total_edges

    def get_start_node(self):
        for node in self.nodes.keys():
            if self.nodes[node].out_degree > self.nodes[node].in_degree:
                return node
        return None

    def get_end_node(self):
        for node in self.nodes.keys():
            if self.nodes[node].out_degree < self.nodes[node].in_degree:
                return node
        return None


class Dataset:

    def __init__(self):
        self.graph = Graph()

    def extract_data_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                for line in file:
                    components = line.rstrip().split(" -> ")
                    node_val = int(components[0])
                    to_nodes_str = components[1].split(",")
                    for to_node in to_nodes_str:
                        self.graph.add_path(node_val,int(to_node))

                file.close()
