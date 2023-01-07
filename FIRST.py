# a=10
# b =20
# print(a+b,"helloworld")

# a = 20
# b=30
# avg =(a+b)/2
# print(avg)

# x =5
# print(x>3 and x > 5)
# print(x>3 or x > 5)

# x = "dbkdk"
# print("z" in x)

# y = 10
# print(y is not 10)

# binary

# x = 10
# print(bin(x))

# x = 10
# print(type(x))

# a = int(input("enter number "))
# b = int(input("enter numnber "))
# c = a+b
# print(c)

# even number

# num = int(input("enter number "))
# if num%2==0:
#     print("Even number ")
# else:
#     print("Odd")    

# num1 = int(input("Enter number : "))
# num2= int(input("Enter number : "))
# op = int(input("Enter operator +,-,/,*: "))

# if op==1:
#     print((num1+num2))
# elif op==2:
#     print((num1-num2))
# elif op==1:
#     print((num1*num2))
# elif op==1:
#     print((num1/num2))
    
# table
# num = 2
# for i in range(1,5):
#     print(num,"*",i,"=",i*num)

# i = 2
# while i<10:
#     print("Welcome to Future ") 
#     i=i+1


# i = 1
# num =2
# while i <= 10:
#     print(num,"*",i,"=",i*num)
#     i=i+1

# String indexing

# w = "welcome to future"

# print(w[0:7])
# print(w[-1])
# print(w[0::2])
# print(w[-1::-1])

# String iteration

# w = "welcome to future"
# t = len(w)
# print(t)
# for w in w:
#     print(w)

# String function

# w = "welcome to future"
# a = w.upper()
# a=w.lower()
# a=w.title()
# a=w.capitalize()
# print(a)

# String func

# a = "welcome"
# print(a.isalpha())
# a="123"
# print(a.isdigit())
# a="welcom123"
# print(a.isalnum())

# Ascii

# a = 67
# print(chr(a))

# b = "a"
# print(ord(b))

# list\
# l1 = [22,33,44,55,11]
# for i in range(len(l1)):
#     print(l1[i])

#list functions

# l1.sort() sorting
# l1.reverse() reverse
# l1.append(22) add in last
# del l[1] delete with index
# l1.pop(2) delete with index return delete last element
# l.remove(11) remover number
# l1.insert(0,23)
# l.clear() clear list
# n =[99,66]
# max()
# min()
# l.extend(n)
# print(l1)

#list practice
# b = input("Enter Fruit : ")
# a = input("Enter Fruit : ")
# c = input("Enter Fruit : ")
# d = input("Enter Fruit : ")

# mylist = [a,b,c,d]
# for i in range(len(mylist)):
#     print(mylist[i])

# Sortd marks

# a = int(input("Enter Number : "))
# b = int(input("Enter Number : "))
# c = int(input("Enter Number : "))
# d = int(input("Enter Number : "))
# mylist=[a,b,c,d]
# mylist.sort()
# print(mylist)
# print(sum(mylist))

#  BLANK LIST
# l = []
# for i in range(1,101):
#     l.append(i)
# print(l)
  
#list comprehension
# l =[i for i in range(1,101)]
# print(l)

#list comprehension for even
# l =[i for i in range(1,101) if i%2==0]
# print("Even numbers are ",l)


# #list comprehension for odd
# l = [i for i in range(1,101) if i%2!=0]
# print("odd numbers are ",l)
#zip function

# l=[11,22,33,44]
# l1=[55,66,77,88]
# for a,b in zip(l,l1):
#     print(a,b)

#string to list
# a = input("Enter")
# l=a.split()
# print(l)

# l=[]
# for i in range(3):
#     n=input("Enter number : ")
#     l.append(n)
# print(l)    

# tuple 
# cannot update
#FIND 1
# a = (1,2,3,4,1,5,7)
# print(a.count(1))
# print(a.index(2))

# d={'name':'Mubashir',"course":"python"} 

# for n in d:
#     print(n)
# #value
# for n in d:
#     print(d[n])    

# mydict = {"pankha":"fan","Dabba":"box"}
# print("choice are",mydict)
# a= input(" Enter Value ")
# print("the meaning of",a,"is",mydict[a])

# d={'name':'Mubashir',"course":"python","fee":800}
# for a,b in d.items():
#     print(a,b) 

# del d["name"]

# d.update({"course":"java"})
# d["new"]=one //update2
# print(d)

#functions

# def showdata():
#     print("Welcome")

# showdata()

# def sum(a,b):
#     print(a+b)

# sum(20, 90)

# square

# def square(x):
#     return x*x 
# s = square(5)
# print(s)     


# #modules
# import math

# x =5
# print(math.factorial(x))

# random

# import random

# r = random.randint(1, 9)
# print(r)

# x =[22,33,44]
# r = random.shuffle(x)
# print(x)

# import datetime

# x = datetime.datetime.now()
# print(x)

#class

# class Democlass:
#     a=10
    
#     def sumvalue(self):
#         print(10+20)

# obj = Democlass()
# print(obj.a)
# obj.sumvalue()

#methods

# class Democlass:
#     def __init__(self):
#         print("Welcome to Future ")
#     a=10
#     def sumvalue(self):
#        self.c=self.a*self.a
#        print(self.c)
#     def sumvalue1(self,a,b):
#         print(a+b)  

# obj = Democlass()
# obj.sumvalue()
# obj.sumvalue1(20, 10)         


# inheritance 

# class A:
#     def displayA(self):
#         print("This is A ")
# class B(A):
#     def displayB(self):
#         print("this is B")
# class C(B):
#     def displayC(self):
#         print("This is C")

# obj = C()
# obj.displayA()

#Encapsulation

# class Student:
#     def __init__(self):
#         self.name=""
#     def getname(self):
#         return self.name
#     def setname(self,name):
#         self.name=name

# obj = Student()
# obj.setname("Ali")
# n=obj.getname()        
# print(n)


