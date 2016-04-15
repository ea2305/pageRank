""" Class to get number of links into HTML document """
## author : Elihu A. Cruz Ablores
##  version : 1.1

from Information import Information
import re ## REgular expresion object

class ReadPage(object):

    currentFile = ""

    """docstring for ReadPage """
    def __init__(self, directory = ""):
        self.currentFile = directory

    # no parameters
    #return, Information : Object
    def countLinks(self,directory = currentFile):

        #Read file and set values into fileContent
        fileContent = open(self.currentFile)

        #count elements
        count = 0# general references
        itSelf = 0# same link to set in constructor
        listOfLinks = []

        ##process file information
        for line in fileContent:

            match = re.search(r'<a[.* ]href=".*">.*</a>',line)

            if match:
                #if contents <a> tag search href in tag
                link = re.search(r'href=".+"',line);

                #search link and compare if doesn't be the same page
                href = link.group()
                if href[6:-1] == self.currentFile:
                    itSelf += 1

                count += 1
                listOfLinks.append(link) # add link into list

        ## Return an object with all data
        return Information(count,itSelf,listOfLinks)

    #set value to search
    def setFile(self,directory):
        self.currentFile = directory
