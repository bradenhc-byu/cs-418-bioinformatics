from C03_GenomePathStringReconstruction import dataset


# ------------------------------------------------------------------------------
# Get the composition of k-mers from the string text
def reconstruct_string_from_path(genome_path):
    string = genome_path[0]
    k = len(genome_path[0])
    for i in range(1,len(genome_path)):
        string += genome_path[i][k-1:]
    return string

################################################################################
# Run the program
#
ds = dataset.Dataset()
ds.readFile("./dataset.txt")
# Testing Code
#test_output_file = open("./test_output.txt")
#test_output = []
#for line in test_output_file:
#    test_output.append(line.rstrip())
#print(test_output[0])
#print(len(test_output))
print("Determining string reconstruction from genome path....")
reconstructed_string = reconstruct_string_from_path(ds.genome_path)
print("Printing Results")
outfile = open("./output.txt","w")
print(reconstructed_string)
outfile.write(reconstructed_string)
outfile.close()