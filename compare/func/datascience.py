# John Walnut
# v 0.1
# To contain the data science methods (PCA and MMDS)
# 8/2/16

import numpy.linalg as np

def pca(simMatrix, k=0):
    U, s, V = np.svd(simMatrix)
    print "U = ", U
    U_k = U[:, 0:k+1]
    print "U_k = ", U_k
    X = U_k.transpose().dot(simMatrix)
    print "X = ", X
    Z = U_k.dot(X)
    print "Z = ", Z
    return Z
