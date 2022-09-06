from cgi import print_directory
import numbers
from re import A


# k=3
# m=1000
# t=list()
# f=list()
# for i in range(k):
#         numbers=list(map(int,input().split()))
#         numbers.pop(0)
#         t.append(max(numbers))
# def doubler(a):        
#     for x in a:
#         f.append(x * x)        
#     return(sum(f)%1000)
# # print(doubler(t))
# k,m=list(map(int,input().split()))
# t=list()
# f=list()
# for i in range(k):
#         numbers=list(map(int,input().split()))
#         numbers.pop(0)
#         t.append(max(numbers))
# def doubler(a):        
#     for x in a:
#         f.append(x * x)        
#     return(sum(f)%m)
# print(doubler(t))
a=1
b=10
c=100
d=1
# list=[a ,b,c,d]
# min=min(list)
# max=max(list)
# print(max - min)
# n=2
# total=list()
# for i in range(1,n+1):
#     if (n % i ==0):
#         total.append(i)

# print(len(total))
def catAndMouse(x, y, z):
    if z < x and z < y:
        a=x-z
        b=y-z
        if a > b:
            return("Cat B")
        elif a < b:
            return("Cat B")
        else:
            return ("Mouse C")
    if z > x and z > y:
        a=z-y
        b=z-x
        if a > b:
            return("Cat B")
        elif a < b:
            return("Cat B")
        else:
            return ("Mouse C")
    if z > x and z < y:
        a=z-x
        b=y-z
        if a > b:
            return("Cat B")
        elif a < b:
            return("Cat B")
        else:
            return ("Mouse C")
    if z < x and z > y:
        a=x - z
        b=z-y
        if a > b:
            return("Cat B")
        elif a < b:
            return("Cat B")
        else:
            return ("Mouse C")
        
   
print(catAndMouse(1,2,3))
print(catAndMouse(1,3,2))
print(catAndMouse(5,78,100))




    

