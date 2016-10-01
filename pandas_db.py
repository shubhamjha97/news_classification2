import pandas as pd

empty=[]
class table_pd:


	def __init__(self):
		self.table=pd.DataFrame(columns=empty)

	def insert_table(self, dict_word, filename, category):
		dict_word['CATEGORY']=category
		dict_word['FILENAME']=filename
		temp_table=pd.DataFrame.from_dict(dict_word, orient='columns', dtype=None)
		self.table=self.table.append(temp_table)
		self.table=self.table.fillna(0)
		
	def return_train_data(self):
		temp_table=self.table[self.table['CATEGORY']!='TEST']
		Y=temp_table['CATEGORY']
		temp=temp_table.drop('CATEGORY', 1)
		temp=temp_table.drop('FILENAME', 1)
		X=temp
		return X,Y

	def return_test_data(self):
		temp_table=self.table[self.table['CATEGORY']=='TEST']
		temp=temp_table.drop('CATEGORY', 1)
		temp=temp_table.drop('FILENAME', 1)
		X=temp
		#X=X[X['CATEGORY']=='TEST']
		return X

	#def return_sparse_mat(self):
	#	return self.table.as_matrix()
	
