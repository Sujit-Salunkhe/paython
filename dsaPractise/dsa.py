# cards= [23,3,2,3,4,12,65,43]
# query = 12

# def liner_Search (cards,query):
#     for i in range(len(cards)):
#         if cards[i] == query:
#             return i
#     return -1
        
# sortarr = sorted(cards)
# # print(sortarr)

# def test_location(cards,query,mid):
#     mid_number = cards[mid]
#     if mid_number == query:
#         if mid-1 >= 0 and cards[mid-1] ==query:
#             return 'right'
#         else:
#             return 'found'
#     elif mid_number < query:
#         return 'left'
#     else:
#         return 'right'
# def binary_search (cards,query):
#     lo,hi = 0,len(cards) -1
#     while lo <=hi:
#         mid = lo + hi // 2
#         loc = test_location(cards,query,mid)

#         if loc == 'found':
#             return mid
#         elif loc == 'right':
#             lo = mid+1
#         else:
#             hi = mid -1   
#     return -1
        

# # print(binary_search(sortarr,3))
# tree_tupel =((1,3,None),2,((None,3,4),5,(6,7,8)))

# class TreeNode:
#     def __init__(self,key) :
#         self.key = key
#         self.right =None
#         self.left = None
# def tuple_Parse (data):
#     if data is None:
#          node = None
#     elif isinstance(data,tuple) and len(data) == 3:
#         node = TreeNode(data[1])
#         node.left = tuple_Parse(data[0])
#         node.right = tuple_Parse(data[2])
#     else:
#         node = TreeNode(data)
    
#     return node

# tree = tuple_Parse(tree_tupel)


# def traverse_in_order(node):
#     if node is None:
#         return []
#     return (traverse_in_order(node.left) + [node.key] + traverse_in_order(node.right))


# print(traverse_in_order(tree))

# def tree_height (node):
#     if node is None:
#         return 0
#     return 1 +(max(tree_height(node.left),tree_height(node.right)))
# def remove_none(nums):
#     return [x for x in nums if x is not None]
# def is_bst (node):
#     if node is None:
#         return True,None,None
#     is_bst_l,min_l,max_l = is_bst(node.left)
#     is_bst_r,min_r,max_r = is_bst(node.right)

#     is_bst_node = (is_bst_r and is_bst_l and (min_l is None or max_l < node.key)
#  and (max_r is None or min_r > node.key ))
     
#     min_key = min(remove_none([min_l,[node.key],min_r])) 
#     max_key = max(remove_none([max_l,[node.key],max_r]))
#     return is_bst_node,min_key,max_key

# class BstNode():
#     def __init__(self,key,value=None):
#         self.key =key
#         self.value = value
#         self.left = None
#         self.right = None
#         self.parent = None

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0,n-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
        

a= bubble_sort([34,54,56,23,43,32,90,23 ])
print(a,'bubule')

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_node = i
        for j in range(i+1,n):
            if arr[j] < arr[min_node]:
                min_node = j
        arr[min_node],arr[i] = arr[i],arr[min_node]
    return arr

b = selection_sort([34,54,56,23,43,32,90,23 ])
print(b,'selection')


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = merge_sort(arr[:mid])
        R= merge_sort(arr[mid:])
        i,j,k = 0
        while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k]  = L[i]
                    i +=1
                else:
                    arr[k] = R[j]
                    j +=1
                k +=1
        while i < len(L):
            arr[k] = L[i]
            i +=1
            k +=1
        while j <len(R):
            arr[k] = R[j]
            j+=1
            k+=1
    return arr
def quick_Sort(arr):
    if len(arr) <=1:
        return arr
    pivot = arr[len(arr) //2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_Sort(left) + middle + quick_Sort(right)

