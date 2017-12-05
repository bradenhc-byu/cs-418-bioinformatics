from C09_SuffixTreeConstruction import help
import help as h
import os


################################################################################
# UNIT TEST
#
def main():
    filename = "dataset.txt"
    if os.path.exists(filename):
        inf = open(filename, "r")
        text1 = inf.readline().rstrip()
        text2 = inf.readline().rstrip()
        inf.close()
        stree1 = help.GeneralizedSuffixTree(text1)
        stree2 = help.GeneralizedSuffixTree(text2)
        substrings1 = []
        substrings2 = []
        node_num = 0
        try:
            while True:
                string = stree1.node_substring(node_num)
                if '$' not in string:
                    substrings1.append(string)
                node_num += 1
        except:
            print substrings1

        node_num = 0
        try:
            while True:
                string = stree2.node_substring(node_num)
                if '$' not in string:
                    substrings2.append(string)
                node_num += 1
        except:
            print substrings2

        longest = ""
        for substring1 in substrings1:
            for substring2 in substrings2:
                if substring1 == substring2:
                    if longest == "":
                        longest = substring1
                    elif len(substring1) > len(longest):
                        longest = substring1
                        break
        longest = h.lcs("\n".join([text1, text2]))
        print longest


if __name__ == "__main__":
    main()