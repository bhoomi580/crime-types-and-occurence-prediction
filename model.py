# 1.read dataset using pandas

import pandas as pd
data=pd.read_csv('data.csv')
print(data)

#2.cleaning the data

print(data.columns)
print(data.shape)
#print(data.info())
#print(data.describe())
print(data.dtypes)
print(data.head(10))
print(data.tail(10))
data=data.dropna()
print(data.shape)

#3.select features and output columns from dataset



print(data.columns)
x=['Case Number','Location','Year','Latitude','Longitude']
y=['Primary Type']
x=data[x]
y=data[y]
print(x,y)

#4.select the model of algorithm
#pip install scikit-learn

#from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

#5.define model

model=RandomForestRegressor(random_state=1)

#6.fit model -> recognizes the pattern of data
print("---------------------------")
from sklearn.model_selection import train_test_split
train_x, val_x, train_y, val_y= train_test_split(x,y,random_state=0)
print(train_x, val_x, train_y, val_y)
model.fit(train_x,train_y)

#7.prediction
print("prediction:")
print(data.head(5))
print(model.predict(val_x.head(5)))

from sklearn.metrics import mean_absolute_error

predict=model.predict(val_x)
print(mean_absolute_error(val_y,predict))

import pickle
with open('model.pkl','wb') as file:
    pickle.dump(model,file)
    
    

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import datetime as dt

# # read data from csv file to dataframe
# df = pd.read_csv('/kaggle/input/crime/Crime.csv')

# #shows columns of dataset and their types
# df.dtypes

# #shows number of rows and columns of dataset
# df.shape
# print(df.shape)

