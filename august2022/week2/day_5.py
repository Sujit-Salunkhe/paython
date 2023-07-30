# a=["bimdi","aluuu","javascript","zandu","pzdu"]
# for x,y in enumerate(a):
#     if x % 2==0:
#         print(y)

# for x in range(len(a),2):
# #     print(x)
# s="you are in love or what "
# for x in s:
# #     print(x.join())
# lis=["john","sina","mina","reena"]
# # print(lis.join("@"))
# print(" and ".join(lis))
# # print(a)
# a=[45,545,5,5,45,5,4,54,646647,6]
# for x,y in enumerate(a):
#     print(x,y)    
from re import T
from turtle import position


# s="sujit"
# position=1
# letter = "h"
# # s[0]="h"
# print(s[0])
# a=s[0]
# print(a)
# # b=s.replace(a,letter)
# # print(b)
# def change(string,position,letter):
#     a=string[position]
#     print(string.replace(a,letter))

# change("abracadabra",5,"k")
# c="abracadabra"
# print(c[5])

# print(c.replace(a,"k"))
# a="sujit"
s="this is string"
position=6
letter = "h"
b=s[:position] + letter +s[position + 1:]
print(b)
a=s[0:2]
print(a)