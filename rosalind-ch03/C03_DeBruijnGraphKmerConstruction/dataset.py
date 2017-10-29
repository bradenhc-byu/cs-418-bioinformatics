import os.path


class Dataset:

    kmers = []

    def readFile(self,filename):
        if os.path.exists(filename):
            with open(filename,"r") as file:
                for line in file:
                    self.kmers.append(line.rstrip())
                file.close()
