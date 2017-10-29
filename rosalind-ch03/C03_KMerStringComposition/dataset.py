import os.path

class Dataset:

    k_val = ""
    string_text = 0

    def readFile(self,filename):
        if os.path.exists(filename):
            with open(filename,"r") as file:
                # first get the k value
                self.k_val = int(file.readline())
                # next get the k value
                self.string_text = file.readline()
            file.close()