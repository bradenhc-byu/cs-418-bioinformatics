"""
Finds matching patterns given the suffix array of a string and a list of patterns to match
"""
import os
from C09_Modules.Collections import SuffixArray


def main():
    dataset_dir = "./datasets"
    filename = "suffix-array-pattern-matching.txt"
    output_dir = "./out"
    output_filename = filename.replace(".txt", "-out.txt")
    filepath = os.path.join(dataset_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, "r") as input_file:
            text = input_file.readline().rstrip()
            patterns = []
            for line in input_file:
                patterns.append(line.rstrip())
    suffix_array = SuffixArray(text)
    output = []
    for pattern in patterns:
        matches = suffix_array.find(pattern)
        if type(matches) == list:
            for x in matches:
                output.append(x)
        else:
            output.append(matches)
    output.sort()
    output = ' '.join(str(x) for x in output)
    print output
    if os.path.exists(output_dir):
        with open(os.path.join(output_dir, output_filename), "w+") as output_file:
            output_file.write(output)


if __name__ == "__main__":
    main()
