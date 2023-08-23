# a=23
# s=str(bin(a))[2:]
# print(s)
# count=[]
# number=0
# for x in range(len(s)):
#     if s[x] == "1":
#         number +=1
#     else:
#         count.append(number)
#         number=0
# count.append(number)
# print(count)
# print(max(count))
# s=23
# n=bin(s)[2:]
# maxsquence=max(n.split("0"))
# print(len(maxsquence))
n = int(input().strip())
n_binary = bin(n)[2:]
max_sequence = max(n_binary.split('0'))
print(len(max_sequence))

