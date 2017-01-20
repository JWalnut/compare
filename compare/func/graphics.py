# John Walnut
# v 0.1
# To provide easy methods to visualize matrix data
# 1/10/17

import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#takes in matrix where rows are points and columns are coordinates
#uses only two leftmost columns for 2-d graphing
def plot(matrix, dimensions=2):
    xDim = matrix[:, 0:1].T
    yDim = matrix[:, 1:2].T
    if (dimensions == 3):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        zDim = matrix[:, 2:3].T
        print xDim, "\n", yDim, "\n", zDim, "\n"
        plt.scatter(xDim, yDim, zs=zDim)
        ax.set_xlim3d(-1*numpy.amax(xDim) - 1.5, numpy.amax(xDim) + 1.5)
        ax.set_ylim3d(-1*numpy.amax(yDim) - 1.5, numpy.amax(yDim) + 1.5)
        ax.set_zlim3d(-1*numpy.amax(zDim) - 1.5, numpy.amax(zDim) + 1.5)
        plt.show()
    else:
        plt.plot(xDim, yDim, 'ro')
        plt.axis([-1*numpy.amax(xDim) - 1.5, numpy.amax(xDim) + 1.5, -1*numpy.amax(yDim) - 1.5, numpy.amax(yDim) + 1.5])
        plt.show()
