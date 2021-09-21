# AIA DocSimilarity.py
# @copyright: Collin Lynch
#
# Code to manage the document comparison and similarity
# measures.  For Week 8 workshop.

# In the last workshop we looked at ways to tokenize documents and
# to represent the document contents as sequences of words, sentences
# or vectors.  In this code we will draw on those representations
# to perform the basic tasks of document similarity.

from collections import defaultdict
from nltk.corpus import stopwords
import nltk

import requests
from bs4 import BeautifulSoup

# The first and most straightforward way to compare documents is through
# a comparison of the words that are present or absent.  Here we can
# draw on the word statistics code that was shown on slide deck 8-2, slide 16.  
# Here once we have calculated the frequency dicts as we do in the loop we can
# compare two documents by calculating the number of words that are
# present in one doc over another or counting the absolute difference
# in numbers.
def countFrequencies(Words, Stopwords=[]):
    WordFrequencies = defaultdict(int)

    for word in Words:
        if (word not in Stopwords):
            WordFrequencies[word.lower()] += 1

    return(WordFrequencies)



# Then given Word Frequency dicts for two different documents
# we can calculate the delta as the number different between
# them for each word.  Here A word present in one but not the
# other gets its total count.
def compareDocs(Doc1Freq, Doc2Freq):

    # Set storage for the word.
    TotalDiff = 0

    # Now iterate over the first doc getting counts
    # for all items in it.
    for (Word, Count1) in Doc1Freq.items():

        # If it is shared add in the difference.
        if (Word in Doc2Freq):
            Count2 = Doc2Freq[Word]
            TotalDiff += abs(Count1 - Count2)

        # Else we add in the total amount.
        else: TotalDiff += Count1

    # Now we deal with all the items that are present in 2
    # But are not present in 1.  Again we add the total count.
    for (Word, Count2) in Doc2Freq.items():
        if (Word not in Doc1Freq):
            TotalDiff += Count2

    # Finally return the Count.
    return(TotalDiff)




# The above method gets us a gestalt difference but it ignores
# word sequence which might be fine for "topical" comparisons
# but it does nothing for sequence.
#
# A simple sequential difference is a manhattan distance.  This
# will allow us to check how far the sequences are off from
# one-another.  This process simply iterates and counts matches.
# As the results will show the similarity is always low.  Even
# if we remove stopwords.
def seqdiff(Seq1, Seq2):

    Count = 0

    for I in range(len(Seq1)):

        Token1 = Seq1[I]
        Token2 = Seq2[I]

        if (Token1 != Token2):
            Count += 1

    return(Count)



# Since the numbers are low it often makes more sense to use a
# sensitive distance metric that, among other things, takes into
# account word similarity.  This is where we can draw on the
# vector representations and do a word-by-word similarity.  This
# would use the vector similarity like above.
#
# Or we can produce a sequence level vector by summing up the 
# individual word vectors in a sequence and then perform a
# cosine similarity of the two vectors to get an overall measure.

import numpy
import scipy.spatial
import gensim
import gensim.downloader

# I suggest commenting the following line out until you reach this point
GloveModel = gensim.downloader.load('glove-twitter-50')




# To make a document vector suitable for this task we first
# convert it to a lower case sequence and then use that to
# get the individual values.  Then we sum the total up.
def makeDocVec(DocTokens):

    WordVectors = []
    for Token in DocTokens:
        try:
            WordVectors.append(GloveModel[Token.lower()])
            
        except:
            print(Token, " not in database")
    
    DocSum = numpy.sum(numpy.array(WordVectors))
    return(DocSum, WordVectors)




# TODO
# import at least two web pages and make the text from them readable
# pass the tokenized webpages into count frequencies and store the results
# pass the count frequencies into compare docs
# pass the count frequencies into the seq diff function
# pass the tokenized webpages into makeDocVecs and store the results
# pass the doc sums into the below function

#call your function



# Now if you do the above for two documents you can just compare
# them using the basic cosine similarity function.
#scipy.spatial.distance.cosine(Doc1Sum, Doc2Sum)
    


