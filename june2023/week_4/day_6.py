k=1
bill=[3,10,2,9]
b=12
pay=0
for i in range(len(bill)):
    if i == k:  
        continue
    else:
        pay += bill[i]
print(pay)
ret=b - (pay//2)

if(b == pay):
            print("Bon Appetit")
else:
    print(ret)   
print(ret)