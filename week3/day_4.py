from email.quoprimime import body_check
import numbers
from operator import truediv
import re
from unicodedata import name
# sujit is a good boy.
# yuvraj salunkhe is my father.
# surekha salunkhe is my mother.
# a={"fish":"grey","apple":"red","orange":"green"}
# name=input("what is your value")
# print(a[name])
# thisdict = {"apple": "banana", "cherry": "graphs"}
# b = input()
# print(thisdict[b])
# # 56*7=786, 2/2=1000, a=b=1
# def factorial(n):
#     fac=1
#     for i in range(n):
#         fac = fac * (i+1)
#     return fac
# number=int(input("enter your number"))
# print(factorial(number))
# print(range(number))
# def factorial_recurisive(n):
#         if n==1:
#          return 1
#         else:
#             return n * factorial_recurisive(n-1) 
# def fibonachi(n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fibonachi(n-1) + fibonachi(n-2) 
# number=int(input())
# # print(fibonachi(number))
# cards=[13,9,8,7,5,4,3,2,1]
# query=7
# output=3
# def locate_carde(cards,query):
#     pass

# test=[{"input": {"cards":[13,45,85,69,789,78],"query":45}
# ,"output":1}]
# test2=[{"input":{"cards":[45,85,96,25,46,],"query":"25"},
# "output":"3"}]
# test.append(test2)
# print(test)
def locate_card(cards,query):
    position=0
    while True:
        if cards[position]==query:
            return position
        position += 1
        if position==len(cards):
            return -1

input=[13,45,85,69,789,78,]
query=90

print(locate_card(input,query))


