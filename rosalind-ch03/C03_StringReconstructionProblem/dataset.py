import os.path
from collections import defaultdict


class Dataset:

    def __init__(self):
        self.k = 0
        self.graph = defaultdict(list)
        self.total_edges = 0
        self.contents_loaded = False

    def read_data_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                self.k = int(file.readline().rstrip())
                for line in file:
                    kmer = line.rstrip()
                    self.graph[kmer[:self.k-1]].append(kmer[1:])
                self.contents_loaded = True
                file.close()
