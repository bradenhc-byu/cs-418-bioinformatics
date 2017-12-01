################################################################################
# Construct a Suffix Tree
#
#
import os
from C09_TrieConstructionProblem import TrieConstruction


def construct_suffix_tree(text):
    trie = build_suffix_trie(text)
    compress_suffix_trie(trie)
    return trie


def build_suffix_trie(text):
    words = []
    for i in range(len(text)):
        words.append(text[i:])
    return TrieConstruction.construct_trie(words)


def compress_suffix_trie(trie):
    if trie.num_children() == 0:
        return trie.value()
    if trie.num_children() == 1:
        compress_suffix_trie(trie.get_child(0))
        suffix = trie.get_child(0).value()
        trie.value(trie.value() + suffix)
        trie.remove_child(0)
        return trie.value()
    for child in trie.children():
        compress_suffix_trie(child)
    return trie.value()


################################################################################
# Unit Testing - Main Function
#
def recursive_trie_print(trie):
    if trie.num_children() == 0:
        if trie.value():
            print trie.value()
        return
    for child in trie.children():
        recursive_trie_print(child)
    if trie.value() is not None:
        print trie.value()


def recursive_trie_to_list(trie, printed_list):
    if trie.num_children() == 0:
        if trie.value():
            printed_list.append(trie.value())
        return
    for child in trie.children():
        recursive_trie_to_list(child, printed_list)
    if trie.value() is not None:
        printed_list.append(trie.value())


if __name__ == "__main__":
    filename = "dataset.txt"
    if os.path.exists(filename):
        with open(filename, "r") as input_file:
            text = input_file.readline().rstrip()
        tree = construct_suffix_tree(text)
        recursive_trie_print(tree)
        result_list = list()
        recursive_trie_to_list(tree, result_list)
        outfile = open("./output.txt", "w")
        outfile.write('\n'.join(result_list))
        outfile.close()