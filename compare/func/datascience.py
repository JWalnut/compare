# John Walnut
# v 0.1
# To contain the data science methods (PCA and MMDS)
# 8/2/16

import numpy.linalg as np
import numpy

def pca(simMatrix, k=0):
    # Center Data
    #mean = simMatrix.mean(axis=0)
    #print "Means = ", mean
    #simMatrix = simMatrix - mean
    #print "Centered = ", simMatrix
    #U, s, V = np.svd(simMatrix)
    #print "Eigenvectors = ", U
    #U_k = V[:, 0:k+1]
    #print "1st Eigenvector = ", U_k
    #X = U_k.transpose()
    #X = X.dot(simMatrix.transpose())
    #print "X = ", X
    #Z = U_k.dot(X)
    #print "Z = ", Z
    #return Z
    
    simMatrix = simMatrix - simMatrix.mean(axis=0)
    cov = numpy.cov(simMatrix.T)
    x1, x2, U = np.svd(cov)
    evecs = U[:, 0:k+1]
    Z = evecs.T.dot(simMatrix.T)
    return Z
