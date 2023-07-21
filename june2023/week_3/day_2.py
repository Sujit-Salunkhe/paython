sujit=[2,3,344]
# s=344
# if sujit[3]==s:
#     print("it' matched")
# else:
#     print("it's not matched")
# suji="sujit"
# print(suji[4])
num = str(input())
result = []
c = 1

for i in range(0, len(num) + 1):
    if i == len(num) - 1:
        result.append((c, " ", int(num[i])))
        break
    if num[i] == num[i + 1]:
        c += 1
    else:
        result.append((c, " ", int(num[i])))
        c = 1

output = '  '.join(f'({(count)}, {digit})' for count,  digit in result)
print(output)