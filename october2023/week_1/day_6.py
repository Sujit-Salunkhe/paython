p=[4,3,5,1,2]
# y=[]
# p.insert(0,0)
# [p.index(p.index(x)) for x in range(1,len(p))]


def permutationEquation(p):
    p.insert(0,0)
    return [p.index(p.index(x)) for x in range(1,len(p))]

j=permutationEquation(p)

print(j)