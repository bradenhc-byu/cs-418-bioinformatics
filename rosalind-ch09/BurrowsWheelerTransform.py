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


def get_first_to_last_mapping(transform, index):
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
    return sorted_transform_pointers.index(transform_pointers[index])


def bw_matching(transform, pattern):

    last_col = transform
    alphabet = "$abcdefghijklmnopqrstuvwxyz"
    first_col = ''.join(sorted(last_col, key=lambda x: [alphabet.index(c) for c in x.lower()]))
    fc_ptrs = []
    lc_ptrs = []
    kcounts = defaultdict(int)
    vcounts = defaultdict(int)
    for i in range(len(transform)):
        fc_ptrs.append((first_col[i], kcounts[first_col[i]]))
        lc_ptrs.append((last_col[i], vcounts[last_col[i]]))
        kcounts[first_col[i]] += 1
        vcounts[last_col[i]] += 1

    def last_to_first(index):
        return fc_ptrs.index(lc_ptrs[index])

    top = 0
    bottom = len(transform) - 1
    while top <= bottom:
        if pattern:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            search_space = transform[top:bottom + 1]
            if symbol in search_space:
                top_index = top + search_space.find(symbol)
                bottom_index = top + ''.join(search_space).rfind(symbol)
                top = last_to_first(top_index)
                bottom = last_to_first(bottom_index)
            else:
                return 0
        else:
            return bottom - top + 1


def count(symbol, index, last_col):
    cnt = 0
    for i in range(index):
        if last_col[i] == symbol:
            cnt += 1
    return cnt


def fast_bw_matching(last_col, pattern, countfun=count):
    alphabet = "$abcdefghijklmnopqrstuvwxyz"
    first_col = ''.join(sorted(last_col, key=lambda x: [alphabet.index(c) for c in x.lower()]))
    top = 0
    bottom = len(last_col) - 1
    while top <= bottom:
        if pattern:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            search_space = last_col[top:bottom + 1]
            if symbol in search_space:
                first_occurrence = first_col.find(symbol)
                top = first_occurrence + countfun(symbol, top, last_col)
                bottom = first_occurrence + countfun(symbol, bottom + 1, last_col) - 1
            else:
                return 0
        else:
            return bottom - top + 1





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


def first_to_last_test():
    dataset_dir = "./datasets"
    filename = "burrows-wheeler-first-to-last.txt"
    output_dir = "./out"
    output_filename = filename.replace(".txt", "-out.txt")
    filepath = os.path.join(dataset_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, "r") as input_file:
            text = input_file.readline().rstrip()
            index = int(input_file.readline().rstrip())
        output = get_first_to_last_mapping(text, index)
        print output
        if os.path.exists(output_dir):
            with open(os.path.join(output_dir, output_filename), "w+") as output_file:
                output_file.write(str(output))


def bw_matching_test():
    dataset_dir = "./datasets"
    filename = "burrows-wheeler-matching.txt"
    output_dir = "./out"
    output_filename = filename.replace(".txt", "-out.txt")
    filepath = os.path.join(dataset_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, "r") as input_file:
            text = input_file.readline().rstrip()
            patterns = input_file.readline().split()
        output = []
        for pattern in patterns:
            output.append(bw_matching(text, pattern))
        output = ' '.join([str(x) for x in output])
        print output
        if os.path.exists(output_dir):
            with open(os.path.join(output_dir, output_filename), "w+") as output_file:
                output_file.write(str(output))


def fast_bw_matching_test():
    dataset_dir = "./datasets"
    filename = "burrows-wheeler-matching-fast.txt"
    output_dir = "./out"
    output_filename = filename.replace(".txt", "-out.txt")
    filepath = os.path.join(dataset_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, "r") as input_file:
            text = input_file.readline().rstrip()
            patterns = input_file.readline().split()
        output = []
        for pattern in patterns:
            output.append(fast_bw_matching(text, pattern))
        output = ' '.join([str(x) for x in output])
        print output
        if os.path.exists(output_dir):
            with open(os.path.join(output_dir, output_filename), "w+") as output_file:
                output_file.write(str(output))


if __name__ == "__main__":
    # construct_test()
    # invert_test()
    # first_to_last_test()
    # bw_matching_test()
    fast_bw_matching_test()
