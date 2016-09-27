from os import listdir
from bagofwords import BOW

def load_files(location, cat_list):
    for category in cat_list:
        for file in (listdir(location + category)):
            temp_file=open((location+category+'/'+file),'r')
            BOW(temp_file,file,category)
            temp_file.close()
