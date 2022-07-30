from gettext import find
# print("hello,world")
# print(9<10)
def find_card(cards,query):
    position=0
    while position<len(cards) :
        if cards[position]==query:
            return position
        position += 1
        if cards[position]==len(cards):
            return -1
    return -1
# a =[13,10,8,5,4,1,]
# b=10
a=[12,10,9,9,9,9,9,9,8,7,6]
b=9
c=[]

d=13
print(find_card(a,b))
        
  