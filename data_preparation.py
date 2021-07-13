import json
import pandas as pd
import pickle
import zipfile
from sys import argv
from sklearn.model_selection import train_test_split


script, filename, zipname = argv

infile = open(filename,'rb')
data = pickle.load(infile)
infile.close()
list_of_dict_values = list(data.values())

df = pd.DataFrame(columns=['id','xmin','ymin','xmax','ymax','xcen', 'ycen', 'w','h', 'class'])

columns = list(df)
data_list = []

for i in list_of_dict_values:
  parsed = json.loads(i)
  try:
    values = [parsed['filename'], parsed['results'][0]['box']['xmin'], parsed['results'][0]['box']['ymin'], parsed['results'][0]['box']['xmax'], parsed['results'][0]['box']['ymax']]
    zipped = zip(columns, values)
    a_dictionary = dict(zipped)
    data_list.append(a_dictionary)
  except:
    pass
df = df.append(data_list, True)

df['class'] = 0
df['xcen'] = (df['xmin'] + df['xmax']) / 2 / 2048
df['ycen'] = (df['ymin'] + df['ymax']) / 2 / 700
df['w'] = (df['xmax'] - df['xmin']) / 2048
df['h'] = (df['ymax'] - df['ymin']) / 700

df1 = df.copy()
df1['id'] = df1['id'].str[:-4]
y1 = df1['id']

df['id'] = 'darknet/build/darknet/x64/data/obj/' + df['id'].astype(str)

X = df[['class', 'xcen', 'ycen', 'w', 'h']]
y = df['id']



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


def prepare_data():
    
    images_dir = 'build/darknet/x64/data/obj'
    
    with zipfile.ZipFile(zipname, 'r') as zip_ref:
        zip_ref.extractall(images_dir)
    
    i = 0 

    for row in X.values: 
        file_title = f'build/darknet/x64/data/obj/{y1.iloc[i]}.txt'
        row.tofile(file_title, sep=" ", format="%s") 
        i+=1
        
    for index, value in y_train.items():
        file_title = 'build/darknet/x64/data/train.txt'
        with open(file_title, 'a') as the_file:
        	the_file.write(value+'\n')

    for index, value in y_test.items():
        file_title = 'build/darknet/x64/data/test.txt'
        with open(file_title, 'a') as the_file:
        	the_file.write(value+'\n')
    
  
prepare_data()





