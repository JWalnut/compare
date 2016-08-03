from setuptools import setup
import nltk

setup(name='compare',
      version='0.4',
      description='Document Comparison',
      url='http://github.com/JWalnut/compare',
      author='JWalnut,tyrusberr',
      author_email='',
      license='',
      packages=['compare'],
      install_requires=[
          'progressbar',
      ],
      zip_safe=False)
      
nltk.download('wordnet')