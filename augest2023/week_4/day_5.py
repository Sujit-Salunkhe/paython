
my_emplyess={"sujig":"001","king":"343"}


# print(my_emplyess.keys())
# print(my_emplyess.values())
# print(my_emplyess.get("sujig"))
# print("a
# " < "B")
input_string="qwertyuiopasdfghjklzxcvbnm"
char_count={}
for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

sorted_chars2= sorted(char_count.items(),key=lambda x:x[0])
dictionary={key:value for key,value in sorted_chars2}
sorted_chars = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
print(sorted_chars2)
for x,y  in sorted_chars:
    print(x,y)
    pass
