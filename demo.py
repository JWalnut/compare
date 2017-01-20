from compare.func import wordmap as wm
from compare.classes import Document
from compare.classes import Corpus
from compare.func import datascience as sci
import numpy
import math
from compare.func import graphics

#tests the pca function on data from Lindsay Smith's "Tutorial on Principal Component Analysis"
#x = numpy.array([[0.0, 3.47, 1.79, 3.0, 2.67, 2.58, 2.22, 3.08],
#                 [3.47, 0.0, 3.39, 2.18, 2.86, 2.69, 2.89, 2.62],
#                 [1.79, 3.39, 0.0, 2.18, 2.34, 2.09, 2.31, 2.88],
#                 [3.00, 2.18, 2.18, 0.0, 1.73, 1.55, 1.23, 2.07],
#                 [2.67, 2.86, 2.34, 1.73, 0.0, 1.44, 1.29, 2.38],
#                 [2.58, 2.69, 2.09, 1.55, 1.44, 0.0, 1.19, 2.15],
#                 [2.22, 2.89, 2.31, 1.23, 1.29, 1.19, 0.0, 2.07],
#                 [3.08, 2.62, 2.88, 2.07, 2.38, 2.15, 2.07, 0.00]])

numpy.seterr(all="print")
rt = 1/math.sqrt(2)
y = numpy.array([[-1*rt, 0],[0, rt], [0, -1*rt], [rt, 0]])
graphics.plotCoordinatesMatrix(y)
dist = sci.generateDistanceMatrix(y)
dist = numpy.sqrt(dist)
y = sci.mmds(dist)
graphics.plotCoordinatesMatrix(y)
