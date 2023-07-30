# s=7 
# t=12
# orange=15
# apple=5
# dropa=3
# dropo=2
# apples=[-2,2,1]
# oranges=[5,-6]
# home = 0
# # def count(s,t,orange,apple,dropa,dropo,apples,oranges):
# # for i in range(len(apples)):
# #     if t >= (apples[i] + apple) and s <=(apples[i] + apple) :
# #         home +=1
# # for i in range(len(oranges)):
# #     if s >= (oranges[i] + orange) and s <=(oranges[i] + orange) :
# #         home +=1
    
# # print(home)
# for i in range(len(apples)):
#     if t >= (apples[i] + apple) and s <=(apples[i] + apple) :
#         home +=1
# print(home)
# home = 0
# for i in range(len(oranges)):
#     if t >= (oranges[i] + orange) and s <=(oranges[i] + orange) :
#         home +=1
# print(home)

# sujit=[84,544,234,56,56]
# def counts(a):
#     for i in range(len(a)):
#         print(a[i])
# counts(sujit)
def kangaru(a,b,c,d):
        if a < c and b < d:
            return "NO"
        if d > b:
            if (b%2 == 0) and ( d%2 == 0 ):
                    return "NO" 
        if d > b:
            if(b%3 == 0) and (d%3 == 0):
                return "NO"
        else:
            return "yes"
    
print(kangaru(0,3,4,2))