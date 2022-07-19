# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 13:11:34 2022

@author: esmnralican
"""
#numpy basics
import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10]) #numpy ın array metodu çağırılarak array oluşturuluyor 
print(array.shape)

a = array.reshape(2,5)
print("shape:",a.shape)
print("dimension:", a.ndim)

print("data type:" , a.dtype.name)
print("size:", a.size)

print("type: " , type(a))

array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

np.zeros((3,4)) #3'e 4'lük (dik-yatay) 0'lardan oluşan bir matris tanımlanır, buna allocation' da denir

zeros = np.zeros((3,4))
zeros[0,0] = 5
print(zeros)
#zeros array'nin [0,0] indisi 5 oldu

np.ones((3,4))
np.empty((3,4)) #python dizi elemanlarını sıfıra çok yakın sayılar şeklinde döndürür bu dizinin boş olduğu anlamına gelir

a = np.arange(10,50,5)
print(a)  #array([10, 15, 20, 25, 30, 35, 40, 45])


a=np.linspace(10,50,20 )
print(a)  # 10-50 arası rastgele 20 sayı yazdırır (virgüllü)

#%%
#numpy basic operations
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a+b) #[5 7 9]
print(a-b) #[-3 -3 -3]
print(a**2) #karesini al [1 4 9]

print(np.sin(a)) #sinüs

print(a<2) #[ True False False]

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2,3],[4,5,6]])


#element wise product
print(a*b) #[[ 1  4  9]
           # [16 25 36]]
  
#matrix product
a.dot(b.T)   #array([[14, 32],
             #       [32, 77]])  
             
a = np.random.random((5,5))# 5'e 5'lik 0'dan 1'e random  sayı oluşturur        
print(a.sum())
print(a.max())     
print(a.min())   

print(a.sum(axis=0)) #sütünları topla
print(a.sum(axis=1)) #satırları topla
       
print(np.sqrt(a)) # karekök
print(np.square(a)) # a**2
# print(np.add(a,a)) = a+a


#%%
#indexing and slicing
array = np.array([1,2,3,4,5,6,7]) # index 0'dan başlar | vector dimension = 1

print(array[0])
print(array[0:4])

reverse_array = array[::-1]
print(reverse_array)

array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(array1[:,1]) # [2 7]
print(array1[1,]) # [ 6  7  8  9 10]
print(array1[1,1:4]) # [7 8 9]
print(array1[1,:]) # [ 6  7  8  9 10]
print(array1[:,-1]) # [ 5 10]

#%%SHAPE MANIPULATION
array = np.array([[1,2,3],[4,5,6],[7,8,9]])

#flatten
a = array.ravel() #3x3'lük matris vektör haline getirildi
array2 = a.reshape(3,3)

arrayT = array2.T
"""
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])

Transpoz = 147
           258
           369
"""
print(arrayT.shape) # dizi boyutu değiştiriliyor

array3 = np.array([[1,2],[4,5],[7,8]])

#reshape : bir değişkene atılmalı resize:direk boyutu değiştiriyor

#%%STACKING ARRAYS

array1 = np.array([[1,2],[4,5]])            
array2 = np.array([[-1,-2],[-4,-5]])

#vertical
array2 = np.vstack((array1,array2))
"""array([[ 1,  2],
       [ 4,  5],
       [-1, -2],
       [-4, -5]])
"""
#horizontal
array2 = np.hstack((array1,array2))
"""array([[ 1,  2, -1, -2],
       [ 4,  5, -4, -5]])
"""

#%%
# CONVERT and COPY

liste = [1,2,3,4] #list
array = np.array(liste) #np.array

liste2 = list(array)

#a değğeri değiştiğinde b ve c de değişir
a = np.array ([1,2,3])
b = a
c = a

#birbirlerinden etkilenmezler
d = np.array([1,2,3])
e = d.copy()
f = d.copy()























