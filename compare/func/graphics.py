# John Walnut
# v 0.1
# To provide easy methods to visualize matrix data
# 1/10/17

import numpy
import matplotlib.pyplot as plt

#takes in matrix where rows are points and columns are coordinates
#uses only two leftmost columns for 2-d graphing
def plot(matrix):
    xDim = matrix[:, 0:1].T
    yDim = matrix[:, 1:2].T
    plt.plot(xDim, yDim, 'ro')
    plt.axis([-6, 6, -4, 4])
    plt.show()
