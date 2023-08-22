a=23
s=str(bin(a))[2:]
print(s)
count=[]
number=0
for x in range(len(s)):
    if s[x] == "1":
        number +=1
    else:
        count.append(number)
        number=0
count.append(number)
print(count)
print(max(count))