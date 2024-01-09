class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def insertAtBeginning(self,data):
        new_node = Node(data)
        new_node.next = self.data
        self.data = new_node

    def insertAtIndex(self,data,index):
        new_node = Node(data)
        position = 0
        current_node = self.data
        if position == index:
            self.insertAtBeginning(data)
        else:
            while current_node != None and position +1 !=index:
                position +=1
                current_node = current_node.next
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print('index does not exist')

    def insertAtend(self,data):
        new_node=Node(data)
        if self.data is None:
            self.data = new_node
        else :
            currentNode = self
            while(currentNode.next):
                currentNode = currentNode.next
            currentNode.next = new_node


    def update_node(self,val,index):
        position = 0
        currentNode = self
        if position == index:
            currentNode = val
        else:
            while position  != index and currentNode != None:
                position+=1
                currentNode = currentNode.next
            if currentNode != None:
                currentNode.data = val
            else:
                print('index not present')

    def remove_first(self):
        if self.next is not None:
            self.data = self.next.data
            self.next =self.next.next
        
        else:
            self.data = None

    def remove_last(self):
        if self.data is None:
            return 
        elif self.next is None:
            self.data = None
        else :
            current = self.data
            while (current.next.next):
                current = current.next
            current.next = None

    def remove_index(self,index):
        if self.data is None:
            return 
        current_node = self
        position = 0 
        if position == index:
            self.remove_first()
        else:
            while position + 1 != index and current_node.next != None:
                position  +=1
                current_node = current_node.next
            if current_node != None:
                current_node.next = current_node.next.next 
            else:
                print('index is not Found')
    def delete_by_given_data(self,val):
        if self.data is None:
            return 
        current = self
        if val == current:
            self.remove_first()
        while  current.next is not None and current.next.data != val:
            current = current.next

        if current is None:
            return

        else:
            current.next = current.next.next
        
    def __repr__(self):
        result =""
        current = self
        while current is not None:
            result += str(current.data) + " "
            current = current.next
        return result
    def __str__(self) -> str:
        return self.__repr__()

# a=Node(4)
# a.remove_first()
# a.insertAtend(100)
# a.update_node(88, 1)
# a.remove_last()
# a.remove_index(0)
# a.delete_by_given_data(88)
# a.insertAtBeginning(45)
# a.insertAtend(100)
# a.insertAtIndex(99, 0)
            
link1= Node(4)
link1.insertAtend(34)

print(link1)


# class Node2: 
#     def __init__(self, data) :
#         self.data = data
#         self.next = None

#     def insertAtBeginning(self, data):
#         new_node = Node2(data)
#         new_node.next = self.next
#         self.next = new_node

# a = Node2(4)
# a.insertAtBeginning(3)

# print(a.data)  # Accessing the value of head
