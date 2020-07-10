import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
 
#dataset 
dataset = pd.read_csv('C://Users/MALVIKA/Desktop/18mcl2\/Project_datascience/cyber_Crime.csv')
#print(dataset)

#X = dataset.iloc[:,0].values
#X = dataset.iloc[:,1].values 
#X = dataset.iloc[:,2].values 
#X = dataset.iloc[:,3].values 
#X = dataset.iloc[:,4].values 
#X = dataset.iloc[:,5].values 
#X = dataset.iloc[:,6].values 
#X = dataset.iloc[:,7].values
#X = dataset.iloc[:,8].values  
#print(X) 
 
# Take column 2 say salary 
 
#y = dataset.iloc[:,0].values
#y = dataset.iloc[:,1].values 
#y = dataset.iloc[:,2].values 
#y = dataset.iloc[:,3].values 
#y = dataset.iloc[:,4].values 
#y = dataset.iloc[:,5].values 
#y = dataset.iloc[:,6].values 
#y = dataset.iloc[:,7].values
#y = dataset.iloc[:,8].values  
#print(y)

from sklearn.model_selection import train_test_split 
 
X_train, X_test, y_train, y_test=train_test_split(X, y, 
test_size=1/3, random_state = 0) 
#print(X_train) # will take whole column 1  
#print(X_test)  # will take one third column 1 data 
#print(y_train) # will take second column 
#print(y_test)  # will take one third of column data 2 
 
from sklearn.linear_model import LinearRegression 
 
regres= LinearRegression()
regres.fit(X_train, y_train)
y_pred=regres.predict(X_test) 
print(y_pred)

#plotting on tghe graph
plt.scatter(X_train, y_train, color= 'red')
plt.plot(X_train, regres.predict(X_train),color='blue')
plt.title('Salary Vs Experience')
plt.show() 
