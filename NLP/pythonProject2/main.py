# This is a sample Python script.
import nltk
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import DocSimilarity
import lxml
import scipy
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nltk.download('punkt')
    nltk.download('stopwords')

    Req = requests.get("https://nationalapprenticeship.org/")

    Req.text[0:100]
    SoupText = BeautifulSoup(Req.text, features="lxml")
    PageText = SoupText.get_text()
    PageText[2200:2200]

    Req1 = requests.get("https://www.hornet.org")

    Req1.text[0:100]
    SoupText1 = BeautifulSoup(Req1.text, features="lxml")
    PageText1 = SoupText1.get_text()
    PageText1[2200:2200]


    sentence_Detector = nltk.data.load('tokenizers/punkt/english.pickle')
    Punctuation = sentence_Detector.tokenize(PageText.strip())
    Sentences = nltk.tokenize.sent_tokenize((PageText.strip()))
    Twitter =TweetTokenizer()

    #print(Twitter.tokenize(PageText))
    Words =nltk.tokenize.word_tokenize(PageText)
    Words1 = nltk.tokenize.word_tokenize(PageText1)

    dataset =[]
    #print("\n")
    #for word in stopwords.words('english'):
        #print(word)
    #for d in Words:
    #    dataset.append([d])
    #print(dataset)
    """import gensim

    Model = gensim.models.Word2Vec(dataset, min_count=2)
    vector = Model.wv['industry']"""
    text1 = DocSimilarity.countFrequencies(Words)
    text2 = DocSimilarity.countFrequencies(Words1)
    cd = DocSimilarity.compareDocs(text1,text2)
    print(cd)
    cb = DocSimilarity.seqdiff(Words,Words1)
    print(cb)
    (cs, WordVectors1) = DocSimilarity.makeDocVec(Words)
    (cs1, WordVectors2) = DocSimilarity.makeDocVec(Words1)
    cs2= scipy.spatial.distance.cosine(WordVectors1[0], WordVectors2[0])
    print(cs2)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
