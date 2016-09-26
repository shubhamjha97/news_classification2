from os import listdir
def load_files(loc, cat_str):
    corpus=[]
    for cat in cat_str:
        for i in (listdir(loc + cat)):
            corpus.append({'file':open((loc+cat+'/'+i), 'r'), 'category':cat})
        #print cat+str(len(listdir(loc+cat)))
    return corpus