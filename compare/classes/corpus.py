# John Walnut
# v 0.3
# Document class will wrap any document we want to compare
# 7/24/16

from collections import namedtuple
import progressbar
import networkx as nx
from os import listdir
import numpy as np
from nltk.corpus import wordnet as wn
from .document import Document
import string
import  platform
MetaData = namedtuple("MetaData", "title length wordcount") #Python equivalent of C-Style "struct" for metadata.  Requires separate "import" to use on its own

class Corpus:

    # Constructors
    def __init__(self, folder = "", title = ""):

        #Fields
        self.doclist = list()
        self.wordlist = list()
        self.corpuswordmap = nx.Graph()
        self.markov = []
        if not folder == "": #If filename is provided, create document from file (will only work with plain text files)
            self.addfolder(folder)
            if title == "": #If not given title directly, set title to filename (sans extension)
                self.title = folder
        #Metadata
        self.meta = MetaData(title = self.title, length = self.length, wordcount = len(self.wordlist))

    # Magic Methods
    def __str__(self):
        return self.folder
    
    def __eq__(self, other):
        return (self.title == other.title) and (self.folder == other.folder)

    # Other Methods 
    
    def synonymList(self,word): #Helper method to generate a list of synonyms using Princeton's WordNet
        list = []
        setList = wn.synsets(word)
        for set in setList:
            for lem in set.lemma_names():
                list.append(str(lem))
        return list

        
    def generateWordMap(self,quiet=True,synCount=False):
        i = 0
        if len(self.corpuswordmap)==0:
            self.corpuswordmap = nx.Graph()
        if not quiet:
            bar = progressbar.ProgressBar(max_value = len(docSet))
        for word in self.wordlist:
            self.corpuswordmap.add_edge(word, word)
            synonyms = self.synonymList(word)
            for syn in set(synonyms):
                if syn in self.wordlist:
                    if not self.corpuswordmap.has_edge(word, syn):
                        if synCount:
                            self.corpuswordmap.add_edge(word, syn,weight=synonyms.count(syn))  
                        else:
                            self.corpuswordmap.add_edge(word, syn)                           
            i += 1
            if not quiet:
                bar.update(i) 
                
            
    def generateMarkov(self,theMap):
        adj = np.asarray(nx.adjacency_matrix(theMap).todense())
        adj = (adj + adj.transpose())/2
        N = len(theMap)
        arrayOfOnes = np.ones([N,1])
        rowSums = adj.dot(arrayOfOnes)
        diagonal = np.diag(rowSums.transpose()[0])
        markov = np.linalg.inv(diagonal).dot(adj)
        return markov
    
    
    def generateDocumentVector(self, document, count=False):
        totalWords = self.wordlist
        docWords = []
        if count == True:
            docWords = document.wordlist
        else:
            docWords = list(set(document.wordlist))
        vector = np.zeros([len(totalWords),1])
        for i in range(len(totalWords)):
            if docWords.count(totalWords[i]) != -1:
                vector[i][0] = docWords.count(totalWords[i])
        return vector

                
    def addfolder(self,foldertoadd="",quiet=True,drawMap=False, synCount=False):
        if not foldertoadd=="":
            allDocs = listdir(foldertoadd)
            N = len(allDocs)
            delim = "/"
            if platform.system() == "Windows": #Handling windows using backslash instead of forward slash for file paths
                delim = "\\"
            for i in range(N):
                iFile = open(foldertoadd+delim+allDocs[i],"r")
                iDoc = Document(body=iFile.read(),title=allDocs[i])
                iDoc.toLowerCase()
                self.doclist.append(iDoc)
                wordstoadd = set(iDoc.wordlist)
                for word in wordstoadd:
                    word = word.lower()  
                    if word not in self.wordlist:
                        self.wordlist.append(word)
            self.length = len(self.wordlist)
            self.generateWordMap(quiet,synCount)
            if (drawMap):
                plt.plot(nx.draw_networkx(self.corpuswordmap,show_labels=1))
                plt.show()
            self.markov = self.generateMarkov(self.corpuswordmap)
        

    def compareCorpus(self, depth=0, count=False):
        N = len(self.doclist)
        allDist = np.zeros([N,N])
        for i in range(N):
            for j in range(i+1,N):
                docivec = self.generateDocumentVector(self.doclist[i], count)
                docjvec = self.generateDocumentVector(self.doclist[j], count)
                docivec /= np.sum(docivec)
                docjvec /= np.sum(docjvec)
                S1 = self.markov.dot(docivec)
                S2 = self.markov.dot(docjvec)
                for k in range(int(depth)):
                    S1 = self.markov.dot(S1)
                    S2 = self.markov.dot(S2)            
                allDist[i,j] = np.sum(np.absolute(S1.transpose()[0] - S2.transpose()[0]))
                allDist[j,i] = allDist[i,j]
        return allDist