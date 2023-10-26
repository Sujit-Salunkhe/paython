n=12
t=str(n)
divider=0
for x in range(len(t)):
    if  t[x] == "0":
        continue
    elif n % int(t[x]) == 0:
        divider +=1
print(divider)


