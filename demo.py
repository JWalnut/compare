from compare.func import wordmap as wm
from compare.classes import Document

# doc = Document("test.txt")
A = wm.compareFolderDocs("LegalDocs",quiet=True)

print(A)