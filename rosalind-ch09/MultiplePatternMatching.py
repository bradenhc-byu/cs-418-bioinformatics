"""
Solution to Rosalind Chapter 9 Problem: Multiple Pattern Matching Problem
"""
from C09_Modules.Collections import SuffixArray
import BurrowsWheelerTransform
from collections import defaultdict
import os


def construct_partial_sa(text, k):
    suffix_array = SuffixArray(text)
    partial_suffix_array = []
    for index in suffix_array.get_suffix_indices():
        if index % k == 0:
            partial_suffix_array.append(index)
    return partial_suffix_array


def construct_checkpoint_array(text):

    def count(symbol, index, last_col):
        cnt = 0
        for i in range(index):
            if last_col[i] == symbol:
                cnt += 1
        return cnt

    keys = set()
    for c in text:
        keys.add(c)
    checkpoints = defaultdict(list)
    for k in keys:
        checkpoints[k].append(0)
    for j in range(1, len(text)):
        for k in keys:
            checkpoints[k].append(count(k, j, text))

    return checkpoints

def multiple_approximate_pattern_matching(text, patterns, d):
    transform = BurrowsWheelerTransform.transform(text)
    better_bw_matching(transform, patterns, d)


def better_bw_matching(last_col, pattern):
    alphabet = "$abcdefghijklmnopqrstuvwxyz"
    first_col = ''.join(sorted(last_col, key=lambda x: [alphabet.index(c) for c in x.lower()]))
    psa_indices = construct_partial_sa(last_col, len(pattern))
    ca = construct_checkpoint_array(last_col)
    top = 0
    bottom = len(last_col) - 1
    while top <= bottom:
        if pattern:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            search_space = last_col[top:bottom + 1]
            if symbol in search_space:
                first_occurrence = first_col.find(symbol)
                top = first_occurrence + ca[top]
                bottom = first_occurrence + ca[bottom + 1] - 1
            else:
                return 0
        else:
            return bottom - top + 1


def hamming_distance(p, q):
    d = 0
    for p, q in zip(p, q): # your code here
        if p != q:
            d += 1
    return d


def approx_pattern_match(pattern, text, d):
    positions = [] # initializing list of positions
    for i in range(len(text) - len(pattern) + 1):
        # and using distance < d, rather than exact matching
        if hamming_distance(pattern, text[i:i + len(pattern)]) <= d:
            positions.append(i)
    return positions


def approx_match_test():
    dataset_dir = "./datasets"
    filename = "approximate-pattern-matching.txt"
    output_dir = "./out"
    output_filename = filename.replace(".txt", "-out.txt")
    filepath = os.path.join(dataset_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, "r") as input_file:
            text = input_file.readline().rstrip()
            patterns = input_file.readline().split()
            d = int(input_file.readline().rstrip())
        output = []
        for pattern in patterns:
            matches = approx_pattern_match(pattern, text, d)
            for match in matches:
                output.append(match)
        output.sort()
        output = ' '.join([str(x) for x in output])
        print output
        if os.path.exists(output_dir):
            with open(os.path.join(output_dir, output_filename), "w+") as output_file:
                output_file.write(str(output))


if __name__ == "__main__":
    approx_match_test()