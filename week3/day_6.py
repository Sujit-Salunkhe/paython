# from gettext import find
# from http.client import FOUND
# from turtle import left, right
# from unittest import result
# # print("hello,world")
# # print(9<10)
# def find_card(cards,query):
#     position=0
#     while position<len(cards) :
#         if cards[position]==query:
#             return position
#         position += 1
#     return -1 
# # a =[13,10,8,5,4,1,]
# c=[]

# # d=13
# def find_card(cards,query,mid):
#     middle_number=cards[mid]
#     # print("mid:",mid,"middle_number:",middle_number)
#     if middle_number==query:
#         if mid -1 >=0 and cards[mid -1]==query:
#             return "left"
#         else:
#             return "found"
#     elif middle_number > query:
#         return "right"
#     else:
#         return "left"
# # binery search``
# def locate_card(cards,query):
#     lo,hi=0,len(cards)-1
#     while lo<=hi:
#         # print("lo:",lo,"hi:",hi)
#         mid = (lo+hi) // 2
#         result=find_card(cards,query,mid)
#         if result == "found":
#             return mid
#         elif result == "right":
#             lo=mid +1
#         elif result=="left":
#             hi=mid -1
#     return -1
# # b=10
# a=[12,10,9,9,9,9,9,9,8,7,6]
# b=9
# print(locate_card(a,b))
# def binery_search(lo,hi,condition):
#     while lo<=hi:
#         mid=(lo+hi)//2
#         result=condition(mid)
#         if result =="found":
#             return mid
#         if result=="left":
#             hi=mid-1    
#         if result=="right":
#             lo=mid+1
#     return -1

a=[1,2,3,3,5]
z=max(a)
while max(a)==z:
    a.remove(max(a))
print(max(a))
li


    


# print(c)
# b=min(a)



        
  