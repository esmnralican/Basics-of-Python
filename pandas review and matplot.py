# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 22:11:30 2022

@author: esmnralican
"""

#matplotlib görselleştirme kütüphanesi
#line plot, scatter plot, bar plot, subplots, histogram

import pandas as pd

df = pd.read_csv("iris.csv")
print(df.columns)
print(df.Species.Unique())
print(df.info())
print(df.descrie())

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]

print(setosa.describe())
print(versicolor.describe())

#%%
#Line Plot - Görselleştirme
import matplotlib.pyplot as plt

df1 = df.drop(["Id"],axis=1)

#görselleştirme
df1.plot()
plt.show()

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.plot(setosa.Id , setosa.PetalLengthCm, color = "red", label= "setosa" )
plt.plot(versicolor.Id , versicolor.PetalLengthCm, color = "green", label= "versicolor" )
plt.plot(virginica.Id , virginica.PetalLengthCm, color = "blue", label= "virginica" )


plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()
plt.show()

df1.plot(grid = True)
plt.show()

df1.plot(grid = True, linestyle = ":")
plt.show()

df1.plot(grid = True, alpha =0.1)
plt.show()

#%%
#sctter plot

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.scatter(setosa.PetalLengthCm, setosa.PetalWidthCm, color="red", label="setosa")
plt.scatter(versicolor.PetalLengthCm , versicolor.PetalWidthCm, color = "green", label= "versicolor" )
plt.scatter(virginica.PetalLengthCm , virginica.PetalWidthCm, color = "blue", label= "virginica" )
plt.legend()
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.title("scatter plot")
plt.show()

#%%
#histogram plot
plt.hist(setosa.PetalLengthCm, bins=10)
plt.xlabel("PetalLengthCm")
plt.ylabel("frekans")
plt.title("hist")
plt.show()

#%%
#Bar Plot
import numpy as np
x = np.array([1,2,3,4,5,6,7])
y=x*2+5
plt.bar(x,y)
plt.title("bar plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
#%%
#subplot

df1.plot(grid = True, alpha =0.1, subplots=True) 
plt.show()


setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.Subplot(2, 1, 1)
plt.plot(setosa.Id , setosa.PetalLengthCm, color = "red", label= "setosa" )
plt.ylabel("setosa -PetalLengthCm")

plt.Subplot(2, 1, 2)
plt.plot(versicolor.Id , versicolor.PetalLengthCm, color = "green", label= "versicolor" )
plt.ylabel("versicolor -PetalLengthCm")
plt.show()
















