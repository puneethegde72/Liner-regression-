# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 15:36:07 2022

@author: Puneet
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

full_health_data = pd.read_csv("inputdata9.csv", header=0, sep=",")

x = full_health_data["Rainfall"]
y = full_health_data["Productivity"]

slope, intercept, r, p, std_err = stats.linregress(x, y)
print(f"slope= {slope} and c= {intercept}")
print(r)
print(p)
print("std_error=",std_err)

def myfunc(X):
 return slope *X + intercept

mymodel = list(map(myfunc, x))
print(mymodel)

CVx = stats.variation(mymodel, nan_policy="omit")
print("co-effient value of model is", CVx)

r2= r**2
print("R Squre is ",r2)

corilation= full_health_data.corr().loc["Rainfall","Productivity"]

print("corilation of x and y is ", corilation)

y_pred = myfunc(275)

print(f"predicted value of 275 is {y_pred}")

plt.scatter(x, y, c='#008B45', label='Rainfall Vs productivity')
plt.plot(x, mymodel, color='#CD3700', label='Regression Line')
plt.scatter (275, y_pred,c='#68228B', label='Prediction point')
plt.xlabel('Rainfall')
plt.ylabel('Productivity')
plt.title("Rainfall Vs Productivity")
plt.legend()
plt.show()