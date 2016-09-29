import pandas as pd

empty=[]
def table_pd:

	def __init__(self):
		self.table=pd.DataFrame(columns=empty)

	def insert_table(self, dict_word, filename, category):
		dict_word['CATEGORY']=category
		dict_word['FILENAME']=filename
		temp_table=pd.DataFrame.from_dict(dict_word, orient='columns', dtype=None)
		self.table=table.append(temp_table)
		self.table=self.table.fillna(0)
		
	def return_sparse_mat(self):
		return self.table.as_matrix()
	
