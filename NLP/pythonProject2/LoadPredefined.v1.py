# AIA LoadPredefined.py
# @copyright: Collin Lynch
#
# Sample code on loading predefined data using the Gensim library.


# Import the Gensim library's downloader package which provides
# access to predefined embeddings and other corpora.
import gensim.downloader

import nltk
import requests
from bs4 import BeautifulSoup
import gensim

# Get a list of all the predefined things in the set.  This will
# be a dict that breaks into two pieces, corpora which we can use
# for text info, and models that we can access.
gensim.downloader.info()
# This lists the available models.
gensim.downloader.info()['models'].keys()

# We will use a smaller model that is trained on wikipedia.  You can
# find the info here.
gensim.downloader.info()['models']['glove-wiki-gigaword-50']

req_moodle = requests.get("https://moodle-projects.wolfware.ncsu.edu/course/view.php?id=8143#section-0")
SoupText_moodle = BeautifulSoup(req_moodle.text)
PageText_moodle = SoupText_moodle.get_text()


nltk.data.path.append("/Volumes/HD2/DevEnv/Python/NLTK/nltk_data")
sentence_detector = nltk.data.load('tokenizers/punkt/english.pickle')
Punctuation = sentence_detector.tokenize(PageText_moodle.strip())


Sentences = nltk.tokenize.sent_tokenize(PageText_moodle)
Words_moodle = nltk.tokenize.word_tokenize(PageText_moodle)

Stopwords = list(nltk.corpus.stopwords.words("english"))

dataset = []
clean_dataset = []
for d in Words_moodle:
    dataset.append([d])
    if (d.lower() not in Stopwords):
        clean_dataset.append([d])
        

model_moodle = gensim.models.Word2Vec(dataset, min_count=2)

vector_moodle = model_moodle.wv['ID']

clean_model_moodle = gensim.models.Word2Vec(clean_dataset, min_count=2)

clean_vector_moodle = clean_model_moodle.wv['ID']

# Now download the model itself.
#  (NOTE: This may take a little while)
GloveModel = gensim.downloader.load('glove-wiki-gigaword-50')

# You can get the word vector itself via a simple lookup.
#GloveModel["flemish"]

# And now we can do some simple synonym or similarity lookup
# based upon the text.
#print(GloveModel.most_similar("flemish"))

# And given a sequence of words print out the most similar for each.
# This can be readily extended to any word list. 
Words = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
for d in Words_moodle:
    if (d in GloveModel):
        print("Most similar word to \"{}\" is \"{}\" ".format(d, GloveModel.most_similar(d)[0][0]))