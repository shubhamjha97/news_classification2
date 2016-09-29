from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from pandas_db import table_pd
from nltk.corpus import stopwords

porter_stemmer=PorterStemmer()
stop=set(stopwords.words('english'))
opset=set([' ', u"'s", '-', ',', '.'])

def BOW(file,filename,category, table):
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
    table.insert_table(word_dict,modified_filename,category)
    #print pd.Series(word_dict).sort_values(ascending=False)