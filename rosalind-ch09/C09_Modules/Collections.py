########################################################################################################################
# Suffix Arrays
#


class SuffixArray(object):
    """
    Represents a suffix array
    """

    def __init__(self, text):
        """
        Class constructor. Creates a suffix array, sorting it lexicographically

        :param text: The text word to use in constructing this array
        """
        if text.find("$") == -1:
            text += "$"
        self.__suffixes = []
        for i in range(len(text)):
            self.__suffixes.append((i, text[i:]))
        alphabet = "$abcdefghijklmnopqrstuvwxyz"
        self.__suffixes.sort(key=lambda x: [alphabet.index(c) for c in x[1].lower()])

    def get_suffix_indices(self):
        return [index for index, suffix in self.__suffixes]

    def get_suffixes(self):
        return [suffix for index, suffix in self.__suffixes]

    def find(self, pattern, first=False):
        matching_indices = []
        for index, suffix in self.__suffixes:
            if suffix.startswith(pattern):
                matching_indices.append(index)
                if first:
                    return matching_indices[0]
        return matching_indices
