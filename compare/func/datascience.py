# John Walnut
# v 0.1
# To contain the data science methods (PCA and MMDS)
# 8/2/16

import numpy.linalg as np
import numpy
import math

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

def generateDistanceMatrix(matrix):
    dmat = numpy.zeros_like(matrix.reshape(matrix.shape[0], matrix.shape[0]))
    for i in range(0, matrix.shape[0]-1):
        for j in range(i+1, matrix.shape[0]):
            sum = 0
            for k in range(0, matrix.shape[1]):
                sum += math.pow((matrix[i, k] - matrix[j, k]), 2)
            dmat[i, j] = sum
            dmat[j, i] = sum
    return dmat

def isSymmetric(matrix):
    for i in range(0, matrix.shape[1]):
        for j in range(0, i+1):
            if (matrix[j,i] != matrix[i,j]):
                return False
    return True

def mmds(distanceMatrix):
    print "Distance Matrix\n", distanceMatrix
    size = float(distanceMatrix.shape[0])
    #Create the Gram matrix from the distance matrix
    massVector = numpy.full((1, size), (1/size))
    print "\n\nmassVector\n", massVector
    centerMatrix = numpy.identity(size) - numpy.ones((size, 1)).dot(massVector)
    print "\n\ncenterMatrix\n", centerMatrix
    gramMat = (-0.5)*centerMatrix.dot(distanceMatrix).dot(centerMatrix)
    print "\n\ngramMatrix\n", gramMat
    #Perform eigen-decomposition
    eVals,eVecs = np.eig(gramMat)
    print "\n\neigenVectors\n", eVecs
    #Create diagonal matrix of eigenvalues
    lambd = numpy.diag(eVals)
    print "\n\nlambd\n", lambd
    lambd = numpy.sqrt(lambd)
    print "\n\nlambd^(1/2)\n", lambd
    #Create euclidean points matrix
    #scoresMat = numpy.identity(gramMat.shape[0], distanceMatrix.shape[0])
    scoresMat = lambd
    scoresMat = scoresMat.dot(distanceMatrix.T)
    #print "\n\n"
    return scoresMat
