import nltk
import requests
from bs4 import BeautifulSoup
from nltk.tokenize import TweetTokenizer
import gensim

req_wiki = requests.get("https://en.wikipedia.org/wiki/Energy_in_Slovenia")
SoupText_wiki = BeautifulSoup(req_wiki.text)
PageText_wiki = SoupText_wiki.get_text()

print(PageText_wiki[2200:3000])

req_mann = requests.get("https://www.mann-hummel.com/en.html")
SoupText_mann = BeautifulSoup(req_mann.text)
PageText_mann = SoupText_mann.get_text()

print(PageText_mann[2200:3000])


req_moodle = requests.get("https://moodle-projects.wolfware.ncsu.edu/course/view.php?id=8143#section-0")
SoupText_moodle = BeautifulSoup(req_moodle.text)
PageText_moodle = SoupText_moodle.get_text()

print(PageText_moodle[2200:3000])


nltk.data.path.append("/Volumes/HD2/DevEnv/Python/NLTK/nltk_data")
sentence_detector = nltk.data.load('tokenizers/punkt/english.pickle')
Punctuation = sentence_detector.tokenize(PageText_moodle.strip())


Sentences = nltk.tokenize.sent_tokenize(PageText_moodle)
Words_moodle = nltk.tokenize.word_tokenize(PageText_moodle)

# print(Punctuation)
# print(Sentences)
# print(Words_moodle)
Twitter = TweetTokenizer()
# print(Twitter.tokenize(PageText_moodle))
twitter = Twitter.tokenize(PageText_moodle)

for word in Words_moodle:
    if (word not in twitter):
        print(word)
        
        

Stopwords = list(nltk.corpus.stopwords.words("english"))

dataset = []
clean_dataset = []
for d in Words_moodle:
    dataset.append([d])
    if (d.lower() not in Stopwords):
        clean_dataset.append([d])
        

model_moodle = gensim.models.Word2Vec(dataset, min_count=2)
print(model_moodle.wv.key_to_index)

vector_moodle = model_moodle.wv['ID']
print(vector_moodle)


clean_model_moodle = gensim.models.Word2Vec(clean_dataset, min_count=2)
print(clean_model_moodle.wv.key_to_index)

clean_vector_moodle = clean_model_moodle.wv['ID']
print(clean_vector_moodle)
        