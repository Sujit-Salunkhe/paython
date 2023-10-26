a=[1,2,3]
k=2
queries=[0,1,2]
def circularArrayRotation(a, k, queries):
    # Write your code here
    for i in range(k):
        lastelement=a.pop()
        a.insert(0,lastelement)
    numbers = []
    for k in range(len(queries)):
        numbers.append(((a[queries[k]])))
    return numbers

a=circularArrayRotation(a,k,queries)
print(a)
# queries=[1,2]
# for i in range(k):
#     lastelement=a.pop()
#     newlist=a.insert(0,lastelement)
# for k in range(len(queries)):
#     print(a[queries[k]])

# for i in range(k):
#         lastelement=a.pop()
#         a.insert(0,lastelement)
# for k in range(len(queries)):
#      return str(((a[queries[k]])))