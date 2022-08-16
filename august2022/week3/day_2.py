# class sujit:
#     pass
# akash=sujit()
# lens=sujit()
# akash.work=45   
# akash.education=12
# lens.suj=-1.25

# print(akash,lens)
# print(lens.suj)
class employee:
    # no_of_leav        es=6
    def __init__(self,name,work,leaves) -> None:
        self.name=name
        self.work=work
        self.leaves=leaves
        
    def pprint(self):
        return f"name is {self.name} work hours is {self.work} hours"


sujit=employee("sujit","devleper",8)
ankit=employee("ankit","accountant",1)
# print(sujit.__dict__) 
print(sujit.__dict__)
print(ankit.__dict__)
#     pass
# sujit=employee()
# anita=employee()
# sujit.work=12
# anita.work=12
# sujit.name="sujit"
# anita.name="anu"


# # print(sujit.work,anita.name)
# # print(sujit.__dict__    )
# # print(sujit.no_of_leaves)
# print(sujit.pprint())
# print(anita.pprint())
    