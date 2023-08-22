# def factorial(n):
#     if n <=1:
#         return 1
#     else:
#          return n*factorial((n - 1))
# print(factorial(3))

def insertion_sort(n):
    for s in range(len(n)):
        pos=s
        while pos > 0 and n[pos] < n[pos-1]:
            (n[pos],n[pos-1]) = (n[pos-1],n[pos])
            pos -=1
    return n
t=[34,2,45,78,98,4]
s=insertion_sort(t)
print(s)