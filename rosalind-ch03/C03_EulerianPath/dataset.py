import os.path
from collections import defaultdict


class Dataset:

    def __init__(self):
        self.graph = defaultdict(list)
        self.total_edges = 0
        self.contents_loaded = False

    def read_data_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                for line in file:
                    parts = line.rstrip().split(" -> ")
                    self.graph[parts[0]] = list()
                    paths = parts[1].split(",")
                    for path in paths:
                        self.graph[parts[0]].append(path)
                        self.total_edges += 1
                self.contents_loaded = True
                file.close()
