# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 15:39:34 2022

@author: Puneet
"""
'''The below code will create linear regression and predict productivity based on the rainfall'''
#importing all the required libreries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Reading file with pandas
leni=pd.read_csv("inputdata9.csv")

#assigning values for a new variable to make it easier to utilise
indipendent_value=leni["Rainfall"]
dependent_value= leni["Productivity"]

# Mean indipendent_value and dependent_value
mean_ind = np.mean(indipendent_value)
mean_dep = np.mean(dependent_value)

# Total number of values
n = len(indipendent_value)

#Using the formula to calculate m and c
numer = 0
denom = 0
for i in range (n):
    numer += (indipendent_value[i] - mean_ind)*(dependent_value[i] - mean_dep)
    denom += (indipendent_value[i] - mean_ind) ** 2
m = numer / denom
c = mean_dep - (m * mean_ind)
# Print coefficients
print (f"Slope of the linear regression is {m}")
print(f"Intersept of the linear regression line is {c}")


#y = (m*x)+c
def myfunc(x):
    y = m * x + c
    return y

mymodel = list(map(myfunc,leni["Rainfall"]))
print(f"the points of the linear regression line is /n {mymodel}")

# value of rainfall which needed to be predicted
x = 275

#predicting the prodactivity of the railfall x
y_pred = myfunc(x)
print(f"predicted value of {x} is {y_pred}")

'''Ploting a visualization of linear regression'''
plt.figure()
# Ploting Scatter Points
plt.scatter(leni["Rainfall"], leni["Productivity"], c='#008B45', label='Rainfall Vs productivity')

#Ploting linear regression line Line
plt.plot(indipendent_value, mymodel , color='#CD3700', label='Regression Line')

#Ploting the prediction point in linear regression
plt.scatter (275, y_pred,c='#68228B', label='Prediction point')

#labeling X and Y axis
plt.xlabel('Rainfall')
plt.ylabel('Productivity')

#Setting title for the plot
plt.title("linear refresion for Rainfall and Productivity")

plt.legend()
plt.show()

