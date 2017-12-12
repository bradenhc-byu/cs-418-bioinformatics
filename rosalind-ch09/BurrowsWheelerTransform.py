"""
Finds matching patterns given the suffix array of a string and a list of patterns to match
"""
import os
from collections import defaultdict
from C09_Modules.Collections import SuffixArray


def transform(text):
    if text.find("$") == -1:
        text += "$"
    transform_result = ""
    rotations = []
    for i in range(len(text)):
        rotations.append(''.join(text[i:] + text[:i]))
    alphabet = "$abcdefghijklmnopqrstuvwxyz"
    rotations.sort(key=lambda x: [alphabet.index(c) for c in x.lower()])
    for rotation in rotations:
        transform_result += rotation[-1]
    return transform_result


def invert(transform):

    def first_to_last(last, m):
        s = len(m)
        for k in range(s):
            if m[k][s - 1] == last:
                return m[k][0]

    alphabet = "$abcdefghijklmnopqrstuvwxyz"
    sorted_transform = sorted(transform, key=lambda x: [alphabet.index(c) for c in x.lower()])
    transform_pointers = []
    sorted_transform_pointers = []
    counts = defaultdict(int)
    for c in transform:
        transform_pointers.append((c, counts[c]))
        counts[c] += 1
    counts = defaultdict(int)
    for c in sorted_transform:
        sorted_transform_pointers.append((c, counts[c]))
        counts[c] += 1
    size = len(transform)
    matrix = []
    for i in range(size):
        row = [("?", -1) for x in range(size)]
        row[0] = sorted_transform_pointers[i]
        row[size - 1] = transform_pointers[i]
        matrix.append(row)
    for i in range(size):
        for j in range(1, size - 1):
            matrix[i][j] = first_to_last(matrix[i][j-1], matrix)
    inversion = ''.join([c for c,i in matrix[0]])
    inversion = inversion[1:] + inversion[0]
    return inversion


########################################################################################################################
# Main method - unit testing
#
def construct_test():
    dataset_dir = "./datasets"
    filename = "burrows-wheeler-transform-construction.txt"
    output_dir = "./out"
    output_filename = filename.replace(".txt", "-out.txt")
    filepath = os.path.join(dataset_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, "r") as input_file:
            text = input_file.readline().rstrip()
        output = transform(text)
        print output
        if os.path.exists(output_dir):
            with open(os.path.join(output_dir, output_filename), "w+") as output_file:
                output_file.write(output)


def invert_test():
    dataset_dir = "./datasets"
    filename = "burrows-wheeler-transform-inversion.txt"
    output_dir = "./out"
    output_filename = filename.replace(".txt", "-out.txt")
    filepath = os.path.join(dataset_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, "r") as input_file:
            text = input_file.readline().rstrip()
        output = invert(text)
        print output
        if os.path.exists(output_dir):
            with open(os.path.join(output_dir, output_filename), "w+") as output_file:
                output_file.write(output)


if __name__ == "__main__":
    # construct_test()
    invert_test()
