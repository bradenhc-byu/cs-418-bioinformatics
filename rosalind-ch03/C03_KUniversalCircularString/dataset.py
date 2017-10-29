import os.path
from collections import defaultdict


class Dataset:

    def __init__(self):
        self.k = 0
        self.kmers = list()
        self.graph = defaultdict(list)
        self.total_edges = 0
        self.contents_loaded = False

    def populate(self, filename):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                self.k = int(file.readline().rstrip())
                for i in range(pow(2,self.k)):
                    kmer = format(i, '0' + str(self.k) + 'b')
                    self.kmers.append(kmer)
                for kmer in self.kmers:
                    self.graph[kmer[:self.k-1]].append(kmer[1:])
                self.contents_loaded = True
                file.close()
