from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from database_ops import add_to_database
porter_stemmer=PorterStemmer()

def BOW(file,filename,category):
    word_dict = {}
    for sentence in file:
        sentence = sentence.decode('utf8')
        sentence = word_tokenize(sentence.lower())
        for word in sentence:
            if word not in stop.union(opset):
                word = porter_stemmer.stem(word)
                word_dict[word] = word_dict.get(word, 0) + 1

    add_to_database(word_dict,filename,category)
    #print pd.Series(word_dict).sort_values(ascending=False)