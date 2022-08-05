# mytuple = ("apple", "banana", "cherry")
# myit=iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))


# nxt="sujit"
# sujit=iter(nxt)
# print(next(sujit))
# print(mytuple)
# from tkinter import N


from locale import DAY_1


mytuple = ("apple", "banana", "cherry")
    # for x in mytuple:
    #     print(x)
    # mystr = "banana"
    # for x in mystr:
    #     print(x)

    # def numbers(n):
    #     while n<= 100:
    #         n += 1
    #         print (n)
    #         if n==100:
    #             break
#     #     return n

# # numbers(5)
# class numbers:
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         if self.a<=20:
#             x =self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration
# sujit=numbers()
# sujit_s= iter(sujit)
# for x in sujit_s:
#     print(x)

# # print(next(sujit_s))
# # print(next(sujit_s))
# # print(next(sujit_s))
# # print(next(sujit_s))
# # print(next(sujit_s))
# # print(next(sujit_s))
# # print(next(sujit_s))
# # print(next(sujit_s))
# # print(next(sujit_s))
       
     

# # # print(numbers(5))
# # class MyNumbers:
# #   def __iter__(self):
# #     self.a = 1
# #     return self

# #   def __next__(self):
# #     x = self.a
# #     self.a += 1
# #     return x

# # myclass = MyNumbers()
# # myiter = iter(myclass)

# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# class numbers:
#     def __iter__(self):
#           self.a=1
#           return self
#     # def __iter__(self):
#         # pass
#     def __next__(self):
#         if self.a<=20:
#             x =self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration
# sujit=numbers()
# sujit2=iter(sujit)
# for x in sujit2:
#     print(x)
f=open(DAY_1)
content=f.read()
print(content)