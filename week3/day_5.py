# a = input()
# b =input()
# print(int(a)+int(b))
# def locate_card(cards,query):
#     position=0
#     while position < len(cards):
#         if cards[position]==query:
#             return position 
#         position =+ 1
        
#     return -1



# # print(locate_card(input,query))
# a=["s","f","h"]
# # b="f"
# b=[]
# print(len(b))
from tokenize import Number
from turtle import right
def test_cards(cards,query,mid):
    if cards[mid] == query:
        if mid >=0 and cards[mid-1]==query:
            return "right"
        else:
            return "got it"
    elif cards[mid]<query:
        return "right"
    else:
        return "left"


def locate_cards(cards,query):
    lo=0
    hi=len(cards)-1
    while lo <= hi:
        mid = (lo + hi)//2
        # mid_number=cards[mid]
        result=test_cards(cards,query,mid)
        

        if result == "got it":
            return mid
        elif result == "right":
            hi = mid - 1
        elif result == "left":
            lo = mid + 1
    return -1
input=[13,45,85,69,789,78,]
query=45
print(locate_cards(input,query))
a = [48,52,60,85,102]
Number=85
def first_position(number,target):
    def condition(mid):

        if number[mid]==target:
            pass
        





