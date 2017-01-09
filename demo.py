from compare.func import wordmap as wm
from compare.classes import Document
from compare.classes import Corpus
from compare.func import datascience as sci
import numpy

#tests the pca function on data from Lindsay Smith's "Tutorial on Principal Component Analysis"
x = numpy.array([[0, 3.47, 1.79, 3.00, 2.67, 2.58, 2.22, 3.08],
                 [])
x = x.T

pcaMatrix,eVals = sci.pca(x)

print pcaMatrix
print eVals
