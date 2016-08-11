# John Walnut
# v 0.1
# To contain the data science methods (PCA and MMDS)
# 8/2/16

import numpy.linalg as np
import numpy

def pca(simMatrix, k=1):
    #Center the matrix
    simMatrix = simMatrix - simMatrix.mean(axis=0)
    #Calculate covariance matrix
    cov = numpy.cov(simMatrix.T)
    #Singular value decomposition
    x1, x2, U = np.svd(cov)
    #Pull eigenvectors (number depends on "k"
    evecs = U[:, 0:k]
    Z = evecs.T.dot(simMatrix.T)
    return Z

def mmds(matrix):
    
