from file_loader import load_files
from file_loader import load_test_files
from prediction import Model
from pandas_db import table_pd
from sklearn.preprocessing import LabelEncoder

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

for_encoding=['FILENAME','CATEGORY']

le=LabelEncoder()
for i in for_encoding:
	Xtrain[i]=le.fit_transform(Xtrain[i])
	Xtest[i]=le.fit_transform(Xtest[i])

Xtrain=Xtrain.as_matrix()
Xtest=Xtest.as_matrix()
#Make predictions
mod=Model()
mod.train_classifier(Xtrain, Ytrain)
mod.make_predictions(Xtest)