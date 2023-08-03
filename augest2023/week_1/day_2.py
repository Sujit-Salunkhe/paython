N=9
if N % 2 == 0 and (2<=N<=5 or N>20):
    print("Not Weird")
else:
    print("Weird")  
def serach(seq,n):
    for x in seq:
        if x == n:
            return( "true" )
    return ("false")

