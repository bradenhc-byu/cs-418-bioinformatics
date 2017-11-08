import os


class Data:

    def __init__(self):
        self.text = ""
        self.words = list()


def import_data(filename):
    if os.path.exists(filename):
        data = Data()
        with open(filename, "r") as input_file:
            data.text = input_file.readline().strip()
            for line in input_file:
                data.words.append(line.strip())
            input_file.close()
        return data
    return None
