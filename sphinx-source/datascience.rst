datascience
===========

*Yeah, I know the linear algebra.  Eigenvectors, and stuff....*

.. py:module:: compare.func.datascience

.. py:staticmethod:: pca(simMatrix, k=1)

   Generates the Principal Component Analysis of the given data.

   :param simMatrix: Matrix contatining the data to be analyzed.  Columns represent dimensions.
   :param k: Dimension of analysis
   :type simMatrix: NumPy Matrix
   :type k: Integer

   :returns: Matrix of principal components with dimensions in rows
   :rtype: NumPy Matrix

.. py:staticmethod:: orderedEig(matrix, labelsMatrix=None, stripNegatives=True)

   Performs Eigendecomposition on matrix, then sorts the Eigenvalues by their Eigenvectors from greatest to least.

   :param matrix: Matrix to be decomposed
   :param labelsMatrix: 1-D matrix containing names of the labels for each point to be decomposed (note: not used currenlty)
   :param stripNegatives: Flag indicating that the algorithm should throw out negative Eigenvalues, and their associated Eigenvector.
   :type matrix: NumPy Matrix
   :type labelsMatrix: List-like
   :type stripNegatives: Boolean

   :returns: Matrix of Eigenvalues and Eigenvectors
   :rtype: NumPy Matrix, NumPy Matrix

.. py:staticmethod:: mmds(matrix)

   Performs Metric Multidimensional Scaling on the given distance matrix.

   :param distanceMatrix: Matrix of distances between points
   :type distanceMatrix: NumPy Matrix

   :returns: Matrix of points with dimensions in ...
   :rtype: NumPy Matrix
