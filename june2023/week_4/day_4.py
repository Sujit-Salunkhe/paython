a=[1,3,2,6,1,2]
k=3
count=0
for i in range(len(a)-1):
    for j in range(i +1,len(a)):
        if (a[i] + a[j] )%k == 0:
            print("i:",i,"j:",j)
            count +=1 
print(count)