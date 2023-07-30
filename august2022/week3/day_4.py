class employee:      

    def __init__(self,name,work,leaves) -> None:
        self.name=name
        self.work=work
        self.leaves=leaves
        
    def pprint(self):
        return f"name is {self.name} work hours is {self.work} hours"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

    @classmethod
    def s_t_r(cls,string):
        p=string.split("-")
        # return cls (p[0],p[1],p[2])
        return cls (*string.split("-"))
    @staticmethod
    def printgood(string):
        print("i am  a good boy" + string)


sujit=employee("sujit","devleper",8)
ankit=employee("ankit","accountant",1)
sumit=employee.s_t_r("sumit-peun-0")
print(sumit.__dict__)
sujit.change_leaves(21)
print(sumit.work)
(sujit.printgood(" sujit"))

