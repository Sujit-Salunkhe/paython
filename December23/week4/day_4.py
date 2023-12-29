class Treenode:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
    
    def height(self):
        if self is None:
            return 0
        return 1 + max(Treenode.height(self.left),Treenode.height(self.right))

    def size(self):
        if self is None:
            return 0
        return 1 + Treenode.size(self.left) + Treenode.size(self.right)
    
    def traverse_in_order(self):
        if self is None:
            return []
        return  (Treenode.traverse_in_order(self.left) + [self.key] + Treenode.traverse_in_order(self.right))

    def display_Keys(self,space='\t',level = 0):
        if self is None:
            print(space*level + 'None')
            return
        
        if self.left is None and self.right  is None:
            print(space*level) + str(self.key)
            return 
        display_Keys(self.right,space,level + 1)
        print(space*level + str(self.key))
        display_Keys(self.left,space,level+1)

    def to_tuple(self):
        if self is None:
            return None
        if self.left  is None and self.right is None:
            return self.key
        return Treenode.to_tuple(self.left),self.key,Treenode.to_tuple(self.right)
    
    def __str__(self) :
        return 'BinaryTree<{}>'.format(self.to_tuple())
    def __repr__(self):
        return 'BinaryTree<{}>'.format(self.to_tuple())

    @staticmethod
    def parse_tuple(data):
        if isinstance(data,tuple) and len(data) == 3:
            node = Treenode(data[1])
            node.left = parse_tuple(data[0])
            node.right=parse_tuple(data[2])
        elif data is None:
            node = None
        else:
            node = Treenode(data)
        return node
        
# node0 =Treenode(2)
# node1 =Treenode(3)
# node2 =Treenode(1)
# node3 =Treenode(5)
# node4 =Treenode(7)
# node5 =Treenode(3)
# node6 =Treenode(6)
# node7 =Treenode(8)
# node8 =Treenode(4)

# right sides of nodes of route nodes
# node0.right= node1
# node1.right=node2
# print((1,2,3))
def makeatuple():
    return 1,2,3

print(makeatuple())

# # left sides of nodes of route nodes

# node0.left=node3
# node3.left =node4
# node3.right=node5
# node4.right=node7
# node4.left=node6
# node5.left=node8
# node0.right=node2

# print(node0.key)
# print(node1.key)
# print(node2.key)
# print(node0.left)
# # print(node0)

# print(Treenode)

tree_tuple =((1,3,None),2,((None,3,4),5,(6,7, 8)))

def parse_tuple(data):
    if isinstance(data,tuple) and len(data) == 3:
        node = Treenode(data[1])
        node.left = parse_tuple(data[0])
        node.right=parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = Treenode(data)
    return node


tree2 = parse_tuple(tree_tuple)
def display_Keys(node,space='/t',level=0):
    if node is None:
        print(space * level + 'none')
        return 
    if node.left is None and node.right is None:
        print(space * level + str(node.key))
        return 
    display_Keys(node.right,space,level+1)
    print(space*level + str(node.key))
    display_Keys(node.left,space,level+1)

# display_Keys(tree2,"  ")

def traverse_in_order(node):
    if node is None:
        return []
    return (traverse_in_order (node.left) + [node.key] + traverse_in_order(node.right))

def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left),tree_height(node.right))

def remove_none(nums):
    return [x for x in nums if x is not None]

def is_bst(node):
    if node is None:
        return True,None,None
    is_bst_l,min_l,max_l = is_bst(node.left)
    is_bst_r,min_r,max_r = is_bst(node.right)

    is_bst_node = (is_bst_l and is_bst_r  and
                   (max_l is None  or node.key > max_l) and (min_r is None  or node.key<min_r))
    min_key  = min(remove_none([min_l,node.key,min_r]))
    max_key  = max(remove_none([max_l,node.key,max_r]))

    return is_bst_node,min_key,max_key