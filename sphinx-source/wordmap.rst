==========
wordmap
==========
*The wordmap module, for all your mapping needs*

.. py:module:: compare.func.wordmap

.. py:staticmethod:: synonymList(word)

   A helper method to generate a list of synonyms of "word" using Princeton's WordNet

   :param word: The word whose synonyms will be returned
   :type word: String
   :returns: A list of the synonyms of \"word\"
   :rtype: List of Strings

.. py:staticmethod:: generateWordMap(doc, quiet=False)

   Generates a map of synonyms from the set of words in document "doc"
   Duplicate matches are ignored
        
   :param doc: Document from which to generate the word map
   :param quiet: Optional argument to toggle printing progress bar (defaults to false)
   :type doc: Document
   :type quiet: Boolean
   :returns: Reference to the generated map
   :rtype:  NetworkX Graph Object

.. py:staticmethod:: generateMarkov(theMap)
   
   Generates a Markov matrix from the word map generated using :py:meth:`generateWordMap`
   The matrix is generated using the adjacency matrix of "theMap"

   :param theMap: A word synonymity map
   :type theMap: NetworkX Graph Object
   :returns: A Markov matrix
   :rtype: NumPy Matrix

.. py:staticmethod:: generateDocumentVector(allWords, document, count=False)

   Generates a vertical vector of the frequency of occurance in allWords of each word in document
   The order of the words appearing in the returned vector will match the order of the words appearing in allWords.wordlist

   If parameter "count" is true, the vector contains the actual frequence (i.e., if "test" appears three times, its entry will be "3")
   If parameter "count" is false, the vector ignores duplicate occurances (i.e., "test"'s entry would be "1")

   :param allWords: Document contating all of the words in the two documents being compared
   :param document: Document from which to generate the vector
   :param count: Flag to determine whether the vector should contain the actual count of each word
   :type allWords: Document
   :type document: Document
   :type count: Boolean
   :returns: Vertical vector
   :rtype: NumPy Matrix

.. py:staticmethod:: compareDocs(doc1, doc2, depth=0, quiet=False, count=False)

   Compares two documents using wordmap

   :param doc1 doc2: Documents to compare
   :type doc1 doc2: Document
   :param depth: Determines how many times the document vectors are multiplied by the markov matrix (0 = once)
   :param quiet: Determines whether word map generation should show progress bar (see :py:meth:`generateWordMap`)
   :param count: determines whether word vectors should count words, or indicate presence alone (see :py:meth:`generateDocumentVector`)
   :type depth: Integer
   :type quiet: Boolean
   :type count: Boolean
   :returns: Similarity measure
   :rtype: Float

.. py:staticmethod:: compareFolderDocs(folder, depth=0, quiet=False, drawMap=False, count=False)

   Compares all documents in a given folder, outputting a matrix of their similarities

   .. NOTE:: All documents must be in plain text format

   :param folder: Folder contating documents to compare
   :param depth: Determines how many times the document vectors are multiplied by the markov matrix (0 = once)
   :param quiet: Determines whether word map generation should show progress bar (see :py:meth:`generateWordMap`)
   :param drawMap: Determines whether the markov matrix should be drawn using NetworkX
   :param count: determines whether word vectors should count words, or indicate presence alone (see :py:meth:`generateDocumentVector`)
   :type depth: Integer
   :type quiet: Boolean
   :type drawMap: Boolean
   :type count: Boolean
   :returns: Matrix containing pairwise similarity of all documents
   :rtype: NumPy Matrix