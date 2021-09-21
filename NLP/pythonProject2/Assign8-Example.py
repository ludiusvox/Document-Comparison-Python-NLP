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
import re
import nltk
from nltk.corpus import stopwords
from random import choices
import os
import numpy



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
    def __init__(self, AuthName, FileNames, Encoding):
        """
        Initialize class variables
        """
        
        self.AuthName  = AuthName #the name of the author
        self.FileNames = FileNames #I took this to be a list of all files for one author
        self.Encoding = Encoding #some files are utf-8 encoded - pass that variable in here

        self.UniGrams = {} #dictionary of one word and frequency
        self.UniGramProb = {} #dictionary of one word and probability

        self.BiGrams = {} #dictionary of two words with frequencies
        self.BiGramProb = {} #dictionary of two words with probabilities
        self.Sentences = [] #list of sentences

        self._readInFileStrings() #call read the files

        
    """
    input:  none
    read in all files in the file name list
    this function will also handle utf-8 encoding
    the function will tokenize the sentences and words
    output: none
    """
    def _readInFileStrings(self):
        self.DocumentsWords = []
        for file in self.FileNames:
            with open(file, encoding = self.Encoding) as infile:
                input_lines = infile.read()
                self.Sentences.append(nltk.tokenize.sent_tokenize(input_lines))
                tempwords = nltk.tokenize.word_tokenize(input_lines)
        
            for word in tempwords:
                clean_word = re.sub(r'[^\w\s]', '', word)
                if len(clean_word) > 0:
                    self.DocumentsWords.append(clean_word)
            
        return


        
    # Accessors
    # -------------------------------------
    # Common good practice to put in things like general
    # accessors for code items like the sentences by name
    # or all sentences.
    
    
    
        
    # Calculation tasks.
    # -------------------------------------
    """
    input: none
    this function will go through the words of the document and count unigrams and bigrams
    it stores these counts in two dictionaries
    output: none
    """
    def collectNgrams(self):
        for word in self.DocumentsWords:
            if word not in self.UniGrams.keys():
                self.UniGrams[word.lower()] = 0
            self.UniGrams[word.lower()] += 1

        for I in range(len(self.DocumentsWords)):
            if (I + 1) < len(self.DocumentsWords):
                bigram = self.DocumentsWords[I] + " " + self.DocumentsWords[I+1] + " "
                if bigram not in self.BiGrams.keys():
                    self.BiGrams[bigram.lower()] = 0
                self.BiGrams[bigram.lower()] += 1

        return
    



    """
    input: none
    this function will take the frequency dictionaries and calculate the probabilities for each word
    output: none
    """
    def collectProbabilities(self):
        total_unis = 0        
        total_unis = sum(self.UniGrams.values())
        for key in self.UniGrams.keys():
            self.UniGramProb[key] = self.UniGrams[key] / total_unis

        total_bis = 0        
        total_bis = sum(self.BiGrams.values())
        for key in self.BiGrams.keys():
            self.BiGramProb[key] = self.BiGrams[key] / total_bis

        return
    

    
    
    # Calculate Text Odds.
    # -----------------------------------
    """
    input: a single document passed in as Sentence
    1. take the document from the separate author and determine the per sentence probability
    2. store each sentence probability in a list
    3. find the average for all the sentences in the document
    output: average sentence probability
    """
    def calcSentenceOdds(self, Sentence):
        Total_Doc_Prob = 1.0
        Doc_Probs = []
        for part in Sentence:
            tempword = part.split(" ")
            sentence_Prob = 1.0
            for word in tempword:
                try:
                    sentence_Prob *= self.UniGramProb[word]
                except:
                    sentence_Prob *= 1

            if sentence_Prob < 1:
                Doc_Probs.append(sentence_Prob)
        
        NP_Doc_Probs = numpy.array(Doc_Probs)
        DocSum = NP_Doc_Probs.sum()/len(Doc_Probs)

        return DocSum


    """
    input: the created author model
    go through the sentecnes for the athor model and pass them to calculate sentence odds
    output: the average of all the documents odds
    """
    def calculateCumulativeOdds(self, AuthorModel):
        All_Doc_Odds = []
        for sentence in AuthorModel.Sentences:
            All_Doc_Odds.append(self.calcSentenceOdds(sentence))
        return All_Doc_Odds
    


    
    # Now generate sentences.
    # ---------------------------------------
    """
    input: the length of the sentence to be generated
    1. pick a random bigram from all bigrams
    2. take the second word of that bibram and find all bigrams that start with that word
    3. choose a random bigram from that list and add the second word of that bigram to the sentence
    4. print the sentence
    output: th sentence
    """
    def generateSentence(self, Sentence_Length):
        
        population = list(self.BiGramProb.keys())
        probabilities = list(self.BiGramProb.values())
     
        sentence_seed = choices(population, probabilities)
        the_Sentence = sentence_seed[0]        
        temp_words = sentence_seed[0].split(" ")


        for I in range(Sentence_Length-2):
            temp_dict = {}
            for key in self.BiGramProb.keys():
                if key.startswith(temp_words[1]):
                    temp_dict[key] = self.BiGramProb[key]

            population = list(temp_dict.keys())
            probabilities = list(temp_dict.values())
            new_words = choices(population, probabilities)
            
            temp_words = new_words[0].split(" ")
            the_Sentence = the_Sentence + temp_words[1] + " "

        print(the_Sentence)

        return
    
    
    """
    input: the number of sentences and sentence length
    call generate sentence function for each time in count
    output: print statement
    """
    def generateMultipleSentences(self, Count, Sentence_Length):
        print(self.AuthName, " would say: ")
        for I in range(Count):
            self.generateSentence(Sentence_Length)
            
        return



#My 3 chosen authors
AuthNameA = 'King James Bible'
AuthNameB = 'Venerable Bede'
AuthNameC = 'Josephus'


#number of sentences and sentence length
NumofSentences = 5
Sentence_Length = 10

#the directories where I housed my authors documents
AuthADir = "/home/aaronlinder/PycharmProjects/pythonProject2/autha/"
AuthBDir = "/home/aaronlinder/PycharmProjects/pythonProject2/authb/"
AuthCDir = "/home/aaronlinder/PycharmProjects/pythonProject2/authc/"


#this bit of code is repeated three times below
#it will look in the author directory and find all files and append them to filenames
FileNames = []
for file in os.listdir(AuthADir):
    FileNames.append(AuthADir + file)

#Call the author model and collect n grams, and probabilities
AuthorA = AuthorModel(AuthNameA, FileNames, None)
AuthorA.collectNgrams()
AuthorA.collectProbabilities()


FileNames = []
for file in os.listdir(AuthBDir):
    FileNames.append(AuthBDir + file)

AuthorB = AuthorModel(AuthNameB, FileNames, None)
AuthorB.collectNgrams()
AuthorB.collectProbabilities()


FileNames = []
for file in os.listdir(AuthCDir):
    FileNames.append(AuthCDir + file)

AuthorC = AuthorModel(AuthNameC, FileNames, 'UTF-8')
AuthorC.collectNgrams()
AuthorC.collectProbabilities()


#calculate the odds that each author is like the first one
AuthorB_Probs = AuthorA.calculateCumulativeOdds(AuthorB)
AuthorC_Probs = AuthorA.calculateCumulativeOdds(AuthorC)

#find the average probabilities for each
sum_total = 0
for probs in AuthorB_Probs:
    sum_total += probs
AuthorB_Avg = sum_total / len(AuthorB_Probs)

sum_total = 0
for probs in AuthorC_Probs:
    sum_total += probs
AuthorC_Avg = sum_total / len(AuthorC_Probs)

#determine which author is more like the author A
if AuthorB_Avg > AuthorC_Avg:
    print(AuthorB.AuthName, " is most like ", AuthorA.AuthName)
else:
    print(AuthorC.AuthName, " is most like ", AuthorA.AuthName)


#generate the sentences
print("\n")
AuthorA.generateMultipleSentences(NumofSentences, Sentence_Length)
print("\n")
AuthorB.generateMultipleSentences(NumofSentences, Sentence_Length)
print("\n")
AuthorC.generateMultipleSentences(NumofSentences, Sentence_Length)


