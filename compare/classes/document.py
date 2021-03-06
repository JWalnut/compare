# John Walnut
# v 0.3
# Document class will wrap any document we want to compare
# 7/24/16

from collections import namedtuple
import string
import  platform
MetaData = namedtuple("MetaData", "title length wordcount") #Python equivalent of C-Style "struct" for metadata.  Requires separate "import" to use on its own

class Document:

    # Constructors
    def __init__(self, file = "", title = "Untitled", body = ""):

        #Fields
        if not file == "": #If filename is provided, create document from file (will only work with plain text files)
            self.body = open(file, "r").read()
            if title == "Untitled": #If not given title directly, set title to filename (sans extension)
                delim = "/"
                if platform.system() == "Windows": #Handling windows using backslash instead of forward slash for file paths
                    delim = "\\"
                tmp = open(file, "r").name.split(delim) #Pull file name from file path
                self.title = tmp[len(tmp)-1].split(".")[0] #Remove file extension and set title
        else:
            self.body = body
            self.title = title

        self.length = len(body)
        self.wordlist = self.body.translate(None, "~`!@#$%^&*()_+={}[]|;:\"\'<,>.?/\n\\").split(" ") #To be used to get wordcount, and for easy access to individual words.
        self.totalSubstrings = -1 #This for substring generation methods, deprecated as of v0.2

        #Metadata
        self.meta = MetaData(title = self.title, length = self.length, wordcount = len(self.wordlist))

    ### TODO: Copy constructor


    # Magic Methods
    def __str__(self):
        return self.body
    
    def __eq__(self, other):
        return (self.title == other.title) and (self.length == other.length)

    ### TODO: Other magic methods (comparison?, formatting?)


    # Other Methods

    def toLowerCase(self): #Converts entire document to lowercase
        self.body = self.body.lower()
        newWordList = []
        for word in self.wordlist:
            newWordList.append(word.lower())
        self.wordlist = newWordList
    
    # Deprecated Methods
    def generateConsecutiveSubstring(self, subLength = 5): #This method deprecated as of v0.2
        # v 0.1
        # currently generates consecutive strings (that is, with no interior characters)
        
        # todo: account for multiple calls with different subLength arguments

        if self.totalSubstrings == -1:
            self.totalSubstrings = self.length - subLength
        elif self.totalSubstrings == 0:
            return ""
        else:
            self.totalSubstrings -= 1
        
        total = self.length - subLength
        startingChar = total - self.totalSubstrings

        return self.body[startingChar:startingChar + subLength]
    
    def generateSubstring(self, subLength = 5): #This method deprecated as of v0.2
        # v 0.1
        # this is the more correct substring generator.  I left the old one intact, in case we wanted to use it later
        print("test")

    def resetSubstring(self): #This method deprecated as of v0.2
        self.totalSubstrings = -1
