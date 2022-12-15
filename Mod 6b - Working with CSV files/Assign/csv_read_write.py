import csv


class OpenFile():
    """ Class that opens the file then automatically closes and cleans up when done. """
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.open_files = open(filename, mode)
    def __enter__(self):
        return self.open_files
    def __exit__(self, type, value, trace):
        self.open_files.close()

def csv_read(file):
    with open(file) as target_file:
        for line in csv.DictReader(target_file):
            print(line)