# # l=10
# def functio(n):
#     global l
#     l = 6 
#     print(l)
#     print(n,"printed")
# functio("sujit")
# # print(l)
# def function():
#     x=20
#     def sujit():
#         global x
#         x=38
#     print("before calling",x)
#     sujit()
#     print("after calling",x)
# function()
# # print(x)
# def factorial(m):
#     fac=1
#     for x in range(1,m+1):
#         fac = fac * (x)
#     return fac
# print(factorial(int(input("enter a number"))))
# for i in range(5):
# #     print(i)
# def factorial(n):
#     z=n
#     while z <=n: 
#         a = n*(z-1)
#         z -=1
# #     return a
# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(int(input("enter a number"))))
def fibonaci(n):
    print("n:",n,"=","n-1=",(n-1),"n-2=",(n-2))
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonaci(n-1) + fibonaci(n-2)
print(fibonaci(int(input("enter a number"))))

