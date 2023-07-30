# class A:
#     def __init__(self,name,fname) -> None:
#         self.name=name
#         self.fname=fname

#     def method(self):
#         print("This is methed of class A")
#     def sanket(self):
#         print(f"Mai ek chutiya hu mera namm hai  {self.name} {self.fname}")
    
# class B(A):
#     def method(self):
#         print ("This is methed of class B")
    
# # class C(A):
# #     def method(self):
# #         print ("This is a method of class C ")
# # class D(B,A):
# #     pass
# # a=A()
# # b=B()
# # c=C()
# # d=D()

# # d.method()
# # a=A("sanket","Mhaske")
# # (a.sanket())
#     # Rainforest
# class employee:

#     def __init__(self,name,work,time) -> None:
#         self.name=name
#         self.work=work
#         self.time=time
#     def printdetails(self):
#         return (f"My name is {self.name} And My work is {self.work} And My working hours is {self.time} ")
#     @classmethod
#     def fromdash(cls,str):
#         a=str.split("-")
#         return cls(a[0],a[1],a[2])
#     @staticmethod
#     def printgood(string):
#         return("he is a good employee "+ string)
#     def __add__(self,other):
#         return self.time + other.time
#     def __repr__(self) -> str:
#         return f"{self.name}, {self.work},{self.time}"
#     def __str__(self) -> str: 
#         return f"I am  in a str method  {self.name}"
# sujit=employee("sujit","Devleper",38)
# Sanket=employee("sanket","peun",78)
# prasad=employee("prasad","manager",10252)
# # # print(sujit.printdetails())
# # print(sujit+ Sanket)
# # print(sujit+prasad)
# print(repr(sujit))
# print(repr(Sanket))
# print(repr(prasad))
# print("sujit is dangerous boy , he is very intelligent and smart boy")
        # 

m=2
d=36
n=30
while m < d:
        print(m,d)
        right=(("*" * ((d//2)-m)).rjust((n//2)+2))
        left=(("*" * ((d//2)-m)))
        print(right,left)
        d -=2
        m +=4

        