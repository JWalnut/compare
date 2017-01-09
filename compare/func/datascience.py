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
    #Calculate eigenvectors and eigenvalues of the covariance matrix
    eVal,eVec = np.eig(cov)
    #Sort eigenvectors by eigenvalues
    indexArray = numpy.argsort(eVal)
    evecs = numpy.zeros_like(eVec)
    i=0
    for value in numpy.nditer(indexArray):
        evecs[:, evecs.shape[0]-1-value] = eVec[:, i]
        i += 1
    #Pull eigenvectors (number depends on "k") & evaluate
    evecs = evecs[:, 0:k]
    Z = evecs.T.dot(simMatrix.T)
    return Z.T,numpy.sort(eVal)[::-1]

# pca based on the singular value decomposition
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

def mmds(matrix, k=1):
    
