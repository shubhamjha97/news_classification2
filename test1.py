import pandas as pd

cols=[]
empty=pd.DataFrame(columns=cols)
#print empty.head()
word_dict={'dfdf':[20], 'drfe':[28], 'ufdhdfh':[22]}
dict2={'dweewew':[36], 'erer':[73]}
#new1=pd.DataFrame(word_dict, index='columns')

new1=pd.DataFrame.from_dict(word_dict, orient='columns', dtype=None)
new2=pd.DataFrame.from_dict(dict2, orient='columns', dtype=None)
new1=new1.append(new2)
new1=new1.fillna(0)
print new1.head()
