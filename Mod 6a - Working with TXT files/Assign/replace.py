""" This module reads and replaces a word then overwrites the file with the new word in it. """

textfile = "colours.txt"

def read_replace_file(textfile):
    """ Reads and replaces the specific word indicated. """
    textfile_read = open(textfile, 'r')
    with textfile_read as colour_file:
        readinglines = colour_file.read()
        updatedlines = readinglines.replace("Aqua #00ffff","Azure #007fff")
        print(updatedlines)
    return updatedlines

def overwrite_file(textfile, replacedlines):
    """ Overwrites the content with the new word. """
    textfile_write = open(textfile, 'w')
    with textfile_write as colour:
        colour.write(replacedlines)
    textfile_write.close()

read_replace_file(textfile)
replacedlines = read_replace_file(textfile)
print(replacedlines)
overwrite_file(textfile, replacedlines)

