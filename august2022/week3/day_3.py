    
# class employee:      

#     def __init__(self,name,work,leaves) -> None:
#         self.name=name
#         self.work=work
#         self.leaves=leaves
        
#     def pprint(self):
#         return f"name is {self.name} work hours is {self.work} hours"

#     @classmethod
#     def change_leaves(cls,newleaves):
#         cls.no_of_leaves=newleaves

#     @classmethod
#     def s_t_r(cls,string):
#         p=string.split("-")
#         # return cls (p[0],p[1],p[2])
#         return cls (*string.split("-"))



# sujit=employee("sujit","devleper",8)
# ankit=employee("ankit","accountant",1)
# sumit=employee.s_t_r("sumit-peun-0")
# print(sumit.__dict__)
# sujit.change_leaves(21)
# print(sumit.work)
# a=[-4,3,-9,0,4,1]
# def hacker(a):
#     plus=[]
#     minus=[]
#     z=[]
#     for x in (a):
#         if x > 0:
#             plus.append(1)
#         elif x < 0:
#             minus.append(1)
#         else: 
#             z.append(1)
#     v= "{:.6f}\n{:.6f}\n{:.6f}" 
#     print( v.format(len(plus)/len(a) ,len(minus)/len(a),len(z)/len(a)))
# (hacker(a))
# p
def staircase(n):
    p=1
    while p <= n:
        a="#" * p
        print(a.rjust(n))
        p +=1
staircase(10)   
# def stair(n)
    # for x in



