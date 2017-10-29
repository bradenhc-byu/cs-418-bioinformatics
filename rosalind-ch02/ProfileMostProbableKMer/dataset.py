import os.path

class Dataset:

    # This class represents the set of data we receive.
    # It has three member variables:
    # - dna_text            The text string for dna
    # - k_val               The value of 'k'
    # - profile_matrix      The profile matrix

    dna_text = ""
    k_val = 0
    matrix_height = 4
    profile_matrix = [[]]

    def readFile(self,filename):
        if os.path.exists(filename):
            with open(filename,"r") as file:
                # first get the dna text
                self.dna_text = file.readline()
                # next get the k value
                self.k_val = int(file.readline())
                # we are expecting a 4xk matrix, so initialize
                width = self.k_val
                height = self.matrix_height
                self.profile_matrix = [[0 for x in range(width)] for y in range(height)]
                # Now for all the remaining lines, we neen
                # to write them into a matrix
                row = 0
                for line in file:
                    col = 0
                    nums = line.split()
                    for val in nums:
                        self.profile_matrix[row][col] = float(val)
                        col += 1
                    row += 1
