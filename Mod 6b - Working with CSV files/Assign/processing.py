"""
    This module contains class and functions that opens and reads the file air.csv for manipulation.
    Manipulated data inside air.csv is written on a new file.
"""


class OpenFile(object):
    """ Class that opens the file then automatically closes and cleans up when done. """
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.open_files = open(filename, mode)
    def __enter__(self):
        return self.open_files
    def __exit__(self, type, value, trace):
        self.open_files.close()


import csv

def csv_reader(filename):
    """ Reads the csv file. """
    data = []
    with OpenFile(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            data.append(dict(line))
    for item in data:
        for k, v in item.items():
            item[k]= float(v) * 2
                    
    return data

def csv_writer(filename, alist):
    """ Writes the new  data into a new csv file. """
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Temp', 'Press', 'Humidity']
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writeheader()
        for item in alist:
            writer.writerow(item)
                


airquality = csv_reader('air.csv')
csv_writer('air_new.csv', airquality)
