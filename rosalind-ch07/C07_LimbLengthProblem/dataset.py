import os.path
from collections import defaultdict


class Dataset:

    def __init__(self):
        self.j_row = 0
        self.num_nodes = 0
        self.distance_matrix = [[]]
        self.loaded = False

    def populate(self, filename):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                self.num_nodes = int(file.readline().rstrip())
                self.j_row = int(file.readline().rstrip())
                self.distance_matrix = [[0 for y in range(self.num_nodes)]
                                        for x in range(self.num_nodes)]
                row = 0
                for line in file:
                    col = 0
                    nums = line.split()
                    for num in nums:
                        self.distance_matrix[row][col] = int(num)
                        col += 1
                    row += 1
                self.loaded = True
                file.close()
