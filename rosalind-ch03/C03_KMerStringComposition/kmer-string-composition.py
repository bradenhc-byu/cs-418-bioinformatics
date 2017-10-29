from C03_KMerStringComposition import dataset


# ------------------------------------------------------------------------------
# Get the composition of k-mers from the string text
def get_kmer_composition(text,k):
    kmers = []
    head = 0
    tail = k
    text_len = len(text)
    while tail <= text_len:
        kmers.append(text[head:tail])
        head += 1
        tail += 1
    kmers.sort()
    return kmers

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
print("Determining string composition of text....")
composition = get_kmer_composition(ds.string_text,ds.k_val)
print("Printing Results")
print(len(composition))
outfile = open("./output.txt","w")
for kmer in composition:
    print(kmer)
    outfile.write(kmer + "\n")
outfile.close()