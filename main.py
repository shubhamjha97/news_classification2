from file_loader import load_train_files
from file_loader import load_test_files
from prediction import Model
from pandas_db import table_pd
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd

#Create empty table
train_table=table_pd()
test_table=table_pd()

#Target paths
loc="/home/shubham/PycharmProjects/news_classifier/training_set/"
loc_bow="/home/shubham/PycharmProjects/news_classifier/bag_of_words/"
cat_str=['sport', 'business', 'tech', 'entertainment', 'politics']
#Prediction file path
test_loc='/home/shubham/PycharmProjects/news_classifier/test_set/148.txt'

#Load train files and run Bag of Words
load_train_files(loc, cat_str, train_table, test_table) #create train_table, insert test columns, delete test rows
#Load test files and run Bag of Words
load_test_files(test_loc, test_table, train_table) #create test table, insert train columns, delete train rows

#Retrieve training data
Xtrain, Ytrain=train_table.return_train_data()
#Retrieve test data
Xtest=test_table.return_test_data()

#Encoding categorical variables
for_encoding=['CATEGORY']
le=LabelEncoder()
Ytrain=le.fit_transform(Ytrain)

#Make predictions
mod=Model(le)
mod.train_classifier(Xtrain, Ytrain)
mod.make_predictions(Xtest)