num_nodes = 5
edges = [(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)]
# num_nodes ,len(edges)

class Graph:
    def __init__(self,num_nodes,edges) :
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]
        self.edges = edges
        for n1,n2 in edges:
            self.data[n1].append(n2)  
            self.data[n2].append(n1)  

    def __repr__(self):
        return "\n".join(["{}:{}".format(n,neigbours) for n,neigbours in enumerate(self.data)])
        
    def __str__(self) -> str:
        return str(self.__repr__())
    
    def addNode(self,edges):
        self.num_nodes +=1
        self.data.append([])
        for n1,n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
    def deleteNode(self,deleteNode):
        self.num_nodes -= 1
        del self.data[deleteNode]

garph1 = Graph(num_nodes,edges)



# print(garph1)

garph1.addNode([(5,1),(5, 4)])
print(garph1)
garph1.deleteNode(1)
print(garph1)

