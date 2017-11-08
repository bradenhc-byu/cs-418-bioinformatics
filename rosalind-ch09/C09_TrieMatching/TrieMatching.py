from C09_TrieConstructionProblem import TrieConstruction
from C09_TrieMatching import Dataset


def trie_matching():

    return None

################################################################################
################################################################################
#
def main():
    words = Dataset.import_data("dataset.txt")
    if words is not None:
        trie = TrieConstruction.construct_trie(words)


if __name__ == "__main__":
    main()