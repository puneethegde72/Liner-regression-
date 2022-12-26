# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 15:39:34 2022

@author: Puneet
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

leni=pd.read_csv("inputdata9.csv")

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
print (m, c)


#y = (m*x)+c
def myfunc(x):
    y = m * x + c
    return y

mymodel = list(map(myfunc,leni["Rainfall"]))
print(mymodel)

y_pred = myfunc(275)

print(f"predicted value of 275 is {y_pred}")
plt.figure()
#Ploting Line
plt.plot(indipendent_value, mymodel , color='#CD3700', label='Regression Line')
# Ploting Scatter Points
plt.scatter(leni["Rainfall"], leni["Productivity"], c='#008B45', label='Rainfall Vs productivity')
plt.scatter (275, y_pred,c='#68228B', label='Prediction point')

plt.xlabel('Rainfall')
plt.ylabel('Productivity')
plt.title("Rainfall Vs Productivity")
plt.legend()
plt.show()

