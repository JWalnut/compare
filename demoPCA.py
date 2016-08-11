from compare.func import datascience as ds
import numpy.linalg as la
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.gca(projection='3d')

# create 100 random points inside a 2-dimensional square
X = np.random.random([2,100])

# create 100 points on a grid in a 2-dimensional square
x,y = np.mgrid[-2:2:10j,-1:1:10j]
X = [np.reshape(x,[100,1]), np.reshape(y,[100,1])]
X = np.reshape(X,[2,100])

# plot the 'hidden' data points in blue
ax.scatter(X[0],X[1],np.zeros([1,100]),marker='.',c='b',edgecolor='b')

# create a random matrix which maps 2-dimensional space into 10-dimensional space
A = np.random.random([10,2])
# convert A into an orthogonal matrix
A,R = la.qr(A)

# map the hidden data (X) to the observed data (Y) and add small noise
Y = A.dot(X) + np.random.random([10,100])/50

# plot the first 3 coordinates of the 'observed' data in green
ax.scatter(Y[0],Y[1],Y[2],marker='.',c='g',edgecolor='g')

# Two equivalent formulations of PCA
Xpca,S = ds.pca(Y.T,k=3);
#Xpca,S = ds.svdpca(Y.T,k=3);

print(S)[0:3]

# use "c" option for setting the face color, use "depthshade=False" to turn off 3d shading
# plot the PCA results, should be right on top of the 'hidden' data
ax.scatter(Xpca[0],Xpca[1],Xpca[2],c='None',marker='o',edgecolor='r',s=50)

plt.show()



