"""
Constructs the suffix array of a string
"""
import os
from C09_Modules.Collections import SuffixArray


def main():
    dataset_dir = "./datasets"
    filename = "suffix-array-construction.txt"
    output_dir = "./out"
    output_filename = "./suffix-array-construction-out.txt"
    filepath = os.path.join(dataset_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, "r") as input_file:
            text = input_file.readline().rstrip()
    suffix_array = SuffixArray(text)
    indices = suffix_array.get_suffix_indices()
    output = str(indices[0])
    for i in range(1, len(indices)):
        output += ", " + str(indices[i])
    print output
    if os.path.exists(output_dir):
        with open(os.path.join(output_dir, output_filename), "w+") as output_file:
            output_file.write(output)


if __name__ == "__main__":
    main()
