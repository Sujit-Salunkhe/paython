# a = 17
# x = (len(str(bin(a))[2:]) +1)
# for i in range(1,a+1):
#     print(f'{i: >{x}}{str(oct(i))[2:]: >{x}}{str(hex(i)).upper()[2:]: >{x}}{str(bin(i))[2:]: >{x}}')
    
# def print_rangoli(N):
#     cols = (4 * N) - 3
#     k = []
#     k1 = []
#     line = ""
#     x = [chr(idx) for idx in range(-(96+N)*-1, 96, -1)]
#     for i in range(N):
#         line = line + x[i] + "-"
#         g = line[-4::-1]
#         k.append((line + g).center(cols, "-"))
#     k1 = [k[i] for i in range(N-2, -1, -1)]
#     if N ==1:
#         print(x[0])
#     else:
#         print(*k, sep='\n')
#         print(*k1, sep='\n')
    

# print_rangoli(5)
# l=[]
# l[0]=2
list=[34,34,34]
list.append(3)
print(list)
list[0]=90
print(list)