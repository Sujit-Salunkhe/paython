sujit=[57,3478,34,43]
va=[73,4.,54,54,5,543,43,57]
j=[90,78,65]
for i in sujit:
    if i in va:
        j.append(i)

# print(j[-1])

def gmd(m,n):
    fm=[]
    for i in range(1,m+1):
        if(m % i) == 0:
            fm.append(i)
    
    fn=[]
    for j in range(1,n+1):
        if(n % j) == 0:
            fn.append(j)
    
    gn=[]
    for i in fm:
        if i in fn:
            gn.append(i)
    
    return gn[-1]


print(gmd(100,1000))

