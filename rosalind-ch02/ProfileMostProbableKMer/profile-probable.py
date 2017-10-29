from ProfileMostProbableKMer import dataset
ds = dataset.Dataset()
ds.readFile("./dataset.txt")

# find all the possible k-mers in the string
str_len = len(ds.dna_text)
head = 0
tail = ds.k_val
kmers = []
max_prop = 0
max_kmer = ""
while tail < str_len:
    kmers.append(ds.dna_text[head:tail])
    head += 1
    tail += 1

# go through all the possible k-mers and find the
# one with the highest probability
for kmer in kmers:
    prop = 1
    col = 0
    for c in kmer:
        if c == 'A':
            prop *= ds.profile_matrix[0][col]
        elif c == 'C':
            prop *= ds.profile_matrix[1][col]
        elif c == 'G':
            prop *= ds.profile_matrix[2][col]
        elif c == 'T':
            prop *= ds.profile_matrix[3][col]
        col += 1
    if prop > max_prop:
        max_prop = prop
        max_kmer = kmer

# print the result
print(max_kmer)