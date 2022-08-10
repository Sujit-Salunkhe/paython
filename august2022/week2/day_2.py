# from fnmatch import translate
# from traceback import print_tb
# txt="sujit is great person"
# mytxt=txt.maketrans("s","v")
# print(txt.translate(mytxt))
# txt="sujit is great person"
# print(txt.partition("great"))
# txt="sujit is great person"
# print(txt.replace("sujit","only sujit"))
# txt="sujit is great person"
# print(txt.rfind("sujit",8,10))
# txt="sujit is great person"
# print(txt.rindex("s"))
# txt="sujit is great person"
# print(txt.rsplit(",",1))
# txt="sujit is great person".split()
# print(txt)
# txt="sujit is great person"
# txt="sujit, is great ,person"
# print(txt.split(","))
# txt="sujit \nis great person"
# print(txt)
# print(txt.splitlines(True))
# txt="sujit is great person"
# # print(txt.startswith("sujit"))
# from traceback import print_tb
# txt="sujit is great person"
# print(txt.strip(".,g"))
# c=("sujit",)
# print(type(c))
# a="sujit"
# list=[1,2,3,2,5,5]
# list.append(4)
# print(list)
# txt="sujit is great person"
# print(txt.swapcase())
# txt="sujit is great person"
# print(txt.title())
# txt="sujit  is great person"
# a="vais h n a v"
# print(txt.translate(a))
# txt="sujit is great person"
# print(txt.upper())
# txt="sujit is great person"
# print(txt.capitalize())
# txt="sujit is great person"
# print(txt.lower())
# txt=".10"
# print(txt.zfill(100))
# price=100
# txt="the price of vada pav is {}".format(price)
# # print(txt)
# list=[1,2,3,45,5,45,5,5,54][1:6]
# # print(list)
# from xmlrpc.client import boolean


# def digrams(a):
#     b=input("select 1 or 0\n")
#     p=1
#     if  b=="1":
#         while p<=a:
#             print ("@"*p)
#             p +=1
#     else:
#         while p<=a:
#             print("@"*a)
#             a -=1
# # a=digrams(int
# for x in range(1,10):
#     if x==3:
#         continue
# #     print(x)
# list=[1,2,3,4,5,6,7,8,9]
# p=0
# while p < len(list):
#         p +=1
#         if p==2:
#             continue
#         print(list[p]) 
from ntpath import join
import textwrap


# n="sujitkfjkd"
# # s="test"
# a=2
# # print("\n".join(textwrap.wrap(n,a)))
# x="\n".join(textwrap.wrap(n,a))
# print(x)
# # n=7
# print("hello".center(9,"-"))
# n=7
# m=21
# # print(".|.".center(m,"-"))
# n="sujit"
# m=4
# # print("\n".join(textwrap,wrap(n,m)))
# x="\n".join(textwrap,wrap(n,m))
# print(x)
# x="sujit"
# y=2
# print((textwrap.wrap(x,y)))
n=9
m=27
for x in range(1,n,2):
    # x +=1
    y=x*".|."
    print(y.center(m,"-"))
print("welcome".center(m,"-"))
for x in range(n-2,-1,-2):
    print("x:",x,"n:",n)
    y=x*".|."
    print(y.center(m,"-"))
# a,b=map(int,input().split())
# print(a)
# # print(b)
# for x in range(9,-1,-2):
#     print(x)


