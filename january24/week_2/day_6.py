
# edges = [[1,2,24],[1,4,20],[3,1,3],[4,3,12]]
# n=4
# # n=5
# # edges=[(0,1,4),(1,2,6),(1,3,23),(1,4,78),(2,3,98),(3,4,34),(4,0,15)]
# def shortesPath(n,edges,s):
#     data = [[] for  _ in range(n)]
#     weights= [[] for _ in range(n)]

#     for e in edges:
#         v1,v2,w = e
#         data[v1-1].append(v2)
#         weights[v1-1].append(w)
#         data[v2-1].append(v1)
#         weights[v2-1].append(w)

#     for i,(edge,weight) in enumerate(zip(data,weights)):
#         print(i+1,':',list(zip(edge,weight)))
#     visited=[False] * len(data)
#     queue= [s]
#     # distance=[]
#     i = 0
#     while i < len(queue):
#         current = queue[i]
#         print(visited) 
#         visited[current-1] = True
#         print(visited)
#         for v in data[current-1]:
#             if not visited[v]:
#                 queue.append(v)
#                 visited[v] = True
#         i +=1
#     return queue



    


# print(shortesPath(n,edges,1))

# first take a add first row and memeroze the number

# s=[34,34,4322,3343]
s=[[5, 3, 4], [1, 5, 8], [6, 4, 2]]
# s=[23,343,4323]
# print(sum(s))
k=0
l=0
horizontalsum = [0,0,0]
verticalsum   = [0,0,0]
dignalsum1 = 0
# dignalsum1 = 
for i in range(len(s)):
    for j in range(len(s[i])):
        horizontalsum[i] +=s[i][j]
for i in range(len(s)):
    for j in range(len(s[i])):
        verticalsum[i] +=s[j][i]
while k < len(s):
    print(k)
    dignalsum1 += s[k][l]
    k +=1
    l+=1
o=0
p=2
dignalsum2 = 0
while o < len(s):
    dignalsum2 += s[o][p]
    o +=1
    p -=1


print('horizontal',horizontalsum,'vertical',verticalsum,'dignnal',dignalsum1,'dignal2',dignalsum2)



    
    

