from C09_SuffixTreeConstruction import help
import os


################################################################################
# UNIT TEST
#
def main():
    filename = "dataset.txt"
    if os.path.exists(filename):
        inf = open(filename, "r")
        text = inf.readline().rstrip()
        inf.close()
        stree = help.GeneralizedSuffixTree(text)
        longest = ""
        node_num = 0
        try:
            while True:
                string = stree.node_substring(node_num)
                if '$' not in string:
                    if len(string) > len(longest):
                        longest = string
                node_num += 1
        except:
            print longest


if __name__ == "__main__":
    main()