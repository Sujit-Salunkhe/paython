
# my_emplyess={"sujig":"001","king":"343","fja":"344"}
# print((x for x in my_emplyess.items())[:1])


# print(my_emplyess.keys())
# print(my_emplyess.values())
# print(my_emplyess.get("sujig"))
# print("a
# " < "B")
# input_string="fgeftkfiabc"
# char_count={}
# for char in input_string:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
# sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1],x[0]))
# for x,y  in sorted_chars[:3]:
#     print(x,y)
# sujit =lambda x,y,z: (x,y+z)    

# s = 'aabbbccde' # input()
# x = {},
# y = list(map(lambda i: x.update({i:len(s.split(i))-1}), set(s)))
# z = {m[0]:m[1] for m in sorted(x.items(), key=lambda k : (-k[1],k[0]))}
# for k,v in list(z.items())[:3]:
#     print(k,v)
# s = input()
s = "sjfkjakfjkjkkjjuhuhuhuhjjlk"
x = {}
list(map(lambda i: x.update({i:len(s.split(i))-1}), set(s)))
z = sorted(x.items(), key=lambda k : (-k[1],k[0]))
for k,v in z[:3]:
    print(k,v)
s=[1,5,6,6,8,4,1,4,1]
