from GreedyMotifSearth import dataset


def scoreMotifs(motif_matrix):
    score = 0
    for col in range(len(motif_matrix[0])):
        d = {"A": 0, "C": 0, "G": 0, "T": 0}
        for row in range(len(motif_matrix)):
            d[motif_matrix[row][col]] += 1
        score += (len(motif_matrix[0]) - d[max(d, key=d.get)])
    return score

# ------------------------------------------------------------------------------
# Greedy Motif Search Algorithm
# Takes a list of dna sequences, a k-mer length k, and the number
# of sequences t and produces a collection of motifs.
def greedyMotifSearch(dna, k, t):
    # First build the initial best-motif matrix
    best_motifs = []
    for sequence in dna:
        best_motifs.append(sequence[0:k])
    # Now form a list of the kmers in the first
    # string from dna
    first_kmers = getKmers(dna[0],k)
    # Loop through the kmers and perform the greedy search
    for motif in first_kmers:
        motifs = [motif]
        for i in range(1,t):
            # Create a profile
            profile = createProfile(motifs)
            # Add the profile most probably kmer to the motif matrix
            most_prob_kmer = profileMostProbableKmer(dna[i],k,profile)
            motifs.append(most_prob_kmer)
        # Compare the motif matrices. Replace if better
        if scoreMotifs(motifs) < scoreMotifs(best_motifs):
            best_motifs = motifs
    # Return the best motif matrix
    return best_motifs




# ------------------------------------------------------------------------------
# Returns a list of possile kmers of length k from the string text
def getKmers(text,k):
    kmers = []
    head = 0
    tail = k
    text_len = len(text)
    while tail < text_len:
        kmers.append(text[head:tail])
        head += 1
        tail += 1
    return kmers


# ------------------------------------------------------------------------------
# Returns the nth kmer of length k from the string text
def getNthKmer(text,k,n):
    head = n - 1
    tail = k + n
    return text[head:tail]

# ------------------------------------------------------------------------------
# Creates and returns a profile from a list of motifs
def createProfile(motifs):
    increment = 1/len(motifs)
    profile = {
        "A": [0 for x in range(len(motifs[0]))],
        "C": [0 for x in range(len(motifs[0]))],
        "G": [0 for x in range(len(motifs[0]))],
        "T": [0 for x in range(len(motifs[0]))],
    }
    for motif in motifs:
        for col in range(len(motif)):
            profile[motif[col]][col] += increment
    return profile

# ------------------------------------------------------------------------------
# Returns the profile most probable kmer of length "k" from the dna sequence
# "sequence" using the profile "profile"
def profileMostProbableKmer(sequence,k,profile):
    kmers = getKmers(sequence,k)
    max_prob = 0
    max_kmer = sequence[0:k]
    for kmer in kmers:
        prob = 1
        col = 0
        for c in kmer:
            prob *= profile[c][col]
            col += 1
        if prob > max_prob:
            max_prob = prob
            max_kmer = kmer
    return max_kmer


################################################################################
################################################################################
# Run the Program
#
# Read the data from the file
ds = dataset.Dataset()
ds.readFile("./dataset.txt")
final_motifs = greedyMotifSearch(ds.dna_strings,ds.k_val,ds.t_val)
for final_motif in final_motifs:
    print(final_motif)