# class Retangle:
#     type="retangle"
#     sides= 4
# 1234567890
# class Employee:
#     def __init__(self,fname,lname) -> None:
#         self.fname=fname
#         self.lname=lname
#         self.Email=f"{self.fname}.{self.lname} @employees.com"
#     def explain (self):
#         return  f"This emplyee name is {self.fname} {self.lname}"
# amar=Employee("amar","Jaiswal")
# sudhir=Employee("sudhir","khan")
# print(amar.explain())
# print(amar.Email)


from tkinter import CENTER
from turtle import left


def printstar(n):
   p=1
   while n//3 > p:
      a="*"* p
      print(a.center(n))
      p +=2

   j=n//2 
   c=n 
   d=n
   while j < c:
      t="*" * d
      print(t.center(n))
      d -=4
      c -=5
   for x in range(3):
      print(('*' * d ).center(n))
   m=0
   while m < d:
      right=(("*" * ((d//2)-4)).just((n//2)-5))
      left=(("*" * ((d//2)-4))).rjust((n//4)+4)
      print(right,left)
      d -=2
      m +=1

   
    

printstar(50)        
    


