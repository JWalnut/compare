from compare.func import wordmap as wm
from compare.classes import Document
from compare.classes import Corpus

myCP = Corpus("LegalDocs")

print(myCP.compareCorpus())

# doc = Document("test.txt")
A = wm.compareFolderDocs("LegalDocs",quiet=True)

print(A)

