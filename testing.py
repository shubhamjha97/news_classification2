from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from os import listdir
import os
from tqdm import tqdm
import pandas as pd
stop=set(stopwords.words('english'))
opset=set([' ', u"'s", '-', ',', '.'])
porter_stemmer=PorterStemmer()
loc="/home/shubham/PycharmProjects/news_classifier/training_set/"
loc_bow="/home/shubham/PycharmProjects/news_classifier/bag_of_words/"
cat_str=['sport', 'business', 'tech', 'entertainment', 'politics']

doc=open(loc+cat_str[2]+'/001.txt', 'r')
word_dict={}
for sentence in doc:
    sentence=sentence.decode('utf8')
    sentence=word_tokenize(sentence.lower())
    for word in sentence:
        if word not in stop.union(opset):
            word=porter_stemmer.stem(word)
            word_dict[word]=word_dict.get(word, 0)+1
print pd.Series(word_dict).sort_values(ascending=False)