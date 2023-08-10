# n=5
# p=3
# turn=0
# page=1
# while (n - p) >=  (n/2):
#     if page >= p:
#         print (turn)
#         break
#     turn +=1
#     page +=2
 
# if (n == p) or (n-1) == p:
#     print(turn)
# page=n -1
# while(True):
#     if page <= p:
#         print(turn)
#         break
#     turn +=1
#     page -=2

# def pageCount(n, p):
#     # Write your code here
#     turn=0
#     page=1
#     if (n == p) or (n-1) == p:
#         return (turn)
#     while (n - p) >=  (n/2):
#         turn=p//2
#         return turn
#     page=n -1
#     while((n - p) <  (n/2)):
#         if page <= p:
#             return (turn)
#         turn +=1
#         page -=2



# print(pageCount(6,5))
def pageCount(n, p):
    # Write your code here
    turn=0
    page=1
    if (n == p):
        return (turn)
    if (n - p) >=  (n/2):
        turn=p//2
        return turn
    if(n%2 ==0):
        page=n
    else:
        page=n -1
    while((n - p) <  (n/2)):
        if page <= p:
            return (turn)
        turn +=1
        page -=2

# print(3//2)