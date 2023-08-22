# t=12
# s="UDDDUDUU"
# vally=0
# counts=0
# level=0
# for i in range(len(s)-1):
a=(-1 + -1)
b=1
print(a + b)
        
    # Write your code here
level = 0
path="DDUUDDDDUUU"
valleys = 0
for i in range(len(path)):
    if path[i] == "D":
        level -= 1
        if level == -1:
            valleys += 1
    if path[i] == "U":
        level += 1
print( valleys)
