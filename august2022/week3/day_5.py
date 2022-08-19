# t,u=input().split()
# print(t)
# print(u)
# s=[1,2,3,4,5,6,7,8,9]
# a.pop()
# a.remove(9)
# print(a)
# # s=[]
# for i in range(int(input())):
#     t=str(input()).split()
#     if t[0]=="pop":
#        s.pop()
#        print(s)
#     elif t[0]  =="remove" and t[1] in s: 
#         s.remove(t[1]) 
#         print(s)
#     elif t[0]  =="discard" and t[1] in s: 
#         s.discard(t[1])
# #         print(s)
# print (1 in s)
# h=str(input()).split()
# print(h[1])
# print(h 
# [0])

# if h[0]=="remove":
#     s.remove(h[1])
# print(s)
# # print(h[])
# # gr=getattr
# n = int(input())
# s = set(map(int, input().split()))
# for i in range(int(input())):
#         t=str(input()).split()
#         if t[0]=="pop":
#             s.pop()
#             print(s)
#         elif t[0]=="remove":
#             a=int(t[1]) 
#             s.remove(a) 
#             print(s)
#         elif t[0]=="discard" and t[1] in s: 
#             s.discard(t[1])
# # print((s))
# s = set(map(int, input().split()))
# for i in range(int(input())):
#         t=str(input()).split()
#         a=int(t[1])
#         if t[0]=="pop":
#             s.pop()
#         elif t[0]=="remove" and a in s: 
#             s.remove(a)
#             print(s) 
#         elif t[0]=="discard": 
#             g=int(t[1])
#             s.discard(g)
# print(s)
# # t=["remove","4"]
# # if t
class employee:      

    def __init__(self,name,work,leaves) -> None:
        self.name=name
        self.work=work
        self.leaves=leaves
        
    def pprint(self):
        return f"name is {self.name} work hours is {self.work} hours"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

    @classmethod
    def s_t_r(cls,string):
        p=string.split("-")
        # return cls (p[0],p[1],p[2])
        return cls (*string.split("-"))
    @staticmethod
    def printgood(string):
        print("i am  a good boy" + string)
    

# def function (arr):
#     p=0
#     arr=t
#     t=arr
#     s=[]
#     while p<len(arr):
#         arr.remove(arr[p])
#         s.append(sum(arr))
#         p +=1
#     print (s)

# t=a
# c = a.remove(8)
# print(c)
# s=[]
# s.append(sum(a))
# print(s)
# print(t[0])
# print(a)
# function(a)


# function(a)
# def sujit(arr):
#     for i in  range(len(arr)):
#         arr.remove(arr[i])
#         # print(i)
# a=[1,2,6,8,9,7,5,78]
# sujit(a)
# for i in range(4):
#     print(i)

a=[1,2,3]
def function(arr):
    p=0
    s=[]
    while p<len(arr):
        c=sum(arr)-arr[p]
        s.append(c)
        p +=1
    return min(s),max(s)
print(function(a))
