from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score

#Train and cross validation

def Model:

	def __init__(self):
		self.model=RandomForestClassifier(n_estimators=100)


	def train_classifier(self, X, Y):
		Xtrain, Xval, Ytrain, Yval=train_test_split(X,Y, train_size=0.7)
		self.model.fit(Xtrain, Ytrain)
		print "Cross validation score= " + str(accuracy_score(model.predict(Xval), Yval))

	def make_predictions(Xpred):
		print 'Prediction= '+str(self.model.predict(Xpred))