Document
========
*A friendly helper class*

.. py:module:: compare.classes

.. py:class:: Document(self, file = "", title = "Untitled", body = "")

   A class to wrap an abstract document.  Can be a full legal brief, or a simple
   string of characters.

.. _fields:

Fields
------

      .. py:attribute:: title

      	 String holding the title of the document.  If created from a file, will contain the name of the file (without the file extension)

      .. py:attribute:: body

      	 String containing the body of the document

      .. py:attribute:: file
      	 
	 String containing the path to the file from which the document is generated (see :py:meth:`Document`)

      .. py:attribute:: wordlist

      	 List containing each word in the document as an element (removing non-word characters)

      .. py:attribute:: wordcount

      	 A count of all of the words in the document (do not have to be unique words)

      .. py:attribute:: meta

      	 An object that contains important information about the object

      	 .. todo:: Is this necessary?

.. _methods:

Methods
-------

   .. py:method:: Document(self, file = "", title = "Untitled", body = "")

      Constructor.  See fields_ for parameter description.  If :py:attr:`file` is specified, document is generated from file.

   .. py:method:: toLowerCase(self)
      
      Converts the entire document to lowercase, both the :py:attr:`body` and the :py:attr:`wordlist`

.. todo:: Document this class *no pun intended*
.. todo:: Implement other magic methods (comparison?, formatting?)