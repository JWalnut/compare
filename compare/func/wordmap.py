# John Walnut
# v 0.2
# Module to hold all of our mapping methods
# 7/30/16

import progressbar
import networkx as nx
from compare.classes import Document
from nltk.corpus import wordnet as wn
import numpy as np
from os import listdir
import matplotlib.pyplot as plt

def synonymList(word): #Helper method to generate a list of synonyms using Princeton's WordNet
    list = []
    setList = wn.synsets(word)
    for set in setList:
        for lem in set.lemma_names():
            list.append(str(lem))
    return list

    #Generates a map of synonyms from the set of words in document "doc"
    #Duplicate matches are ignored
    #Optional progress bar for map generation (default is on).  Quiet option turns off

def generateWordMap(doc, quiet=False, synCount=False):
    i = 0
    map = nx.Graph()
    docSet = set(doc.wordlist)
    if not quiet:
        bar = progressbar.ProgressBar(max_value = len(docSet))
    for word in docSet:
        map.add_edge(word, word)
        synonyms = synonymList(word)
        for syn in synonyms:
            if syn in docSet and not map.has_edge(word, syn):
                map.add_edge(word, syn)
        i += 1
        if not quiet:
            bar.update(i)            
    return map

    #Generates a markov matrix from the word map generated in the method above

def generateMarkov(theMap):
    adj = np.asarray(nx.adjacency_matrix(theMap).todense())
    adj = (adj + adj.transpose())/2
    N = len(theMap)
    arrayOfOnes = np.ones([N,1])
    rowSums = adj.dot(arrayOfOnes)
    diagonal = np.diag(rowSums.transpose()[0])
    markov = np.linalg.inv(diagonal).dot(adj)
    return markov

    #Generates a vertical vector of the frequency of occurrance in allWords of each word in document
    #If parameter "count" is true, the vector contains the actual frequence (i.e., if "test" appears three times, its entry will be "3")
    #If parameter "count" is false, the vector ignores duplicate occurances (i.e., "test"'s entry would be "1")
    #The order of the words appearing in the returned vector will match the order of the words appearing in allWords.wordlist
def generateDocumentVector(allWords, document, count=False):
    totalWords = list(set(allWords.wordlist))
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

    #Compares two documents using wordmap. Returns similarity measure
    #Depth determines how many times the document vectors are multiplied by the markov matrix (0 = once)
    #Quiet determines whether wordmap generation should show progress bar
    #Count determines whether word vectors should count words, or indicate presence alone
def compareDocs(doc1, doc2, depth=0, quiet=False, count=False, synCount=False):
    markovDoc = Document(body=doc1.body+" "+doc2.body)
    markovMap = generateWordMap(markovDoc, quiet, synCount)
    markov = generateMarkov(markovMap)
    doc1vec = generateDocumentVector(markovDoc, doc1, count)
    doc2vec = generateDocumentVector(markovDoc, doc2, count)
    doc1vec /= np.sum(doc1vec)
    doc2vec /= np.sum(doc2vec)
    S1 = markov.dot(doc1vec)
    S2 = markov.dot(doc2vec)
    for i in range(int(depth)):
        S1 = markov.dot(S1)
        S2 = markov.dot(S2)            
    return np.sum(np.absolute(S1.transpose()[0] - S2.transpose()[0]))
        
    #Compares all documents in a given folder, outputting a matrix of their similarities
def compareFolderDocs(folder, depth=0, quiet=False, drawMap=False, count=False, synCount=False):
    doclist = [];
    allBody = [];
    allDocs = listdir(folder)
    N = len(allDocs)
    allDist = np.zeros([N,N])
    allBody = " "
    for i in range(N):
        iFile = open(folder+"/"+allDocs[i],"r")
        iBody = iFile.read()
        doclist.append(Document(body=iBody,title=allDocs[i]))
        allBody = allBody+" "+iBody
    markovDoc = Document(body=allBody)
    markovMap = generateWordMap(markovDoc, quiet, synCount)
    if (drawMap):
        plt.plot(nx.draw_networkx(markovMap,show_labels=1))
        plt.show()
    markov = generateMarkov(markovMap)
    for i in range(N):
        for j in range(i+1,N):
            docivec = generateDocumentVector(markovDoc, doclist[i], count)
            docjvec = generateDocumentVector(markovDoc, doclist[j], count)
            docivec /= np.sum(docivec)
            docjvec /= np.sum(docjvec)
            S1 = markov.dot(docivec)
            S2 = markov.dot(docjvec)
            for k in range(int(depth)):
                S1 = markov.dot(S1)
                S2 = markov.dot(S2)            
            allDist[i,j] = np.sum(np.absolute(S1.transpose()[0] - S2.transpose()[0]))
            allDist[j,i] = allDist[i,j]
    return allDist
