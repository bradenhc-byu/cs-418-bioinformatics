from C03_GenomePathStringReconstruction import dataset


# ------------------------------------------------------------------------------
# Get the composition of k-mers from the string text
def construct_overlap_graph(genome_path):
    adjacency_list = []
    k = len(genome_path[0])
    genome_path.sort()
    for i in range(len(genome_path)):
        from_kmer = genome_path[i]
        for j in range(len(genome_path)):
            to_kmer = genome_path[j]
            if from_kmer[1:] == to_kmer[0:k-1]:
                adjacency_list.append((from_kmer, to_kmer))
                break
    return adjacency_list

################################################################################
# Run the program
#
# Testing Code -----------------------------------------------------------------
test_output_file = open("./test_output.txt")
test_output_lines = test_output_file.readlines()
test_output_file.close()
# ------------------------------------------------------------------------------
testing = True
if len(test_output_lines) == 0:
    testing = False
# ------------------------------------------------------------------------------
ds = dataset.Dataset()
ds.readFile("./dataset.txt")
print("Determining string reconstruction from genome path....")
print("Length of path: " + str(len(ds.genome_path)))
result_list = construct_overlap_graph(ds.genome_path)
print("Printing Results")
outfile = open("./output.txt","w")
for i in range(0,len(result_list)):
    result = result_list[i][0] + " -> " + result_list[i][1]
    if testing and result != test_output_lines[i].rstrip():
        print(result + "  X " + test_output_lines[i].rstrip())
    else:
        print(result)
    outfile.write(result + "\n")
outfile.close()