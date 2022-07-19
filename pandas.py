# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 16:38:36 2022

@author: esmnralican
"""

#1) pandas hızlı ve etkili for dataframes
#2) csv ve text dosyalarına açıp inceleyip sonuçlarımızı da bu dosya tiplerine rahat bir şekilde kaydedebiliriz
#3) NaN (missing data) için işleri kolaylaştırıyor
#4) reshape yapıpdata yı daha etkili bir şekilde kullanabiliriz
#5) slicing indexing kolay
#6) time series data analizinde çok yardımcı
#7) gerçekten çok hızlı (optiimize edilmiş)

import pandas as pd

dictionary = {"NAME": ["jane","alec","shawn","david","max","finn"],
              "AGE":[11,22,3,44,7,8],
              "SALARY": [100,233,345,45,634,333]}

dataFrame1 = pd.DataFrame(dictionary)

head = dataFrame1.head()#ilk 5 satırı ver
tail = dataFrame1.tail()#son satırı ver

#%%
#pandas basic methods
print(dataFrame1.columns)
print(dataFrame1.info())
print(dataFrame1.dtypes)
print(dataFrame1.describe()) #numeric feature = columns(age,salary)

#%%
#indexing and slicing
print(dataFrame1["NAME"])

print(dataFrame1["AGE"]) #print(dataFrame1.AGE)

dataFrame1["new_feature"] = [-1,-2,-3,-4,-5,-6]
print(dataFrame1.new_feature)

print(dataFrame1.loc[:, "AGE"])

print(dataFrame1.loc[:3,"AGE"] )

print(dataFrame1.loc[:3, "AGE":"NAME"])

print(dataFrame1.loc[:3, ["AGE","NAME"]])

print(dataFrame1.loc[::-1,:])

print(dataFrame1.loc[:,:"NAME"])

print(dataFrame1.loc[:,"NAME"])

print(dataFrame1.iloc[:,2]) #iloc: integer location

#%%
#filtering

filtre1 = dataFrame1.MAAS >200
filtelenmıs_data = dataFrame1[filtre1]

filtre2 = dataFrame1.AGE < 20
dataFrame1[filtre1 & filtre2]

print(dataFrame1[dataFrame1.AGE > 60])

#%%
#list comprehension
mean_value = dataFrame1.MAAS.mean() #ort maaş

#ort>maas yuksek & ort<maas dusuk
dataFrame1["maas_seviyesi"] = ["dusuk" if mean_value > each else "yuksek" for each in dataFrame1.MAAS]



for each in dataFrame1.MAAS:
    if(mean_value>each):
        print("dusuk")
    else:
        print("yuksek")

dataFrame1.columns


dataFrame1.columns = [each.lower() for each in dataFrame1.columns] #column adlarının hepsini küçük harfe dönüştürdü

dataFrame1.columns = [each.split()[0]+"_"+each.split()[1] if(len(each.split())>1) else each in dataFrame1.columns] #yeni deneme -> yeni_deneme oldu
#%%
#drop and concatenating
dataFrame1.drop(["new_feature"],axis=1,implace = True # new_feature silindi
 
# dataFrame1 = dataFrame1.drop(["new_feature"],axis=1)
 

data1 = dataFrame1.head()
data2 = dataFrame1.tail()

#vertical olarak birleştirme
data_concat = pd.concat([data1,data2],axis=0)

#horizontal olarak birleştirme
maas = dataFrame1.maas
age = dataFrame1.age

data_h_concat = pd.concat([data1,data2],axis=1)

#%%SINAV 16
dictionary = {"NAME":["ali","veli","kenan","hilal","ayse","evren"],

              "AGE":[15,16,17,33,45,66],

              "MAAS": [100,150,240,350,110,220]}

dataFrame1 = pd.DataFrame(dictionary)

data1 = dataFrame1.head()

data2 = dataFrame1.tail()

pd.concat([data1,data2],axis=0)
            
"""
  NAME  AGE  MAAS
0    ali   15   100
1   veli   16   150
2  kenan   17   240
3  hilal   33   350
4   ayse   45   110
1   veli   16   150
2  kenan   17   240
3  hilal   33   350
4   ayse   45   110
5  evren   66   220
"""
#%%
#TRANSFORMING DATA
dataFrame1["list_comp"] = [each*2 for each in dataFrame1.AGE]

#apply
def multiply(AGE):
    return AGE*2

dataFrame1["apply_metodu"] = dataFrame1.AGE.apply(multiply)




























