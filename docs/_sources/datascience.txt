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

.. py:staticmethod:: mmds(matrix)

   Generates the Metrix Multidimensional Scaling of the given matrix

   .. todo:: Write method & document