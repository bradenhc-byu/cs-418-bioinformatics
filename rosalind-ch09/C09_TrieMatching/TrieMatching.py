from C09_TrieConstructionProblem import TrieConstruction
from C09_TrieMatching import Dataset


def trie_matching(text, trie):
    matching_indices = list()
    i = 0
    while text:
        result = prefix_trie_matching(text, trie)
        if result is not None:
            matching_indices.append(i)
        i += 1
        text = text[1:]
    return matching_indices


def prefix_trie_matching(text, trie):
    symbol = text[0]
    i = 1
    v = trie
    while True:
        if i >= len(text):
            return None
        if v.num_children() == 0:
            return text
        else:
            match = False
            for j in range(v.num_children()):
                if v.get_child(j).value() == symbol:
                    symbol = text[i]
                    i += 1
                    v = v.get_child(j)
                    match = True
                    break
            if not match:
                return None


################################################################################
################################################################################
#
def main():
    data = Dataset.import_data("dataset.txt")
    if data.words is not None:
        trie = TrieConstruction.construct_trie(data.words)
        matching_indices = trie_matching(data.text, trie)
        print matching_indices
        outfile = open("./output.txt", "w")
        for n in matching_indices:
            outfile.write(str(n) + " ")


if __name__ == "__main__":
    main()
