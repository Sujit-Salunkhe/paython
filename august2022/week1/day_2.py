# we have to watch 24,25,26 of code with harry
from functools import reduce
from logging import exception
import numbers
from tokenize import Number
from xml.sax.saxutils import prepare_input_source

from click import secho



# def guess_number(n):
#     guess=1
#     while guess <= 10:
#         number=int(input("guess your number"))
#         if number < n:
#             print("your number is small")
#         elif number > n:
#             print ("your number is big")
#         else:
#             print("your guess is perfect you won buddy")
#             break
#         print("you left with a",10-guess,"guesses")
#         guess += 1
#     if guess>10:
#         print("you lost")
# guess_number(10)
# num=5
# cube=lambda x: x **3
# def fibnomic(n):
#     lis = [0,1]
#     for i in range(2,n):
        
#         lis.append(lis[i-2] + lis[i-1])
#     return(lis[0:n])
# print(fibnomic(5))      
# so he did make alis of 0 and 1 lis[2-2]+lis[2-1]
# lis[0]+lis[1]
# lis[1]+lis[2]
# lis = [0,1]
# n=3
# lis=[0,1]
# for i in range(2,n):
#     lis.append(lis[i-2] + lis[i-1])
# print(lis[0:n])
# def docstring(n):
#     """this is example of doc string"""
#     pass
# # print(docstring.__doc__)
# a=(input())
# b=(input())
# try:
#     print(int(a)+int(b))
# except Exception as e:
#     print(e)
# print("inportant")
# a=any([1==0])
# # print(a)
# lis=[["haeey",30],["beta",50],["seta",40],["apte",90]]
# mark=[]
# for x in lis:
#     mark.append(x)
# print(mark)
# mark.sorted()
  
# lis.sort()
# print(lis)
# marksheet=[]
# for x in range(0,int(input)):
#     marksheet.append([input(),float(input())])
# #     second_lowestgrade=sort()
# m= {2, 4, 5, 9}
# for x in m:
#     t=x
#     print(x)

# n={2, 4, 11, 12}
# for y in n:
#     s=y
#     print(y)

# n={"a","b","c","d","e"}
# m={"a","c","d","f","h","z"}
# x=n.symmetric_difference(m)
# print("\n".join(sorted(x,key=int)))
# def fibnomical(n):
    
#     for i in range(n):
#         a=range(n)
#         nums=reduce(lambda x,y:x+y,a)
#         return nums
        
# print(fibnomical(5))