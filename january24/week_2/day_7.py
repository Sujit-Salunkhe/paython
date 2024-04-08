def magic_min_cost(s):
    possibleMagicSqures=[
        [[8,1,6],[3,5,7],[4,9,2]],
        [[6,1,8],[7,5,3],[2,9,4]],
        [[4,9,2],[3,5,7],[8,1,6]],
        [[2,9,4],[7,5,3],[6,1,8]],
        [[8,3,4],[1,5,9],[6,7,2]],
        [[4,3,8],[9,5,1],[2,7,6]],
        [[6,7,2],[1,5,9],[8,3,4]],
        [[2,7,6],[9,5,1],[4,3,8]]
    ]
    min_cost = float('inf')
    for p in possibleMagicSqures:
        cur_cost = 0
        for i in range(len(p)):
            for j in range(len(p[i])):
                cur_cost += abs(s[i][j] - p[i][j])
        if cur_cost < min_cost:
            min_cost = cur_cost
    return min_cost

# s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
# k = magic_min_cost(s)
# print(k)

# numbers = [1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
numbers = [1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,7]
s='zaba'
# # s='abc'
# values = []
# for i in range(len(s)):
#     values.append(numbers[i])

# a = max(values)
# # print(a)
# print(a * len(s))
# import string   
# lowercase_letters = string.ascii_lowercase
# print(lowercase_letters)
# Find the index of each letter
# for letter in lowercase_letters:
#     index = ord(letter) - ord('a')
#     print(f"Index of '{letter}': {index}")
# def find_an_value(s,number):
#     lower_value = 0
#     for letters in s:
#         index = ord(letters) - ord('a')
#         k = number[index]
#         print(k)
#         if lower_value < k:
#             lower_value = k
#     print(k)
#     return k * len(s)
    
# j=find_an_value(s,numbers)
# print(j)


def count_people(n,people=5):
    if n == 0:
        return 0
    people = people//2
    shared = people * 3
    return people + count_people(n-1,shared)

print(count_people(3))


def count_people2(n):
    count = 0
    people = 5
    for _ in range(n):
        peoplecount = people //2
        shared = peoplecount * 3
        people = shared
        count +=peoplecount
    return count

print(count_people2(3))


    

    