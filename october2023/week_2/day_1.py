n=8
k=3
c=[1,1,1,0,1,1,0,0,0,0]
energy=100




if c[0] == 0:
        energy = 99
else:
        energy = 97
    
n = len(c)
if k == n:
    print( energy )
i = 0 + k
    
while i != 0:
    if c[i] == 0:
        energy -= 1
    else:
        energy -= 3
    i = (i + k)% n
    print("i",i,"c[i]",c[i])

print(energy)