import os.path

class Dataset:

    genome_path = []

    def readFile(self,filename):
        if os.path.exists(filename):
            with open(filename,"r") as file:
                for line in file:
                    self.genome_path.append(line.rstrip())
            file.close()
