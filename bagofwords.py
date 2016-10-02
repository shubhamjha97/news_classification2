from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from pandas_db import table_pd
from nltk.corpus import stopwords

porter_stemmer=PorterStemmer()
stop=set(stopwords.words('english'))
opset=set([' ', u"'s", '-', ',', '.'])

def BOW(file,filename,category, train_table, test_table):
    word_dict = {}
    for sentence in file:
        sentence = sentence.decode('utf8')
        sentence = word_tokenize(sentence.lower())
        for word in sentence:
            if word not in stop.union(opset):
                word = porter_stemmer.stem(word)
                word_dict[word] = word_dict.get(word, 0) + 1

    for word in word_dict:
        word_dict[word]=[word_dict[word]]

    modified_filename=category+filename
    train_table.insert_table(word_dict,modified_filename,category)
    test_table.insert_table(word_dict,modified_filename,category)

def BOW_test_data(file,test_table, train_table):
    word_dict = {}
    for sentence in file:
        sentence = sentence.decode('utf8')
        sentence = word_tokenize(sentence.lower())
        for word in sentence:
            if word not in stop.union(opset):
                word = porter_stemmer.stem(word)
                word_dict[word] = word_dict.get(word, 0) + 1

    for word in word_dict:
        word_dict[word]=[word_dict[word]]

    modified_filename='TEST'
    test_table.insert_table(word_dict,modified_filename,'TEST')
    train_table.insert_table(word_dict,modified_filename,'TEST')