ngram
=====

*Still can't figure out how it's computationally efficient...*


.. py:module:: compare.func.ngram

.. py:staticmethod:: calculatePrimeLength(substring, document)

   Calculates length of substring from first character to end of document

   :param substring: Substring to search for
   :param document: Document to search through
   :type substring: String
   :type document: Document

.. py:staticmethod:: calculateLength(substring, document)

   Calculates length of substring from first character to end of character

   :param substring: Substring to search for
   :param document: Document to search through
   :type substring: String
   :type document: Document

.. py:staticmethod:: K_Prime(doc1, doc2, n, lambd=0.5)

   Calculates K' recursively (as in paper)

   :param doc1: First document
   :param doc2: Second document
      

.. todo:: Finish documenting this module