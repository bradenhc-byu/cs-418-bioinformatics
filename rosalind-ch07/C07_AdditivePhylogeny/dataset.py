import os.path


class Dataset:

    def __init__(self):
        self.num_leaves = 0
        self.distance_matrix = [[]]
        self.loaded = False

    def populate(self, filename):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                self.num_leaves = int(file.readline().rstrip())
                self.distance_matrix = [[0 for y in range(self.num_leaves)]
                                        for x in range(self.num_leaves)]
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
