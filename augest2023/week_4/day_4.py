s=[1,2,3,4,5,6,7,8,9]
for x in range(int(input())):
    t=input().split()
    if t[0]=="pop":
            if(len(s)):
                s.pop()
    elif t[0]=="remove" : 
            a=int(t[1])
            s.discard(a) 
    elif t[0]=="discard": 
            g=int(t[1])
            s.discard(g)
        
        
