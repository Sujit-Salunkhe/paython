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
t =[]
k= 4
for i in range(len(s)):
    for k in range(len(s)):
        if (s[i] + s[k]) % k != 0:
                t.append(s[i])
                t.append(s[k])
        else:
             t.pop(s[k])


