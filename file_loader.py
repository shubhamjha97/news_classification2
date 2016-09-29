from os import listdir
from bagofwords import BOW
from tqdm import tqdm

def load_files(location, cat_list, table):
    for category in tqdm(cat_list):
        for file in tqdm(listdir(location + category)):
            temp_file=open((location+category+'/'+file),'r')
            BOW(temp_file,file,category, table)
            temp_file.close()

def load_test_files(path, table):
	temp_file=open(path,'r')
	file='TEST'
	category='TEST'
	BOW(temp_file,file,category, table)
	temp_file.close()