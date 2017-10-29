import os.path
from collections import defaultdict


class Dataset:

    def __init__(self):
        self.num_leaves = 0
        self.num_nodes = 0
        self.adjaceny_list = defaultdict(list)
        self.loaded = False

    def populate(self, filename):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                self.num_leaves = int(file.readline().rstrip())
                for line in file:
                    pair = line.split("->")
                    node = int(pair[0])
                    next_and_weight = pair[1].split(":")
                    next = int(next_and_weight[0])
                    weight = int(next_and_weight[1])
                    self.adjaceny_list[node].append((next, weight))
                self.num_nodes = len(self.adjaceny_list.keys())
                self.loaded = True
                file.close()
