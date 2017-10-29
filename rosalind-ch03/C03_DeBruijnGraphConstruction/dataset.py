import os.path


class Dataset:

    sequence = ""
    k_val = 0

    def readFile(self,filename):
        if os.path.exists(filename):
            with open(filename,"r") as file:
                    self.k_val = int(file.readline().rstrip())
                    self.sequence = file.readline().rstrip()
            file.close()
