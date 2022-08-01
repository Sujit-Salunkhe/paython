# input=[1,2,3,4,5,6]
# output=0
# output=2
# input3=[10,11,15,4,5]
# input5=[2]

# def rotation_count(numbers):
#     position = 0
#     while position < len(numbers):
#         # print("position:",position)
#         if position > 0 and numbers[position] < numbers[position-1]:
#             return position 
#         position += 1
#     return 0
# input4=[10,11,16,17,18,4,5,6,7,8]
# input2=[8,9,1,2,3,4,5]
# input3=[10,1,2,3]
# input4=[1,2,3,4,5]
# # print(rotation_count(input2))
# def rotete_list(nums):
#     lo,hi=0,len(nums)-1
#     while lo < hi:
#         mid=(lo+hi)//2
#         middle_number=nums[mid]
#         print("lo:",lo,"hi:",hi,"mid:",mid,"middle:",middle_number)
#         if mid > 0 and  middle_number > nums[mid+1]:
#             return mid + 1
#         elif middle_number > nums[mid-  1]:
#             hi = mid -1
       

#     return 0

# print(rotation_count(input4))
# print(rotete_list(input2))
# # liner seaerch algorithem
# def liner_search(numbers):
#     position=0
#     while position < len(numbers):
#         if position > 0 and "given conditon":
#             return position
#         position =+ 1
#     return -1 
            
# from functools import reduce


# map,filter,reduce
# for x in range(len(numbers)):
#     numbers[x]=int(numbers[x])
# numbers[2]=numbers[1]+ 1
# print(numbers[2])
# # print(a)
# a=set(numbers)
# print(a)
# # a=set(map(int,numbers))
# numbers=["56","78","67"]
# numbers=list(map(int,numbers))
# print(numbers)
# numbers=[2,3,4,5,6,7,8,9,10]
# triples=list(map(lambda a:a*a*a,numbers))
# print(triples)
# def squre(a):
#     return a+a
# def triple(a):
#     return a*a*a
# func=[squre,triple]
# for i in range(5):
#     val=list(map(lambda x:x(i),func)) 
#     print(val)
# list1=[1,2,3,4,5,6,7,8,9,10]
# def gr_thau5(num):
#     return num> 5
# gr_than5=list(filter(gr_thau5,list1))
# print(gr_than5)
# num=0
# for x in list1:
#     # num=num + x
#     num += x
# print(num)
from functools import reduce


# list1=[1,2,3,4,5,6,7,8,9,10]
# nums=reduce(lambda x,y:x+y,list1)
# print(nums)





