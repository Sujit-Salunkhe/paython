# a="sujit"
# s=""
# t=""
# for i in range((len(a))):
#     if(i%2 == 0):
#         s +=a[i]
# for l in range((len(a))):
#     if(l%2 != 0):
#         t +=a[l]

# print(s)
# print(t)
# times=int(input())
# times = int(input())
# for x in range(times):
#     t=""
#     s=""
#     n=input()
#     for i in range((len(n))):
#         if(i%2 == 0):
#             s +=n[i]
#     for l in range((len(n))):
#         if(l%2 != 0):
#             t +=n[l]

#     print(s,t)
# for x in range(times):
#     s=input()
#     print(s[::2],s[1::2])
def sorting (l):
    for i in range(len(l)):
        smallvalue=i
        for x in range(i,len(l)):
            if l[smallvalue] > l[x]:
                smallvalue = x
        (l[smallvalue],l[i]) = (l[i],[l[smallvalue]]) 
    p = [x for list in l for x in list]
    return (p)

a=[2,4,89,67,1]
print(sorting(a))