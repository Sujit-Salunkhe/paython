# j=0
# for i in range(len(birds)-1):
#     print (i < len(birds))
#     while i < (len(birds)):
#         if i == j:
#             print(i,j)
#             i += 1
#         elif birds[i] == birds[j]:
#             j+=1
#             print(birds[i])
        


# print(range(len(birds)))
# for i in range(len(birds)):
#     print(i)


birds=[1,2,3,3,4,4,3]
value=0
result=0
for x in sorted(set((birds))):
    count = birds.count(x)
    if value > count:
        value = value
    elif value == count:
        if result > x:
            result = x
        else:
            result = result
    else:
        value = count
        result=x

print(result)
    
# type1=0
# type2=0
# print(sorted(set(birds)))
# type3=0
# type4=0
# type5=0
# birdss=[]
# for i in range(len(birds)):
#     if  (birds[i] == 1):
#             type1 +=1
#     elif  (birds[i] == 2):
#             type2 +=1
#     elif  (birds[i] == 3):
#             type3 +=1
#     elif  (birds[i] == 4):
#             type4 +=1
#     else:
#             type5+=1
    
    
# print(type1,type2,type3,type4,type5)


