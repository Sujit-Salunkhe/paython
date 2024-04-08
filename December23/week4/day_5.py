# class User:
#     def __init__(self,username,name,email,):
#         self.username = username
#         self.name = name
#         self.email = email

# class UserDatabase:
#     def __init__(self):
#         self.users = []

#     def insert(self,user):
#         i = 0
#         while i < len(self.users):
#             if user.username < self.users[i].username:
#                 break
#             i +=1
#         self.users.insert(i,user)

#     def find(self,username):
#         for user in  self.users:
#             if user.username == username:
#                 return [user.username,user.name,user.email]
            
#     def upgrade(self,user):
#         target = self.find(user.username)
#         target.name,target.email ,user.email
    
#     def remove(self,username):
#         self.users.remove(self.find(username))
    
#     def list_all (self):
#         return [user.username for user in self.users]
    

# database = UserDatabase()
# user1 = User('sujit', 'Sujit Kumar', 'sujit@example.com')
# user2 = User('akash', 'Akash Singh', 'akash@example.com')
# user3 = User('hemant', 'Hemant Sharma', 'hemant@example.com')

# database.insert(user1)
# database.insert(user2)
# database.insert(user3)
# database.upgrade(User('sujit','Vaishnav','sujit@example.com'))

# print(database.list_all())
# print(database.find('hemant'))
tree_tuple =((1,3,None),2,((None,3,4),5,(6,7, 8)))
def parse_tuple(data):
        if isinstance(data,tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = parse_tuple(data[0])
            node.right= parse_tuple(data[2])
        
        elif data is None:
            node = None
        else:
            node = TreeNode(data)

        return node


tree = parse_tuple(tree_tuple)
# print(tree.left.key)

# print(tree.key)




# display_Keys(tree,space=' ')

# inorder traversal
        # left middle right
# preorder traversal
        # middle left right
# postorder traversal
      # left right middle

def traverse_in_order(node):
    if node is None:
         return []
    return (traverse_in_order(node.left) + [node.key] + traverse_in_order(node.right))

def traverse_pre_order(node):
    if node is None:
         return []
    return ([node.key] + traverse_in_order(node.left) + traverse_in_order(node.right))

def traverse_post_order(node):
    if node is None:    
         return []
    return ( traverse_in_order(node.left) + traverse_in_order(node.right) + [node.key])

# list1 = []
list1 = traverse_in_order(tree)
# # print(list1)
# print(max(tree))
def tree_height(node):
     if node is None:
          return 0 
     return 1 + max(tree_height(node.left),tree_height(node.right))


def tree_size(node):
     if node is None:
          return 0
     return 1 + tree_size(node.left) + tree_size(node.right) 



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
            node.left = parse_tuple(data[0])
            node.right= parse_tuple(data[2])
        
        elif data is None:
            node = None
        else:
            node = TreeNode(data)

        return node




def goes_from_tree(node):
    if node is None:
          return []
     
    return (goes_from_tree(node.left) + [node.key] + goes_from_tree(node.right))

