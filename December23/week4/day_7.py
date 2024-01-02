def bubble_sort(nums):
    nums = list(nums)
    for _ in range(1,len(nums) - 1):
        for i in range(len(nums) - 1):
            print(i)
            if nums[i] > nums[i+1]: 
                nums[i] ,nums[i+1] = nums[i + 1] , nums[i]
    return nums

list1=[1,23,45,2,64,33]

a = bubble_sort(list1)
print(a)

def insertion_sort(nums):
    nums = list(nums)
    for i in range(len(nums)):
        cur = nums.pop(i)  
        j = i -1
        while j >=0 and nums[j] > cur:
            j -=1
        nums.insert(j + 1,cur)
    return nums

a=list(range(7))
print(list(range(0,10)))
# print(a[3:])
# print(a[1])
# print(a[1:3])
