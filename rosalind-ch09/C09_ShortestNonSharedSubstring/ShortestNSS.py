########################################################################################################################
# Shortest Non-Shared Substring
#
from C09_LongestRepeatInString.Trie import SuffixTree


########################################################################################################################
# Main
#
import os


def main():
    filename = "dataset.txt"
    if os.path.exists(filename):
        with open(filename, "r") as input_file:
            text1 = input_file.readline().rstrip()
            text2 = input_file.readline().rstrip()
        substrings1 = SuffixTree(text1).get_substrings()
        substrings2 = SuffixTree(text2).get_substrings()
        for i in range(len(substrings1)):
            if substrings1[i] in substrings2:
                substrings1.pop(i)
                i -= 1
        print substrings1


if __name__ == "__main__":
    main()
