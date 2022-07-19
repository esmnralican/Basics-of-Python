# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 10:50:14 2022

@author: esmnralican
"""
#%%
#VARIABLES 6
# variable(değişken) / Python'ın temelinde 3 farklı component vardır: / Değişken tanımlamada boşluk olmaz

#variable
#function
#object

var1= 10 #integer
var2= 15#integer

var3 = "monday"#string

var4= 10.0 #double

#syntax kuralı : Tanımlanan değişkenin başına sayı gelmez '5var' olmaz, bunun yerine 'var5' olmalı. Ayrıca tanımlama büyük hatfle başlayamaz. 

#%%
#STRING 7
s = "today is tuesday"

variable_type = type(s) # str
uzunluk = len(s) #python'da değerler 0'dan başlanarak sayılır
#%%
#NUMBERS 8
integer_deneme = -50
float_deneme = -30.7
float = 10
#%%
#QUIZ SORULARI 
   
'100' + '200'
Out[29]: '100200'



3 + '3'
Traceback (most recent call last):

  File "C:\Users\ESMNRA~1\AppData\Local\Temp/ipykernel_8640/238351767.py", line 1, in <module>
    3 + '3'

TypeError: unsupported operand type(s) for +: 'int' and 'str'


'5'*5
Out[31]: '55555'
#%%
#BBUILT-IN FUNCTIONS 9 

str1 = "deneme"
float = 30.7

str2 = "1005"

#MANTIĞI : output = typr(parametre(input)) = type(int(str2)) Out[38]: int

#%%
var1 = 20
var2 = 50
output = (((var1+var2)*50/100.0)*var1/var2)

#function parameter = input
def my_first_function(a, b):
    """
    this is my first try
    parametre: 
    return:
    """
    output = (((var1+var2)*50/100.0)*a/b)
    return output

sonuc = my_first_function(var1, var2)

#var1 = a ve var2 = b oluyor


def ():
    print("It's return nothing.")
    
#%%
# DEFAULT ve FLEXIBLE FUNCTIONS 
# Default : zaten tanımlı ifadeleri tekrar tekrar yazmanın önüne geçiliyor.  

#çemberin çevre uzunluğu= 2*pi*r

def circumference_of_the_circle(r, pi=3.14):
   """
   input(parametre):r
   output = circumference_of_the_circle
   """
   output = 2*pi*r
   return output

# Flexible :
def calculate(weight, height):
    output = weight + height
    return output

# def calculatee(weight, height, age):
#     output = (weight + height) * age
#     return output
    
def calculatee(weight, height, *args): #boy ve kilo parametreleri kesin olmalı, istenirse ek bir şeyler eklenebilir
    print(len(args))
    output = (weight + height) 
    return output
    
#%%*
#QUIZ

#int variable yas , stringname ad ,  fonksiyon olucak , fonksiyon print(type(),Len,float(),*args soyisim , default parametre ayakkabı numarası)

yas = 10
name = "kaan"
soyisim = "kalın"
def function_quiz(yas, name, *args, ayakkabi_numarasi=35):
    print("Çocuğun adı:",name ,"Cocuğun yaşı:",yas , "Çocuğun ayak numarası:",ayakkabi_numarasi)
    print(type(name))
   # print(float(yas))

    output = args[0]*yas

    return output 

sonuc = function_quiz(yas, name, soyisim)

print("args[0]*yas:" ,sonuc)


#%%
# Lambda function

def hesapla(x):
    output = x*x
    return output
sonuc = hesapla(3)
print(sonuc)

sonuc2 = lambda x: x*x
print(sonuc2(3))

#%%
#List

list = [1,2,3,4,5]
list_str = ["monday", "tuesday", "wednesday"]
type(list_str)

#python'da listeler 0'dan başlar.

value = list[0]
print(value)

#list[-1] : sondaki elemanı verir.
value = list[-1]
print(value)

#listenin ilk elemanında başla, 3. eleman dahil değil
list[0:3]

#dir(list) : hangi işlemlerin yapılabildiğini gösterir.

#help(list.append) : append fonksiyonunun ne yapdığını anlatır.
list.append(8) #liste sonuna 8 eklendi.

string_int_liste = [1,2,3,"aa","bb"]

#%%
#Tuple
t = (1,2,3,4,5,6)

t.count(5) #liste içinde  5'den kaç adet var
t.index(5) #5'in indexini bulur

#%%
#Dictionary
dictionary = {"ali":12, "veli":15}

#ali, veli = keys    |      12, 15 = values

def deneme():
    dictionary = {"ali":12, "veli":15}
    return dictionary
dic = deneme()

#QUIZ SORUSU
a = "sakin calismaktan vazgecmeyin"

a[1]+a[0]+a[8]+a[1] + " " + a[-11:]
#Output = 'asla vazgecmeyin'


d1 = {"datai" : 40,"team" : 45}

d2 = {"datai" : 55,"team" : 45}
# d1==d1 ? answer = False 

#%%
#Conditionalas
var1 = 10
var2 = 20
if(var1 > var2):
    print("var1 > var2")
elif(var1==var2):
    print(" var1 = var2")
else:
    print("var1 < var2")    
    
    
liste = [1,2,3,4,5]

if 6 in liste:
    print("6 listede var")
else:
    print("hayır")    
 
    
        
liste = [1,2,3,4,5]

if 3 in liste:
    print("{} listede var".format(value))
else:
    print("hayır")    
    

keys = dictionary.keys()

if "ali" in keys:
    print("evet") 
else:
    print("hayır")    

#%%
#VİDEO QUIZ
#1648. yıl = 17. yüzyıl

#metod yazın
    #input int yıllar
    #output yüzyıl
    #input year >>1 <= year <=2005
    
def year2centruy(year):

    str_year = str(year)

    if(len(str_year)<3):
        return 1
    elif(len(str_year) == 3):
        if(str_year[1:3] == "00"):
            return int(str_year[0])
        else:
            return int(str_year[0])+1
    else:
        if(str_year[2:4]=="00"):
            return int(str_year[:2])
        else:
            return int(str_year[:2])+1
            
    

#%%
## for Loop
for each in range(1,11):
    print(each)
    
for each in "ankara ist" :
    print(each)    
    
for each in "ankara ist".split(): 
    print(each) 
    
liste = [1,2,3,4,5,6] #sum(liste):21 

summation = sum(liste)

count = 0
for each in liste:
    count =count + each
    print(count)
    
#%%
## while Loop 
i =0
while(i<4):
    print(i)
    i = 1 + i
    
sinir = len(list)    
each = 0
count = 0
while (each < sinir ):
    count = count + liste[each]
    each = each + 1
#OUTPUT : count =21  

#%%
#VIDEO QUIZ
#tanımlanan listedeki en küçük elemanı bulma

liste = [1,23,3,4,5,6,-455,78]  

mini = 10000
for each in liste:
    if(each < mini):
        mini = each
    else:
        continue

#%%
#CLASS
class Worker:
    raise_rate = 1.8
    counter = 0
    
    def __init__(self,name,surname,salary): #constructor
        self.name = name
        self.surname = surname
        self.salary = salary
        self.email = name+surname+"@gmail.com"
      
        Worker.counter = Worker.counter + 1
      
      
      
    def giveNameSurname(self):
        return self.name+" "+self.surname
    
#employee1 = Worker("jane", "dennis", 100)        
#print(employee1.giveNameSurname())        

    def give_a_raise(self):
        self.salary = self.salary + self.salary*self.raise_rate

#Class variable
employee2 = Worker("jane", "dennis", 100) 
print("First salary : " , employee2.salary) 
employee2.give_a_raise()
print("New salary :" ,employee2.salary)


employee3 = Worker("adam", "smith", 500)  
employee4 = Worker("selena", "benjamin", 300)  
employee5 = Worker("alec", "mendes", 600)  
     
#Class EXAMPLE
liste = [employee2,employee3,employee4,employee5]
   
max_salary = -1
index = -1
for each in liste:
    if(each.salary>max_salary):
        max_salary = each.salary
        index = each
        
print(max_salary)  
print(index.giveNameSurname())     

#%%
# SINAV 6
#soru1
class A:

    global a

    a = 5

    def __init__(self,x = 4):

        self.x = x

    def sum(self):

        return a + self.x

x = A(5)

x.sum()
#soru3
class DataiTeam:

    def __init__(self, x = "hi"):

        self.x = x

    def show(self):

        print(self.x)

my_class = DataiTeam()

my_class.show()

#%%
#Try-Except1-2
#python ilk olarak yazım(syntax) hatalarının varlığını kontrol eder
a = 10
b = "2"
liste = [1,2,3]
print(sum(liste))
#print(a+b) #hatalı
print(str(a)+b)#string ve int değer toplanıyor

k=10
print(k/0)

zero=0
k=10
if(zero==0):
    a=0
else:
    a=k/zero    


try:
    a= k/zero
except ZeroDivisionError:
    a = 0    

#index error
list1 = [1,2,3,4]
list1[15] #out of index hatası , 15. index listede yok

#module not found error
import numpyyy #numpyyy adlı kütüphane yok

#file not found error
import panas as pd 
pd.read_csv("asd") #asd isimli dosya yok

#type error
"2" + 2 #iki farklı tür toplanamaz

#value error
int("sad") #sad int değere dönüştürülemez


try:
    1/0
except:
    print("except") 
else:
    print("else")
finally:
    print("done")    
 #except done   

try:
    1/1
except:
    print("except") 
else:
    print("else")
finally:
    print("done")    
#else done   


#Python: Yapay Zeka için Python Programlama (1) FIRST PART







   