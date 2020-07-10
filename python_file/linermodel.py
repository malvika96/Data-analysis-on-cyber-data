import numpy as np #for using data as array
import pandas as pd #for loading csv file data to numpy array
import matplotlib.pyplot as plt #for plotting graph of x,y
from sklearn import linear_model # for model we want to predict by
from sklearn.metrics import mean_squared_error, r2_score #for mean error and variance calculation
from sklearn.model_selection import train_test_split #splitting traing and testing sets

#dataset
dataset = pd.read_csv('C://Users/MALVIKA/Desktop/18mcl2/Project_datascience/cyber_Crime2.csv')
'''print(dataset)'''
# Take column 1 say number of years
X = dataset.iloc[:,1].values
print(X)

# Take column 2 say salary
y = dataset.iloc[:,3].values  #below 18
#y = dataset.iloc[:,2].values   #between 18-30
#y = dataset.iloc[:,3].values    #betweeen 30-45
#y = dataset.iloc[:,4].values     #between 45-60
#y = dataset.iloc[:,5].values      #above 60
#y = dataset.iloc[:,6].values
print(y)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=1/3, random_state = 0)

print(X_train) # will take whole column 1 
print(X_test)  # will take one third column 1 data
print(y_train) # will take second column
print(y_test)  # will take one third of column data 2
from sklearn.linear_model import LinearRegression

regres= LinearRegression()
regres.fit(X_train, y_train)
y_pred=regres.predict(X_test)
#print(y_pred)

#plotting on tghe graph
plt.scatter(X_train, y_train, color= 'red')
plt.plot(X_train, regres.predict(X_train),color='blue')
plt.xlabel('Year')
plt.ylabel('Crime Rate')
plt.title('Year Vs Crimes')
plt.show() 
