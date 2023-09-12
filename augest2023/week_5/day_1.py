n=5
k=2
clas=[0,-1,2,1]
yes=0
no=0
for x in range(len(clas)):
    if clas[x] <= 0:
        yes +=1
    else:
        no+=1
if yes >= k:
    print("NO")
else:
    print("Yes")