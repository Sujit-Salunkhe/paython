# list=[[2,3,[9]],5,["sujit"]];
# # print(list[0][2][0])
# # print(list[2][0])
# def pattern(j):
#     i=1
#     while i < j:
#         pass
k=1
for i in range(1,6): 
    print(("H" * k).center(10," "))
    k +=2
for i in range(1,7):
    print(("H" * 5).rjust(5," "),("H" * 5).ljust(15," ")) 
for i in range(1,4):
    print(("H" * 17).rjust(19," "))


n,x=map(int,input().split(" "))
z=[]
for i in range(x):
    z.append(list(map(float,input().split(" "))))

for k in zip(*z):
    print(sum(k)/x)

a=[[78,45,46],[24,34,43]]
for i,n in zip(*a):
    print(i,n)