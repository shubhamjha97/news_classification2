#from nltk.tokenize import word_tokenize
#from os import listdir
#import os
from file_loader import load_files
from file_loader import load_test_files
#from tqdm import tqdm
from prediction import Model
from pandas_db import table_pd

#Pickle trained classifier!!!!!!!!!!!!!!!!!!!!!!!!
#Create empty table
table=table_pd()
test_table=table_pd()

#Target paths
loc="/home/shubham/PycharmProjects/news_classifier/training_set/"
loc_bow="/home/shubham/PycharmProjects/news_classifier/bag_of_words/"
cat_str=['sport', 'business', 'tech', 'entertainment', 'politics']

#Load train files and run Bag of Words
load_files(loc, cat_str, table)

#Retrieve training data
Xtrain, Ytrain=table.return_train_data()
#Done

#Prediction file path
test_loc='/home/shubham/PycharmProjects/news_classifier/test_set/031.txt'

#Load test files and run Bag of Words
load_test_files(test_loc, test_table)
#Retrieve test data
Xtest=test_table.return_test_data()

#Make predictions
mod=Model()
mod.train_classifier(Xtrain, Ytrain)
mod.make_predictions(Xtest)

