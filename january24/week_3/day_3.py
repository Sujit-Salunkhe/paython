a = [1,2,3,4,5]
b = 'Sample String'
k ={
    'name':'sujit',
    "lname":'salunkhe'
}
print(str(a))
print(repr(a))
print(str(b))
print(repr(b))
print(str(k))
print(repr(k))
s = [19,10,12,10,24,25,22]
list2 =[]
k= 4
for i in range(len(s)):
    for t in range(len(s)):
        print((s[i] + s[t]) % k )
        if (s[i] + s[t]) % k != 0:
                
                list2.append(s[i])
                list2.append(s[t])
        else:
             list2.remove(s[t])


