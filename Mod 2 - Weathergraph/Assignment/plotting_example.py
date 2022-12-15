from requests import get
import matplotlib.pyplot as plt
from dateutil import parser
from pprint import pprint

print('start')

#key value pair:
#key = records, value = a list of dictionaries
#each list item is a dictionary with keys: date, qtr1, qtr2, qtr3 and qtr4
quarterly_data = {'records':[{'date': 2000, 'qtr1': 838, 'qtr2': 1117, 'qtr3': 870, 'qtr4': 739}, 
                             {'date': 2001, 'qtr1': 750, 'qtr2': 1241, 'qtr3': 669, 'qtr4': 655}, 
                             {'date': 2002, 'qtr1': 332, 'qtr2': 43, 'qtr3': 879, 'qtr4': 477}, 
                             {'date': 2003, 'qtr1': 989, 'qtr2': 1212, 'qtr3': 997, 'qtr4': 554},
                             {'date': 2004, 'qtr1': 679, 'qtr2': 3315, 'qtr3': 588, 'qtr4': 767},
                             {'date': 2005, 'qtr1': 906, 'qtr2': 542, 'qtr3': 443, 'qtr4': 763},
                             {'date': 2006, 'qtr1': 334, 'qtr2': 311, 'qtr3': 9897, 'qtr4': 234},
                             {'date': 2007, 'qtr1': 765, 'qtr2': 2121, 'qtr3': 453, 'qtr4': 432},
                             {'date': 2008, 'qtr1': 2345, 'qtr2': 1437, 'qtr3': 345, 'qtr4': 544},
                             {'date': 2009, 'qtr1': 224, 'qtr2': 1000, 'qtr3': 663, 'qtr4': 896},
                             {'date': 2010, 'qtr1': 1345, 'qtr2': 880, 'qtr3': 774, 'qtr4': 123},
                             {'date': 2011, 'qtr1': 654, 'qtr2': 988, 'qtr3': 564, 'qtr4': 878},
                             {'date': 2012, 'qtr1': 23, 'qtr2': 889, 'qtr3': 989, 'qtr4': 221},
                             {'date': 2013, 'qtr1': 767, 'qtr2': 909, 'qtr3': 885, 'qtr4': 945},
                             {'date': 2014, 'qtr1': 874, 'qtr2': 878, 'qtr3': 877, 'qtr4': 909},
                             {'date': 2015, 'qtr1': 443, 'qtr2': 876, 'qtr3': 906, 'qtr4': 123}]}




