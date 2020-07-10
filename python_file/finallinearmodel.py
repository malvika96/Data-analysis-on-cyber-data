# -*- coding: utf-8 -*-
"""
Created on Wed May  1 18:57:53 2019

@author: MALVIKA
"""

#import numpy as np #for using data as array
import pandas as pd #for loading csv file data to numpy array
import matplotlib.pyplot as plt #for plotting graph of x,y
from sklearn import linear_model # for model we want to predict by
from sklearn.metrics import mean_squared_error, r2_score #for mean error and variance calculation
from sklearn.model_selection import train_test_split #splitting traing and testing sets

"""
#dataset
dataset = pd.read_csv('C://Users/MALVIKA/Desktop/18mcl2/Project_datascience/cyber_Crime.csv')


X = dataset.iloc[:,2].values
print(X)
#Y = dataset.iloc[:,3].values #below 18
#Y = dataset.iloc[:,4].values   #between 18-30
#Y = dataset.iloc[:,5].values    #betweeen 30-45
#Y = dataset.iloc[:,6].values     #between 45-60
#Y = dataset.iloc[:,7].values      #above 60
Y = dataset.iloc[:,8].values    #Total
print(Y)
X_train, X_test, Y_train,Y_test=train_test_split(X, Y, test_size=1/3, random_state = 0)

#reshaping array to convert from 1D to 2D array
X_test=X_test.reshape(-1,1)
X_train=X_train.reshape(-1,1)


#lin_reg is our model calling model "LinearRegression()"

lin_reg=linear_model.LinearRegression()

#fittring our data in linear regression model
lin_reg.fit(X_train,Y_train)

#making predictions
lin_reg_pred=lin_reg.predict(X_test)

#cof_and intercept_ are cofficients and intercepts resp. for our model
print("Coefficients : \n",lin_reg.coef_)
print("Intercept : \n",lin_reg.intercept_)

#the mean squares error
print("Mean squares error : %.2f" % mean_squared_error(Y_test,lin_reg_pred))


#explained variance scorwe :1 is perfect prediction
print('Variance score : %.2f' % r2_score(Y_test,lin_reg_pred))

#plotting graph
plt.scatter(X_test, Y_test, color= 'red')
plt.plot(X_test,lin_reg_pred,color='blue')
plt.title('YEAR VS AGE')
plt.xlabel('YEAR')
plt.ylabel('AGE')

plt.show() 

"""

dataset = pd.read_csv('C://Users/MALVIKA/Desktop/18mcl2/Project_datascience/cyber_Crime2.csv')
X = dataset.iloc[:,1].values #states
print(X)

Y = dataset.iloc[:,3].values #below 18 
print(Y)
#Y = dataset.iloc[:,4].values  #between 18-30  
#Y = dataset.iloc[:,5].values #betweeen 30-45   
#Y = dataset.iloc[:,6].values #between 45-60     
#Y = dataset.iloc[:,7].values #above 60   
#Y = dataset.iloc[:,7].values #Total




X_train, X_test, Y_train,Y_test=train_test_split(X, Y, test_size=1/3, random_state = 0)

#reshaping array to convert from 1D to 2D array
X_test=X_test.reshape(-1,1)
X_train=X_train.reshape(-1,1)


#lin_reg is our model calling model "LinearRegression()"

lin_reg=linear_model.LinearRegression()

#fittring our data in linear regression model
lin_reg.fit(X_train,Y_train)

#making predictions
lin_reg_pred=lin_reg.predict(X_test)

#cof_and intercept_ are cofficients and intercepts resp. for our model
print("Coefficients : \n",lin_reg.coef_)
print("Intercept : \n",lin_reg.intercept_)

#the mean squares error
print("Mean squares error : %.2f" % mean_squared_error(Y_test,lin_reg_pred))


#explained variance scorwe :1 is perfect prediction
print('Variance score : %.2f' % r2_score(Y_test,lin_reg_pred))

#plotting graph
plt.scatter(X_test, Y_test, color= 'red')
plt.plot(X_test,lin_reg_pred,color='blue')
plt.title('STATE VS AGE BELOW 18 YEARS')
plt.xlabel('STATE')
plt.ylabel('AGE BELOW 18 YEARS')

plt.show() 
