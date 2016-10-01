from os import listdir
from bagofwords import BOW
from bagofwords import BOW_test_data
from tqdm import tqdm

def load_train_files(location, cat_list, train_table, test_table):
    for category in tqdm(cat_list):
        for file in tqdm(listdir(location + category)):
            temp_file=open((location+category+'/'+file),'r')
            BOW(temp_file,file,category, train_table,test_table)
            temp_file.close()

def load_test_files(path, test_table, train_table):
	temp_file=open(path,'r')
	temp_file1=open(path,'r')
	filename='TEST'
	category='TEST'
	BOW(temp_file,filename,category, train_table, test_table)
	BOW_test_data(temp_file1,test_table,train_table)
	temp_file.close()