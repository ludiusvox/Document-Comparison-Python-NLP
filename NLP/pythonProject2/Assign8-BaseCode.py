# -*- coding: utf-8 -*-
"""
AIA Markov Model Base Code
@copyright: Collin Lynch 2021

This assignment calls for you to build a simple probabilistic 
language model based upon ngrams which you can use to recognize
or generate language based upon authorship.  Use the skeleton 
code below to support your implementation.
"""



# Import code.
# ------------------------------------
import nltk
import glob



# Subtask 1. 
# ------------------------------------
# Load the documents into strings and list of words for our 
# calculations and store the bigrams and probability tables.

class AuthorModel(object):
    """
    The Author Model class stores a set of documents and allows 
    us to calculate the basic probabilities and items.
    """
    
    # init
    # -----------------------------------
    def __init__(self, AuthName, FileNames):
        """
        Initialize the document with the file name.

        Parameters
        ----------
        FileName : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        
        self.AuthName  = AuthName
        self.FileNames = FileNames
        
        self._readInFileStrings()
        
    
    def _readInFileStrings(self):
        """
        Read in the text from the set files and extract
        sentences and other items.

        Returns
        -------
        None.

        """
        
        # Read In texts.
        self.DocumentsStrings = {}
        
        
        # Split to sentences
        self.DocumentsSentences = {}
        
    
        
    # Accessors
    # -------------------------------------
    # Common good practice to put in things like general
    # accessors for code items like the sentences by name
    # or all sentences.
    
    
    
        
    # Calculation tasks.
    # -------------------------------------
    def collectNgrams(self):
        """
        Collect the bigrams and unigrams with frequencies 
        from the document text.
        

        Returns
        -------
        None.

        """

        pass
    
    def collectProbabilities(self):
        """
        Collect the unary and conditional probabilities.

        Returns
        -------
        None.

        """
        
        pass
    

    
    
    # Calculate Text Odds.
    # -----------------------------------
    def calcSentenceOdds(self, Sentence):
        """
        Calculate the odds of an individual sentence.
        

        Parameters
        ----------
        Sentence : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        pass
    
    def calculateCumulativeOdds(self, Sentences):
        """
        Calculate the cumulative odds of a set of sentences.

        Parameters
        ----------
        Sentences : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        pass
    
    
    # Now generate sentences.
    # ---------------------------------------
    def generateSentence(self):
        """
        Generate a single sentence.
        

        Returns
        -------
        None.

        """
        
        pass
    
    
    def generateMultipleSentences(self, Count):
        """
        Generate Count sentences.

        Parameters
        ----------
        Count : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        pass
