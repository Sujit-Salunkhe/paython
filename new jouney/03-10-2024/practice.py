# def find_first_position(cards,query,mid):
#     mid_number = cards[mid]
#     if mid_number == query:
#         if mid -1 >=0 and cards[mid - 1] == query:
#             return 'left'
        
#         return 'found'
    
#     if mid_number > query:
#         return 'right'
    
#     else:
#         return 'left'

# def locate_cards(cards,query):
#     lo = 0
#     hi = len(cards)-1
#     while lo <= hi:
#         mid = (lo + hi)//2
#         mid_number = cards[mid]
#         first_position = find_first_position(cards,query,mid)

#         if  first_position == 'found':
#                 return mid
#         elif first_position == 'right':
#             lo = mid + 1
#         else:   
#             hi = mid - 1
#     return -1


# query_answer = locate_cards([10,9,8,7,4,3,2,1],4)
# test_case = [8,8,6,6,6,5,4,3,2,1]
# query=6

# result = locate_cards(test_case,query)
# print(result)
# print(query_answer)


        
test = [2,7,11,15]
target = 9
def twoSum (nums,target):
    arr = []
    for i in range(0,len(nums)): 
        for j in range(i+1,len(nums) - 1):
            print(i,nums[i],j+1,nums[j])
            if nums[i] + nums[j] == target:
                return [i,j]

def objMethod(nums,target):
    res = {}
    for i in range(len(nums)):
        if (target - nums[i]) in res:
            return [i,nums[target - nums[i]]]
        else:
            res[nums[i]] = i


print(twoSum(test,target))


class User:
    def __init__(se.f,username,name,email):
        self.username = username
        self.name = name
        self.email = email