""" Python file that contains the class MyHTMLParser used to read tags from and parse XHTML. """

from html.parser import HTMLParser
import urllib.request

class MyHTMLParser(HTMLParser):
    """ Class that Inherits and passes HTMLParser to read data and tags from XHTML. """

    def __init__(self):
        HTMLParser.__init__(self)
        self.body = False
        self.ip = ""

    def handle_starttag(self, tag, attrs):
        """ Inherited method from HTMLParser. This method is called to handle the start tag of an element. """
        if tag=="body":
            self.body = True

    def handle_endtag(self, tag):
        """ Inherited method from HTMLParser. This method is called to handle the end tag of an element. """
        if tag == "body":
            self.body = False   
            
    def handle_data(self, data):
        """ Inherited method from HTMLParser. This method is called to process data. """
        if self.body:
            self.ip = data
            data_ip = data.split(": ")[-1]
            
        
def show_ip():
    """ Parses and returns the ip address. """
    myparser = MyHTMLParser()
    with urllib.request.urlopen('http://checkip.dyndns.org/') as response:
        html = str(response.read())
    myparser.feed(html)
    xhtmlparser = myparser.ip
    xhtmlparser_ip = xhtmlparser.split(": ")[-1]
    return(xhtmlparser_ip)


if __name__ == "__main__":
    print(show_ip())

