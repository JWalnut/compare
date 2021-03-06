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
    #Pull eigenvectors (number depends on "k")
    evecs = U[:, 0:k]
    Z = evecs.T.dot(data.T)
    return Z, S

# function to create a distance matrix from a matrix of points
def generateDistanceMatrix(matrix):
    dmat = numpy.zeros((matrix.shape[0], matrix.shape[0]))
    for i in range(0, matrix.shape[0]-1):
        for j in range(i+1, matrix.shape[0]):
            sum = 0
            for k in range(0, matrix.shape[1]):
                sum += math.pow((matrix[i, k] - matrix[j, k]), 2)
            dmat[i, j] = sum
            dmat[j, i] = sum
    return dmat

# removes values smaller than tolerance from matrix
def removeArtifacts(matrix, tolerance=float(10e-10)):
    if (len(matrix.shape) == 1):
        for i in range(0, matrix.size):
            if (math.fabs(matrix[i]) < tolerance):
                matrix[i] = 0
    else:
        for i in range(0, matrix.shape[0]):
            for j in range(0, matrix.shape[1]):
                if (math.fabs(matrix[i,j]) < tolerance):
                    matrix[i,j] = 0
    return matrix

# checks if matrix is symmetric (i.e., is a valid distance array)
def isSymmetric(matrix):
    for i in range(0, matrix.shape[1]):
        for j in range(0, i+1):
            if (matrix[j,i] != matrix[i,j]):
                return False
    return True

# performs eigenvalue decomposition on matrix, and sorts the eigenvectors by their eigenvalues (from largest to smallest)
def orderedEig(matrix, labelsMatrix = None, stripNegatives = True):
    eVals,eVecs = np.eig(matrix)
    eVals = removeArtifacts(eVals)
    eVecs = removeArtifacts(eVecs)
    
    posEVals = []
    for i in range(0, eVals.size):
        if (stripNegatives == True and eVals[i] > 0):
            posEVals.append(eVals[i])
    
    print posEVals
    posEVals = numpy.array(posEVals)
    indexArray = list(numpy.argsort(posEVals))[::-1]

    evecs = numpy.zeros((eVecs.shape[0], posEVals.size))
    evals = numpy.zeros_like(posEVals)

    i=0
    for value in indexArray:
        evecs[:, i] = eVecs[:, value]
        evals[i] = posEVals[value]
        i += 1
    return evals,evecs
    
# performs metric multidimensional scaling on a distance matrix
def mmds(distanceMatrix):
    distanceMatrix = numpy.square(distanceMatrix)
    pointsCount = float(distanceMatrix.shape[0])
    centeringMatrix = numpy.identity(pointsCount) - (1/pointsCount)*numpy.ones((pointsCount, pointsCount))

    gramMatrix = (-0.5)*centeringMatrix.dot(distanceMatrix).dot(centeringMatrix)
    gramMatrix = removeArtifacts(gramMatrix)

    eVals,eVecs = orderedEig(gramMatrix)
    eVals = removeArtifacts(eVals)
    eVecs = removeArtifacts(eVecs)

    lambdaMatrix = numpy.diag(eVals)
    print lambdaMatrix
    rootLambdaMatrix = numpy.sqrt(lambdaMatrix)
    
    return rootLambdaMatrix.dot(eVecs.T).T
