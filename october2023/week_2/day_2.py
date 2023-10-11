n=25
longnumber=n
run=1
for x in range(n):
    run +=1
    longnumber += longnumber * (n - 1)
    print(longnumber)
    n -= 1
    print(n)
print(longnumber)
# print(run)