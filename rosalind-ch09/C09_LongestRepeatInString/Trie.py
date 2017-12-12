"""
A class for constructing a trie given a set of words. There are two tries
implemented in this module. The first is a generic Trie, the second is a
suffix trie.
"""
import copy


class Edge(object):
    """
    A class describing an edge between two nodes in a trie.
    """

    def __init__(self):
        self.__value = ""
        self.__to_node = Node()

    def value(self, value=None):
        """Getter and setter for the value member variable"""
        if value is None:
            return self.__value
        else:
            self.__value = value
            return True

    def dest_node(self, dest_node=None):
        """Getter and setter for the from and to node member variable values"""
        if dest_node is None:
            return self.__to_node
        else:
            self.__to_node = dest_node
            return True



class Node(object):
    """
    A class describing a Node object inside of a Trie. Nodes contain a label
    and a list of edges.
    """

    ID_COUNT = 0

    def __init__(self):
        self.__label = ""
        self.__edges = list()
        self.__id = Node.ID_COUNT
        Node.ID_COUNT += 1

    def id(self):
        return self.__id

    def label(self, label=None):
        """Getter and setter method for the label member variable"""
        if label is None:
            return self.__label
        else:
            self.__label = label
            return True

    def edges(self, edges=None):
        """Getter and setter method for the list of edges in the Node object"""
        if edges is None:
            return self.__edges
        else:
            self.__edges = copy.deepcopy(edges)

    def add_edge(self, edge):
        """Adds an edge to the list of edges in the class. Verifies the edge
        is of the class type Edge before doing so"""
        if type(edge) is Edge:
            self.__edges.append(edge)
            return True
        else:
            return False

    def remove_edge(self, edge):
        """Removes an edge from the list of edges after verifying it is of
        the correct type and the edge is included in the list already"""
        if type(edge) is Edge:
            index = self.__edges.index(edge)
            if index < 0:
                return False
            self.__edges.pop(index)
            return True


class Trie(object):
    """A class describing a Trie data structure made up of nodes and edges"""

    def __init__(self, words=None):
        self.__root = Node()
        if words is not None:
            self.populate(words)

    def root(self):
        return self.__root

    def populate(self, words):
        """Takes a set of words and generates nodes and edges to fill the
        trie"""

        def recursive_add(node, word_remainder):
            """Helper method for populate(), recursively adds nodes to the
            trie using the suffixes of the words provided in the populate
            method"""
            if not word_remainder:
                return
            letter = word_remainder[0]
            for edge in node.edges():
                if edge.value() == letter:
                    recursive_add(edge.dest_node(), word_remainder[1:])
                    return
            new_edge = Edge()
            new_edge.value(letter)
            new_node = Node()
            new_edge.dest_node(new_node)
            node.add_edge(new_edge)
            recursive_add(new_node, word_remainder[1:])

        for word in words:
            first_letter = word[0]
            found = False
            for edge in self.__root.edges():
                if edge.value() == first_letter:
                    found = True
                    recursive_add(edge.dest_node(), word[1:])
                    break
            if not found:
                new_root_edge = Edge()
                new_root_edge.value(first_letter)
                new_root_node = Node()
                new_root_edge.dest_node(new_root_node)
                self.__root.add_edge(new_root_edge)
                recursive_add(new_root_node, word[1:])
        return True

    def to_string(self):
        """Returns the trie as a string adjacency list in the format
        [from_node]->[to_node]:[edge_value] """

        def to_list(node, print_list):
            """Recursive helper method for printing the trie as an adjacency
            list"""
            if len(node.edges()) == 0:
                return
            for edge in node.edges():
                print_list.append("{0}->{1}:{2}".format(node.id(),
                                                        edge.dest_node().id(),
                                                        edge.value()))
                to_list(edge.nodes()[1], print_list)

        trie_list = []
        for edge in self.__root.edges():
            trie_list.append("0->{0}:{1}".format(edge.dest_node().id(),
                                                 edge.value()))
            to_list(edge.nodes()[1], trie_list)
        return "\n".join(trie_list)


class SuffixTree(object):
    """Uses the Trie class above to construct and compress a suffix trie
    into a suffix tree. It's constructor takes a string and turns it into a
    list of words, then populates the trie
    accordingly"""

    def __init__(self, text):
        if text.find("$") == -1:
            text += "$"
        words = []
        for i in range(len(text)):
            words.append(text[i:])
        self.__trie = Trie()
        self.populate(words)

    def populate(self, words):

        def recursive_add(node, remainder):
            split = False
            found = False
            for edge in node.edges():
                substring = remainder[0]
                if edge.value().startswith(substring):
                    found = True
                    i = 0
                    for i in range(1, len(edge.value())):
                        substring += remainder[i]
                        if edge.value().startswith(substring):
                            continue
                        split = True
                        edge_part_1 = edge.value()[0:i]
                        edge_part_2 = edge.value()[i:]
                        edge_part_3 = remainder[i:]
                        edge.value(edge_part_1)
                        edge1 = Edge()
                        edge1.value(edge_part_2)
                        edge2 = Edge()
                        edge2.value(edge_part_3)
                        edge.dest_node().add_edge(edge1)
                        edge.dest_node().add_edge(edge2)
                        break
                    if split:
                        break
                    if len(word) > len(edge.value()):
                        recursive_add(edge.dest_node(), remainder[i:])
                        break

            if not found:
                new_edge = Edge()
                new_edge.value(remainder)
                new_node = Node()
                new_edge.dest_node(new_node)
                node.add_edge(new_edge)

        for word in words:
            root_split = False
            root_found = False
            for root_edge in self.__trie.root().edges():
                root_substring = word[0]
                if root_edge.value().startswith(root_substring):
                    root_found = True
                    root_i = 0
                    for root_i in range(1,len(root_edge.value())):
                        root_substring += word[root_i]
                        if root_edge.value().startswith(root_substring):
                            continue
                        root_split = True
                        root_edge_part_1 = root_edge.value()[0:root_i]
                        root_edge_part_2 = root_edge.value()[root_i:]
                        root_edge_part_3 = word[root_i:]
                        root_edge.value(root_edge_part_1)
                        root_edge1 = Edge()
                        root_edge1.value(root_edge_part_2)
                        root_edge2 = Edge()
                        root_edge2.value(root_edge_part_3)
                        root_edge.dest_node().add_edge(root_edge1)
                        root_edge.dest_node().add_edge(root_edge2)
                        break
                    if root_split:
                        break
                    if len(word) > len(root_edge.value()):
                        if root_i == 0:
                            root_i += 1
                        recursive_add(root_edge.dest_node(), word[root_i:])
                        break

            if not root_found:
                new_root_edge = Edge()
                new_root_edge.value(word)
                new_root_node = Node()
                new_root_edge.dest_node(new_root_node)
                self.__trie.root().add_edge(new_root_edge)

    def compress_to_tree(self):
        """Takes the suffix trie populated from a string text and compresses
        it into a suffix tree"""

        def retract_edge(node):
            while len(node.edges()) == 1:
                # Get the value of the edge

                # Prepend the value to the next edge if it exists

                #
                prefix = node.edges()[0].value()
                node.edges()[0].value(prefix + node.edges()[0].value())
                node.edges()[0].dest_node(node.edges()[0].dest_node()
                                          .edges()[0].dest_node())
                node = node.edges()[0].dest_node()

        def compress(node):
            """Helper method for compressing the suffix trie to a suffix tree"""
            if len(node.edges()) == 0:
                return
            if len(node.edges()) == 1:
                retract_edge(node)
            for edge in node.edges():
                compress(edge.dest_node())

        for root_edge in self.__trie.root().edges():
            compress(root_edge.dest_node())

    def get_edges_as_list(self):
        """Returns all of the edges in the suffix tree as a list. The list
        will be ordered according to a depth first search"""

        def to_list(node, tree_list):
            if len(node.edges()) == 0:
                return
            for edge in node.edges():
                tree_list.append(edge.value())
                to_list(edge.dest_node(), tree_list)

        suffix_list = []
        to_list(self.__trie.root(), suffix_list)
        return suffix_list

    def get_substrings(self):

        def to_list(node, substring_list, stack):
            found = False
            for edge in node.edges():
                if edge.value().find("$") != -1:
                    if stack and not found:
                        substring_list.append(''.join(stack))
                        found = True
                else:
                    stack.append(edge.value())
                    to_list(edge.dest_node(), substring_list, stack)
                    stack.pop()

        sub_list = []
        s = []
        to_list(self.__trie.root(), sub_list, s)
        return sub_list


################################################################################
# UNIT TESTING
#
def main():
    words = ["ATAGA",
             "ATC",
             "GAT"]
    #trie = Trie(words)
    #print trie.to_string()

    text = "panamabananas"

    stree = SuffixTree(text)
    for suffix in stree.get_edges_as_list():
        print suffix


if __name__ == "__main__":
    main()
