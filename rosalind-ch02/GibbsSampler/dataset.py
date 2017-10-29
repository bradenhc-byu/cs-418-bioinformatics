# This class holds the data given to the problem from the dataset
# text file provided by Rosalind
class Dataset:

    k_val = 0
    t_val = 0
    n_val = 0
    dna_strings = []

    def readFile(self,filename):
        with open(filename,"r") as file:
            line = file.readline()
            nums = line.split()
            # Read in the k argument
            self.k_val = int(nums[0])
            # Read in the t argument
            self.t_val = int(nums[1])
            # Read in the N argument
            self.n_val = int(nums[2])
            # Read in the dna strings
            for line in file:
                self.dna_strings.append(line)