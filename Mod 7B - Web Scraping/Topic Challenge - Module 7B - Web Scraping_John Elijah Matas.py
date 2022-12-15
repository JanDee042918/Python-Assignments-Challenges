""" Python file that contains the class MyHTMLParser used to read tags from and parse XHTML. 
    This will get the colors and their hex codes.
"""

from html.parser import HTMLParser
import urllib.request
from pprint import pprint


class MyHTMLParser(HTMLParser):
    """ Class that Inherits and passes HTMLParser to read data and tags from XHTML. """

    def __init__(self):
        HTMLParser.__init__(self)
        self.body = False
        self.ip = ""
        self.singleQuote = ''
        self.colorDictionary = {}
        self.directory = "/"
        self.hash = "#"
        self.code = False
        self.tags = False

    def handle_starttag(self, tag, attrs):
        """ Inherited method from HTMLParser. This method is called to handle the start tag of an element. """
        self.code = True
        if tag == "td":
            self.tags = True
        if tag == "a":
            for name, value in attrs:
                if name == "class":
                    self.body = True
                if name == "href":
                    self.ip = value          

    def handle_endtag(self, tag):
        """ Inherited method from HTMLParser. This method is called to handle the end tag of an element. """
        if tag == "a":
            self.body = False
            self.code = False
            self.tags = False

    def handle_data(self, data):
        """ Inherited method from HTMLParser. This method is called to process data."""
        if self.body and self.code and self.tags:
            self.colorDictionary.update({data: self.ip.replace(self.directory, self.hash, 1)})
            print(data, self.ip.replace(self.directory, self.hash, 1))


myparser = MyHTMLParser()
with urllib.request.urlopen('https://www.colorhexa.com/color-names') as response:
    page = response.read()
    html = str(page)
myparser.feed(html)
print("Total colors:", len(myparser.colorDictionary))