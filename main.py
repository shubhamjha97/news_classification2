from file_loader import load_train_files
from file_loader import load_test_files
from prediction import Model
from pandas_db import table_pd
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd

#Pickle trained classifier!!!!!!!!!!!!!!!!!!!!!!!!
#Create empty table
train_table=table_pd()
test_table=table_pd()

#Target paths
loc="/home/shubham/PycharmProjects/news_classifier/training_set/"
loc_bow="/home/shubham/PycharmProjects/news_classifier/bag_of_words/"
cat_str=['sport', 'business', 'tech', 'entertainment', 'politics']
#Prediction file path
test_loc='/home/shubham/PycharmProjects/news_classifier/test_set/031.txt'

#Load train files and run Bag of Words
load_train_files(loc, cat_str, train_table, test_table)
#Load test files and run Bag of Words
load_test_files(test_loc, test_table, train_table)

#Retrieve training data
Xtrain, Ytrain=train_table.return_train_data()
#Retrieve test data
Xtest=test_table.return_test_data()
#sh=Xtest.shape
#Encoding categorical variables
for_encoding=['CATEGORY']
le=LabelEncoder()
Ytrain=le.fit_transform(Ytrain)
Xtrain=Xtrain.drop('CATEGORY', 1)
Xtest=Xtest.drop('CATEGORY', 1)
print 'FILENAME' in Xtrain.columns

print pd.Series(Ytrain).value_counts()
#for i in for_encoding:
#	Ytrain[i]=le.fit_transform(Ytrain[i])
#	Xtest[i]=le.fit_transform(Xtest[i])

#for i in range(0,6):
#	print Xtest[Xtest['CATEGORY']==i].shape

#Xtest=Xtest[Xtest['CATEGORY']==0]

#Xtrain=Xtrain.as_matrix()
#Xtest=Xtest.as_matrix()

#Make predictions
mod=Model()
mod.train_classifier(Xtrain, Ytrain)
#print Xtest.shape#.reshape(-1,sh[1])
#print Xtrain.shape
mod.make_predictions(Xtest)