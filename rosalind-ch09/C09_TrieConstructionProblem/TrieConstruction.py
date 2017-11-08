import Dataset
import copy


class Node:

    next_id = 0

    def __init__(self, _value=None, _children=list()):
        self.__id = Node.next_id
        Node.next_id += 1
        self.__value = _value
        self.__children = copy.deepcopy(_children)

    def id(self, _id=None):
        if _id is None:
            return self.__id
        else:
            self.__id = _id

    def value(self, value=None):
        if value is None:
            return self.__value
        else:
            self.__value = value

    def children(self, children=None):
        if children is None:
            return self.__children
        else:
            self.__children = copy.deepcopy(children)

    def num_children(self):
        return len(self.__children)

    def add_child(self, child):
        if child in self.__children:
            return False
        self.__children.append(copy.deepcopy(child))
        return True

    def get_child(self, index):
        if index < len(self.__children):
            return self.__children[index]
        else:
            return None

    def __str__(self):
        out_string = ""
        for child in self.__children:
            out_string += "{0}->{1}:{2}\n".format(self.__id,
                                                  child.id(),
                                                  child.value())
            if len(child.children()) != 0:
                out_string += str(child)
        return out_string


def construct_trie(words):
    trie = Node()
    for word in words:
        letter = word[0]
        found = False
        for i in range(trie.num_children()):
            if trie.get_child(i).value() == letter:
                found = True
                recursive_add(trie.get_child(i), word[1:])
                break
        if not found:
            child = Node(letter)
            trie.add_child(child)
            recursive_add(trie.get_child(trie.num_children()-1), word[1:])

    return trie


def recursive_add(node, remainder):
    if not remainder:
        return
    letter = remainder[0]
    for i in range(node.num_children()):
        if node.get_child(i).value() == letter:
            recursive_add(node.get_child(i), remainder[1:])
            return
    child = Node(letter)
    node.add_child(child)
    recursive_add(node.get_child(node.num_children() - 1), remainder[1:])


################################################################################
################################################################################
#
def main():
    words = Dataset.import_data("dataset.txt")
    if words is not None:
        trie = construct_trie(words)
        print str(trie)
        outfile = open("./output.txt","w")
        outfile.write(str(trie))
        outfile.close()


if __name__ == "__main__":
    main()