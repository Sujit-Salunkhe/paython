class Graph:
    def __init__(self,vertex,edges):
        self.data = [[] for _ in range(vertex)]
        for v1,v2 in edges:
            self.data[v1].append(v2)
            self.data[v2].append(v1)

    def __repr__(self):
        results =' '
        for i,nodes in enumerate(self.data):
             results += str(i) + ':' + str(nodes) + '\n'
        return results
    def __str__(self):
        return self.__repr__()

n=5
edges=[(0,1),(1,2),(1,3),(1,4),(2,3),(3,4),(4,0)]

graph1 = Graph(n,edges)
# print(graph1.data)
# print(graph1)
def bfc(graph,source):
    visited =[False] * len(graph)
    queue = [source]
    visited[source] = True 
    distance = [0]
    parent = [None]
    i = 0
    while i < len(queue):
        current = queue(i)
        visited[current] = True 
        for v in graph.data[current]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True  
                distance.append(distance[current]+1)
                parent.append(current) 
            i +=1
    return queue 

def dfs (graph,source):
    stack =[source]
    visited=[False] * len(graph.data)
    result = []
    while len(stack) > 0:
        current =stack.pop()
        if not visited[current]:
            result.append(current)
        visited[current] = True
        for v in graph.data[current]:
            if not visited[v]:
                stack.append(v)
    return result

    # Write a function  program to find a shorts path in graphe
    # write a function to find a cycle path of a graphe

sujit=[[2,3],[45,34,90],[873,23]]  

# a=sujit.pop()
# print(sujit[a])
# print(sujit)

class Graph2:
    def __init__(self,n,edges,directed = False) :
        self.data = [[] for _ in range(n)]
        self.weights = [[] for _ in range(n)]
        for e in edges:
            if len(e) == 3:
                v1,v2,w = e
                self.data[v1].append(v2)
                self.weights[v1].append(w)
                if not directed:
                    self.data[v2].append(v1)
                    self.data[v2].append(w) 
            else:
                v1,v2 = e
                self.data[v1].append(v2)
                if not directed:
                    self.data[v2].append(v1)

    def __repr__(self):
        results =' '
        for i,(nodes,weights) in enumerate(zip(self.data,self.weights)):
             results += str(i) + ':' + str(list(zip(nodes,weights))) + '\n'
        return results
    def __str__(self):
        return self.__repr__()
        
n = 6
edges=[(0,1,4),(0,2,2),(1,2,5),(1,4,10),(2,5,3),(4,3,4),(3,5,11)]

graphe2=Graph2(n,edges,directed=True)
  
print(graphe2)
print(graphe2.data)