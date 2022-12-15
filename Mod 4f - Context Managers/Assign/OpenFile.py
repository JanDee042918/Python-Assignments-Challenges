""" File that contains the class OpenFile used with open and close file setup. """

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
