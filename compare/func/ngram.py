# John Walnut
# v 0.2
# Contains all methods and code for comparing two documents
# 7/8/16

from compare.classes import Document
import math

    @staticmethod
    def calculatePrimeLength(substring, document): #calculates to end of document (I'm calling it l'(s))
        # todo: incorrect type handling
        finalLength = document.length
        first = substring[:1]
        firstIndex = document.body.rfind(substring[:1])
        if firstIndex == -1:
            return 0
        nextIndex = firstIndex+1
        nextChar = 1
        while nextChar < len(substring):
            tmp = document.body.rfind(substring[nextChar:nextChar+1], nextIndex)
            if tmp == -1:
                return 0
            nextChar += 1
        return document.length - firstIndex + 1

    @staticmethod
    def calculateLength(substring, document): #calculates to end of substring (l(s) as in paper)
        # todo: incorrect type handling
        finalLength = document.length
        first = substring[:1]
        firstIndex = document.body.rfind(substring[:1])
        if firstIndex == -1:
            return 0
        nextIndex = firstIndex+1
        nextChar = 1
        tmp = 0
        while nextChar < len(substring):
            tmp = document.body.rfind(substring[nextChar:nextChar+1], nextIndex)
            if tmp == -1:
                return 0
            nextChar += 1
        return tmp - firstIndex + 1

    @staticmethod
    def K_Prime(doc1, doc2, n, lambd = 0.5):
        #print "K'_", n, "(\"", doc1.body, "\",\"", doc2.body, "\")"

        #Total to return later
        total = 0.0

        #Base Cases
        if n == 0:
            return 1
        if min(doc1.length, doc2.length) < n:
            return 0
       
        #First Recursive Call
        doc_s = Document(body = doc1.body[:doc1.length-1]) #Peel last character off of "S"
        total += lambd*Compare.K_Prime(doc_s, doc2, n, lambd)

        #Second Recursive Call
        lastchar = doc1.body[doc1.length-1:] #Grab last character of "S"
        charIndex = doc2.body.find(lastchar) #Find that character in "T"
        while charIndex != -1: #For every instance of the last character of "S" found in "T"...
            doc_t = Document(body = doc2.body[:charIndex]) #Grab "T" up to (but not including) that character
            total += math.pow(lambd, doc2.length - charIndex + 1)*Compare.K_Prime(doc_s, doc_t, n-1, lambd) #Call K_Prime at one less level of "n"
            charIndex = doc1.body.find(lastchar, charIndex+1, doc1.length) #Find next occurance of character in "T"
        #print "Recursion on K'_", n, "(\"", doc1.body, "\",\"", doc2.body, "\") complete!  Total += ", total
        return total

    @staticmethod
    def K(doc1, doc2, n, lambd=0.5):
        
        #Total to return later
        total = 0.0

        #Base Cases
        if n == 0:
            return 1
        if min(doc1.length, doc2.length) < n:
            return 0
       
        #First Recursive Call
        doc_s = Document(body = doc1.body[:doc1.length-1]) #Peel last character off of "S"
        total += Compare.K(doc_s, doc2, n, lambd)

        #Second Recursive Call
        lastchar = doc1.body[doc1.length-1:] #Grab last character of "S"
        charIndex = doc2.body.find(lastchar) #Find that character in "T"
        while charIndex != -1: #For every instance of the last character of "S" found in "T"...
            doc_t = Document(body = doc2.body[:charIndex]) #Grab "T" up to (but not including) that character
            total += math.pow(lambd, 2)*Compare.K_Prime(doc_s, doc_t, n-1, lambd) #Call K_Prime at one less level of "n"
            charIndex = doc1.body.find(lastchar, charIndex+1, doc1.length) #Find next occurance of character in "T"
       # print "Recursion on K'_", n, "(\"", doc1.body, "\",\"", doc2.body, "\") complete!  Total += ", total
        return total
