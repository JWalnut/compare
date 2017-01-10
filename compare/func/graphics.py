# John Walnut
# v 0.1
# To provide easy methods to visualize matrix data
# 1/10/17

import numpy
import matplotlib.pyplot as plt

def plotCoordinatesMatrix(matrix):
    pertinentDimensions = 2
    if (len(matrix.shape) > 2):
        print "Matrix is ", len(matrix.shape), " dimensional.  Pulling only first 2 dimensions."
    matrix = matrix[:, 0:pertinentDimensions]
    xDim = matrix[:, 0:1].T
    yDim = matrix[:, 1:2].T
    print xDim, "\n", yDim
    plt.plot(xDim, yDim, 'ro')
    plt.axis([-6, 6, -4, 4])
    plt.show()
