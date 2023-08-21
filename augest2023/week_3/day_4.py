import sys
sys.setrecursionlimit(10000)
def quicksort(list,start,end):
    if end - start <=1:
        return ()
    yellow = start + 1
    for green in range(start + 1,end):
        if list[green] <= list[start]:
            (list[green],list[yellow]) = (list[yellow],list[green])
            yellow += 1
    ( list[start],list[yellow -1] ) = ( list[yellow -1],list[start] ) 
    quicksort(list,start,yellow -1 )
    quicksort(list,yellow,end)  
a=list(range(100,3,-1))
print(a[100:3])
print(a)
quicksort(a,0,len(a))
print(a)

# print(list(range(5,1000)))

# a=[100, 100, 50, 40, 40, 20 ,10]
# b=[5,25, 50, 120]

# i = 0
# while i < len(a) - 1:  # Loop until the second-to-last element
#     if a[i] == a[i + 1]:
#         a.pop(i)  # Remove the element at index i
#     else:
#         i += 1
# for i  in range(len(b)):
#     for k in range(len(a)):
#         if b[i] >= a[k]:
#             print(k +1)
#             break
#     if b[i] < a[-1]:
#         print(len(a) + 1)

# def climbingLeaderboard(a, b):
#     c=[]
#     # Write your code here
#     i = 0
#     while i < len(a) - 1:  # Loop until the second-to-last element
#         if a[i] == a[i + 1]:
#             a.pop(i)  # Remove the element at index i
#         else:
#             i += 1
#     for i  in range(len(b)):
#         for k in range(len(a)):
#             if b[i] >= a[k]:
#                 c.append((k +1))
#                 break
#         if b[i] < a[-1]:
#             c.append((len(a) + 1))
#     return (c)
# a=[100, 100, 50, 40, 40, 20 ,10]
# b=[5,25, 50, 120]

# # print(climbingLeaderboard(a,b))
# def climbingLeaderboard(ranked, player):
#     for i in range(len(player)):
#             ranked.append(player[i])
#             List = set(ranked)
#             Sorted_list = sorted(List)
#             Sorted_list.reverse()
#             rank = Sorted_list.index(player[i])
#             print(rank + 1)
# a=[100, 100, 50, 40, 40, 20 ,10]
# b=[5,25, 50, 120]
# def climbingLeaderboard(ranked, player):
#     result=[]
#     for i in player:
#         while ranked and i >= ranked[-1]:
#             ranked.pop()  
#         result.append(len(ranked) + 1) 
#     for i in result:
#         print(i)
# climbingLeaderboard(a,b)
# def climbingLeaderboard(ranked, player):
#     unique_ranked = [ranked[0]]  # Initialize with the first score
#     for score in ranked[1:]:
#         if score != unique_ranked[-1]:
#             unique_ranked.append(score)  # Add only if it's a new score

#     player_ranks = []

#     for player_score in player:
#         # Perform binary search to find the appropriate rank
#         left, right = 0, len(unique_ranked) - 1
#         while left <= right:
#             mid = (left + right) // 2
#             if unique_ranked[mid] == player_score:
#                 player_ranks.append(mid + 1)  # Found exact score
#                 break
#             elif unique_ranked[mid] < player_score:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         else:
#             player_ranks.append(left + 1)  # Insert the player's score

#     return player_ranks

# Example usage
# ranked = [100, 90, 90, 80, 75, 60]
# player = [50, 65, 77, 90, 102]
# print(climbingLeaderboard(ranked, player))
