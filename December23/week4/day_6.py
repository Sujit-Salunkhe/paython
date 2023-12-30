class TreeNode:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

    def height(self):
        if self is None:
            return 0 
        return 1 + max(TreeNode.height(self.left) + TreeNode.height(self.right))
    
    def traverse_in_order(self):
        if self is None:
             return []
        return (TreeNode.traverse_in_order(self.left) + [self.key] + TreeNode.traverse_in_order(self.right))

    def traverse_pre_order(self):
        if self is None:
             return []
        return ([self.key] + TreeNode.traverse_pre_order(self.left) + TreeNode.traverse_pre_order(self.right))

    def traverse_post_order(self):
        if self is None:    
             return []
        return ( TreeNode.traverse_post_order(self.left) + TreeNode.traverse_post_order(self.right) + [self.key])

    def display_Keys(self,space='\t',level = 0):
        if self is None:
            print(space*level + 'None')
            return
        
        if self.left is None and self.right  is None:
            print(space*level + str(self.key))
            return 
        TreeNode.display_Keys(self.right,space,level + 1)
        print(space*level + str(self.key))
        TreeNode.display_Keys(self.left,space,level+1)

    def __str__(self) :
            return 'BinaryTree<{}>'.format(self.to_tuple())
    def __repr__(self):
            return 'BinaryTree<{}>'.format(self.to_tuple())

    def to_tuple(self):
        if self is None:
            return None
        if self.right is None and self.left is None:
            return self.key
            
        return  TreeNode.to_tuple(self.left),self.key,TreeNode.to_tuple(self.right)
    
    def remove_items(nums):
         return [x for x in nums if x is not None ]
    
    @staticmethod
    def parse_tuple(data):
        if isinstance(data,tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right= TreeNode.parse_tuple(data[2])
        
        elif data is None:
            node = None
        else:
            node = TreeNode(data)

        return node


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




tree1 = TreeNode.parse_tuple(((1,3,None),2,((None,3,4),5,(6,7, 8))))
name=(('aakash','biraj','hemanth'),'jadhesh',('siddhant','sonaksh','vishal'))
value= TreeNode.parse_tuple(name)

# print(is_bst(value))
# print(is_bst(tree1))
def is_binary_tree(node):
    if node is None:
        return True,None,None
    
    is_bst_l,min_l,max_l = is_binary_tree(node.left)
    is_bst_r,min_r,max_r = is_binary_tree(node.right)

    is_bst =  is_bst_l and is_bst_r and (max_l is None or node.key > max_l) and (min_r is None or node.key < min_r )

    max_key = max(remove_none([max_l,node.key,max_r]))
    min_key = min(remove_none([min_l,node.key,min_r]))

    return is_bst,min_key,max_key

# print(is_binary_tree(value))

class BSTNode():
    def __init__(self,key,value=None) :
        self.key = key
        self.value = value
        self.left =None
        self.right=None
        self.parent=None


tree4=BSTNode('jadhesh.username','jadhesh')
tree4.left=BSTNode('biraj.username','biraj')
tree4.right=BSTNode('sonaksh.username','sonaksh')
tree4.left.left=BSTNode('aakash.username','aakshe')
tree4.left.right=BSTNode('hemanth.username','hemanth')
tree4.right.left=BSTNode('siddhant.username','siddhant')
tree4.right.right=BSTNode('vishal.username','vishal')
tree4.left.parent = tree4
tree4.right.parent = tree4


print(tree4.right.key,tree4.right.value)

def display_Keys(node,space='\t',level = 0):
        if node is None:
            print(space*level + 'None')
            return
        
        if node.left is None and node.right  is None:
            print(space*level + str(node.key))
            return 
        TreeNode.display_Keys(node.right,space,level + 1)
        print(space*level + str(node.key))
        TreeNode.display_Keys(node.left,space,level+1)

# display_Keys(tree4)
display_Keys(tree4)

def insert(node,key,value):
    if node is None:
          node = BSTNode(key,value)
    elif node.key < key:
        node.right = insert(node.right,key,value)
        node.right.parent = node
    elif node.key > key:
        node.left = insert(node.left,key,value)
        node.left.parent = node
    return node