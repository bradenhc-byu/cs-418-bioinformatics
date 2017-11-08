import os


def import_data(filename):
    if os.path.exists(filename):
        words = list()
        with open(filename,"r") as input_file:
            for line in input_file:
                words.append(line.strip())
            input_file.close()
        return words
    return None
