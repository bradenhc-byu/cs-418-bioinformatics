from GibbsSampler import dataset
import random
import numpy


# ------------------------------------------------------------------------------
# Uses the gibbs sampling technique to find the best motifs in the provided
# sequences of dna. It find motifs of length k (k-mers), with t being the
# number of sequences and N being the number of times to repeat the procedure
def gibbsSampler(dna, k, t, n):
    #initialize variables
    motifs = []
    for sequence in dna:
        random_motif = randomMotifSelect(sequence, k)
        motifs.append(random_motif)
    best_motifs = list(motifs)
    # Start the algorithm loop
    for j in range(n):
        i = numpy.random.randint(0,t)
        profile = createGibbsProfile(motifs,i)
        i_kmers = getKmers(dna[i],k)
        profile_kmer = profileGeneratedKmer(i_kmers,profile)
        motifs[i] = profile_kmer
        if scoreMotifs(motifs) < scoreMotifs(best_motifs):
            best_motifs = list(motifs)
    return best_motifs

# ------------------------------------------------------------------------------
# Randomly select a k-mer from the sequence
def randomMotifSelect(sequence,k):
    kmers = getKmers(sequence,k)
    return numpy.random.choice(kmers)

# ------------------------------------------------------------------------------
# Selects a random item from a list given the probabilities
def weightedRandomSelect(item_list, probabilities):
    x = random.uniform(0, 1)
    cumulative_probability = 0.0
    for item, item_probability in zip(item_list, probabilities):
        cumulative_probability += item_probability
        if x < cumulative_probability: break
    return item

# ------------------------------------------------------------------------------
# Determines the profile most probable k-mer in the sequence using the
# provided profile probabilities
def profileGeneratedKmer(kmers,profile):
    # generate a list of probabilities
    probabilities = [1 for x in range(len(kmers))]
    kmer_pos = 0
    for kmer in kmers:
        profile_pos = 0
        for nucleotide in kmer:
            probabilities[kmer_pos] *= profile[nucleotide][profile_pos]
            profile_pos += 1
        kmer_pos += 1
    prob_sum = sum(probabilities)
    probabilities[:] = [val / prob_sum for val in probabilities]
    selected_kmer = numpy.random.choice(kmers,p=probabilities)
    return selected_kmer


# ------------------------------------------------------------------------------
# Creates and returns a profile from a list of motifs (using pseudo-counts)
def createGibbsProfile(motifs,i):
    profile = {
        "A": [1 for x in range(len(motifs[0]))],
        "C": [1 for x in range(len(motifs[0]))],
        "G": [1 for x in range(len(motifs[0]))],
        "T": [1 for x in range(len(motifs[0]))],
    }
    motif_position = 0
    for motif in motifs:
        if motif_position == i:
            continue
        for col in range(len(motif)):
            profile[motif[col]][col] += 1

    return profile


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
best_final_motifs = gibbsSampler(ds.dna_strings,ds.k_val,ds.t_val,ds.n_val)
for iteration in range(20):
    final_motifs = gibbsSampler(ds.dna_strings,ds.k_val,ds.t_val,ds.n_val)
    if scoreMotifs(final_motifs) < scoreMotifs(best_final_motifs):
        best_final_motifs = list(final_motifs)
for final_motif in best_final_motifs:
    print(final_motif)