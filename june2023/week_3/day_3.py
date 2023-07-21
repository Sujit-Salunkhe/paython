# sujit= [67,34,34,34,78];
# # i=1
# for i,j in enumerate(sujit):
#     print(i,j)
# sujit ={
#     "alpha":[47,54,45],
#     "bets":[90,45,45]
# }
# for i,j in sujit:
#     print(i)

# 3
# dic ={ "Krishna" : [7, 68, 69],
#             "Arjun": [70, 98, 63],
#             "Malika" :[52, 56, 60],
#  }
# s = "Malika"
# for i,j in dic.items():
#     if i == s:
#         # print(sum(j))

# j=0
# sum=0
# for i in dic[s]:
#     sum +=i
#     # print(sum)
#     j +=1
    # print(j)
# print("{:.2f}".format(sum/j))
# print()
# suji=45.66
# # print((suji))
# list=[89]
# list.append(1)
# list.insert(1,7)
# list.sort()
# print(list)

# sujit=input().split();
# print(sujit)
num = str(input())
result=[]
c=1
for i in range(0,len(num)+ 1):
    # print("i:",i)
    if i == len(num) - 1:
        result.append((c," ",int(num[i])))
        break;
    if num[i] == num[i + 1]:
        c += 1
    else:
        result.append((c," ",int(num[i])))
        c=1
output = ' '.join(f'({count}, {digit})' for count,digit in result)
print(output)
# spli=num.split()
# print(spli)
# for i in num:
    #  print(i)
    #  print(i + 1)
# num="sujit"
# print(len(num))
# # while 
# sujit=[45,45]
# print(len(sujit))
# for i in num:
    # c=1
    # if i == i + 1:
    #       c += 1
    # else:
        # print(c,j)
        # pass
        # 
    # print(i,j)
#     print(i)

