# a=eval(input("enter your first number"))
# b=eval(input("enter second number"))
# c=a + b
# print(c)

# class a:
#     def __init__(self):
#         pass
#     def __str__(self) -> str:
#         return "print"
#     def __repr__(self) -> str:
#         return "print4"
# A=a()
# print(A)
# print(repr(A))
# txt="meduvada{}".format(5)
# print(txt.format(5))
# print(txt)
# a="suji"
# b="ashu"
# print(a>b)


# """
# creating a big data base for 100 millon users
# insert=the profile information for a new user.
# find=the profile information of a user given their usernames
# update=the profile information of  a user,given their username 
# list =all the users of the platform,sorted by username 
# """
# class userdatabase:
#     def __init__(self):
#         self.user=[]git 
    

#     def insert(self,user):
#         pass
        
#     def find(self,username):
#         pass
#     def update(self,user):
#         pass
#     def list_all(self): 
# #          pass
# class user:
#     def __init__(self,username,name,email):
#         self.username=username
#         self.name=name
#         self.email=email
#     def _repr_(self):
#         return "user(username='{}',name='{}',email='{}')".format(self.username,self.name,self.email)
#     def __str__(self):
#         return self._repr_()
# sujit=user("sujit4950","sujit","sujitsalunkhe@gmail.com")
# vaishnav=user("vaishnav45","vaishnav","vaishnav45@gmail.com")
# suraj=user("suraj09","suraj","suraj@gamil.com")
# roshan=user("roshan09","roshan","roshan@gamil.com")
# devi=user("devi09","devi","devi@gamil.com")
# rohit=user("rohit09","rohit","rohit@gamil.com")
# user=[sujit,vaishnav,suraj,roshan,devi,rohit,]
# print(list(map(str,user)))
# print(user)
# def fuc():
#     x=300
#     def printer():
#         print(x)
#     printer()
# fuc()
# from collections import namedtuple

# from python.week4.day_3 import sujit


from collections import namedtuple


a=namedtuple("sujit","vaishnav")
a.__dict__