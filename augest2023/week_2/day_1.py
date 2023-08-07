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
times = int(input())
for x in range(times):
    t=""
    s=""
    n=input()
    for i in range((len(n))):
        if(i%2 == 0):
            s +=n[i]
    for l in range((len(n))):
        if(l%2 != 0):
            t +=n[l]

    print(s,t)


    