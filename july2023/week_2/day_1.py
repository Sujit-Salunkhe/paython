# x=min(23,24)
# print(x)
def cmd(m,n):
    for i in range(1,min(m,n)+1):
        if (m%i)==0 and (n%i) == 0:
            mrcf = i
    return mrcf
print(cmd(100,1000))
def cmd_2(m,n):
    i = min(m,n)
    while i > 0:
        if (m%i)==0 and (n%i) == 0:
            return i
        else:
            i -= 1
            