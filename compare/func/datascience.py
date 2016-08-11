# John Walnut
# v 0.1
# To contain the data science methods (PCA and MMDS)
# 8/2/16

import numpy.linalg as np
import numpy

# pca based on the covariance matrix
def pca(simMatrix, k=1):
    #Center the matrix
    simMatrix = simMatrix - simMatrix.mean(axis=0)
    #Calculate covariance matrix
    cov = numpy.cov(simMatrix.T)
    #Singular value decomposition
    S,U = np.eig(cov)
    #Compute percentage of variance in each principal component
    S = S/sum(S)
    #Pull eigenvectors (number depends on "k"
    evecs = U[:, 0:k]
    Z = evecs.T.dot(simMatrix.T)
    return Z,S

# pca based on the covariance matrix
def svdpca(data, k=1):
    #Center the matrix
    data = data - data.mean(axis=0)
    #Singular value decomposition
    U,S,V = np.svd(data.T)
    #Compute percentage of variance in each principal component
    S = S*S/data.shape[0]
    S = S/sum(S)
    #Pull eigenvectors (number depends on "k"
    evecs = U[:, 0:k]
    Z = evecs.T.dot(data.T)
    return Z, S

def mmds(matrix):
    return 0