# class Retangle:
#     type="retangle"
#     sides= 4
# 1234567890
class Employee:
    def __init__(self,fname,lname) -> None:
        self.fname=fname
        self.lname=lname
        self.Email=f"{self.fname}.{self.lname} @employees.com"
    def explain (self):
        return  f"This emplyee name is {self.fname} {self.lname}"
amar=Employee("amar","Jaiswal")
sudhir=Employee("sudhir","khan")
print(amar.explain())
print(amar.Email)

