a=[4 ,6, 5, 3 ,3 ,1,2,3,33,3333]
# list1=[]
# list2=[]
# list3=0
# list4=0
# count=0
# s=True
# b=sorted(a)
# print(b)
# for i in range(len(b)):
#     if (i != (len(b) - 1)):
#         if (s):
        
#             if(abs(b[i] - b[i + 1]) == 1  or b[i] == b[i + 1]):
#                 list1.append(b[i])
#                 list3 +=1
#             else:
#                 list1.append(b[i])
#                 list3 +=1
#                 s=False
#         if (a[i] < a[i + 1]):
#             if(abs(b[i] - b[i + 1]) == 1  or b[i] == b[i + 1]):
#                 list2.append(b[i])
#                 list4 +=1
#     else:
#         if(abs(b[i] - b[i - 1]) == 1  or b[i] == b[i - 1]):
#             list2.append(b[i])
#             list4 +=1
# print(list1)
# print(list2)
# print(list3)
# print(list4)
print(a.count(3))        
s = set(a)
d = {e:a.count(e) for e in s }
max([d[k]+d.get(k+1,0) for k in d.keys() ])
          
    
    