from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score

#Train and cross validation

class Model:

	def __init__(self, le):
		self.model=KNeighborsClassifier(n_neighbors=8)
		self.le=le

	def train_classifier(self, X, Y):
		Xtrain, Xval, Ytrain, Yval=train_test_split(X,Y, train_size=0.7)
		self.model.fit(Xtrain, Ytrain)
		print "Cross validation score= " + str(accuracy_score(self.model.predict(Xval), Yval))

	def make_predictions(self, Xpred):
		print 'Prediction= '+str(self.le.inverse_transform(self.model.predict(Xpred)))