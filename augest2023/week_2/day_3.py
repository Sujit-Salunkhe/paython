# # counting=[]
# # for x in range(len(ar)):
# #     count=0
# #     for y in range((x +1),):
# #         if ar[x] == ar[y]:
# #             count+=1
# #             # ar.pop(ar[y])
# #         else:
# #             count -=1
# #             if count%2 == 0 :
# #                 if count !=0:
# #                     print(count)
# #                     counting.append(count)
# n=7
# ar=[1,2,1,2,1,3,2]
# a=0
# t=1
# count=0
# while (len(ar)):
#     # a +=1
#     while ar[a] == ar[t]:
#         count +=1
#         # ar.pop(ar[t])
#         print("ar[t]",ar[t],"t:",t)
#     t +=1
#     print(count)

# def sockMerchant(n, ar):
#     pairs = 0
#     for i in range(0, n):
#         matched = 0
#         for j in range(i+1, n):
#             if ar[i] == ar[j]:
#                 matched+=1
#         pairs += matched%2
#     return pairs

# print(sockMerchant(6,[1,2,3,1,1,3]))
# print(1%2)/


print( (7-4)>(7/2))
# print(len(counting))
# print((counting))