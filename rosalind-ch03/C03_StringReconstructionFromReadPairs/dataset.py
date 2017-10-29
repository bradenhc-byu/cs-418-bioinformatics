import os.path


class Dataset:

    def __init__(self):
        self.k = 0
        self.d = 0
        self.pairs = list()
        self.contents_loaded = False

    def populate(self, filename):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                num_values = file.readline().rstrip().split(" ")
                self.k = int(num_values[0])
                self.d = int(num_values[1])
                for line in file:
                    kmers = line.rstrip().split("|")
                    self.pairs.append((kmers[0], kmers[1]))
                self.contents_loaded = True
                file.close()
