from RandomizedMotifSearch import dataset
import random



# ------------------------------------------------------------------------------
# Uses a randomized algorithm to determine the set of best motifs given several
# sequences of dna, a k value, and a t value
def randomizedMotifSearch(dna, k, t):
    # Generate a random best motif matrix
    motifs = []
    for sequence in dna:
        random_motif = randomMotifSelect(sequence,k)
        motifs.append(random_motif)
    best_motifs = motifs
    while True:
        profile = createProfile(motifs)
        motifs = []
        for sequence in dna:
            motifs.append(profileMostProbableKmer(sequence,k,profile))
        if scoreMotifs(motifs) < scoreMotifs(best_motifs):
            best_motifs = motifs
        else:
            return best_motifs


# ------------------------------------------------------------------------------
# Randomly select a k-mer from the sequence
def randomMotifSelect(sequence,k):
    kmers = getKmers(sequence,k)
    return random.choice(kmers)


# ------------------------------------------------------------------------------
# Creates and returns a profile from a list of motifs (using pseudo-counts)
def createProfile(motifs):
    increment = 1/(len(motifs) + 4)
    profile = {
        "A": [increment for x in range(len(motifs[0]))],
        "C": [increment for x in range(len(motifs[0]))],
        "G": [increment for x in range(len(motifs[0]))],
        "T": [increment for x in range(len(motifs[0]))],
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
# Determines the score of a matrix of motifs
def scoreMotifs(motif_matrix):
    score = 0
    for col in range(len(motif_matrix[0])):
        d = {"A": 0, "C": 0, "G": 0, "T": 0}
        for row in range(len(motif_matrix)):
            d[motif_matrix[row][col]] += 1
        score += (len(motif_matrix[0]) - d[max(d, key=d.get)])
    return score






################################################################################
################################################################################
# Run the Program
#

ds = dataset.Dataset()
ds.readFile("./dataset.txt")
best_final_motifs = randomizedMotifSearch(ds.dna_strings,ds.k_val,ds.t_val)
for x in range(1000):
    final_motifs = randomizedMotifSearch(ds.dna_strings,ds.k_val,ds.t_val)
    if scoreMotifs(final_motifs) < scoreMotifs(best_final_motifs):
        best_final_motifs = final_motifs
for final_motif in best_final_motifs:
    print(final_motif)