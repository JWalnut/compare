Corpus
======

*A wrapper class*

.. py:module:: compare.classes.corpus

.. py:class:: Corpus(self, folder = "", title = "")

   A class to wrap many of the document comparison methods, so that comparisons may be
   done multiple times on the same set of data.


.. _fields:

Fields
------

	.. py:attribute:: folder

	   Holds the path to the folder containing all of the comparable files

	.. py:attribute:: title

	   A simple identifier for the object.  Defaults to equal :py:attr:`folder`

	.. py:attribute:: doclist

	   A list of :py:class:`Document` objects containing the documents to be compared

	.. py:attribute:: wordlist

	   A list of all of the words in all of the given documents

	.. py:attribute:: corpuswordmap

	   A *NetworkX* graph to hold the wordmap of the folder of documents

	.. py:attribute:: markov

	   A *NumPy* array to hold the Markov matrix generated from the folder of documents

	.. py:attribute:: meta

	   A structure holding metadata about the documents to be compared

	   .. todo:: Once again, necessary?

.. _methods:

Methods
-------

   .. NOTE:: For most methods, see :py:mod:`wordmap` for implementation.

   .. py:method:: Corpus(self, folder = "", title = "")

      Constructor.  See fields_ for parameter description.

   .. py:method:: addFolder(self, foldertoadd = "", quiet = True, drawMap = False, synCount = False)

      Loads a folder of documents to be compared into the object, and generates a wordmap
      from those documents and the markov matrix.

      :param foldertoadd: Path to the folder containing comparable documents
      :type foldertoadd: String
      :param quiet: Toggle status bar when generating wordmap
      :type quiet: Boolean
      :param drawMap: Toggle graphical drawing of generated wordmap
      :type drawMap: Boolean
      :param synCount: Toggle graph weights based on how frequently WordNet gives it as a synonym
      :type synCount: Boolean

   .. py:method:: compareCorpus(self, depth = 0, count = False)

      Compares all of the documents loaded into the object, and returns a matrix of their pairwise distances
      See :py:meth:`wordmap.compare`