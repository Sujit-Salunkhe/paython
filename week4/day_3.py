# class mycalss():
#    x=5
#    y=5
# p=mycalss()
# print(p.y)
# class persons:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1=persons("sujit",16)
# print(p1.name)
# print(p1.age)
# sujit=marks()
# sujit.work=15
# print(sujit.__dict__    )
# class marks:
#     def __init__(self,name,age):
#         self.age=age
#         self.name=name
#     def fuc(self):
#         print("hello my name is "+ self.name)
# class marks:
#     def __init__(joke,name,std):
#         joke.name=name
#         joke.std=std
#     def names(abd):
#         print("my name is " + abd.name)
# sujit=marks("sujit",90)
# sujit.names()
#         print("my age is " +  self.age)

# a=person("sujit","salunkhe")
# a.printname()
# sujit=marks("sujit","15")
# # sujit.fuc()
# class marks:
#         print("my name is " + abd.name)
#     def __init__(joke,name,std):
#         joke.name=name
#         joke.std=std
#     def names(abd):
# sujit=marks("sujit",90)
# sujit.names()
class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lname=lname
        
    def printname(self):
        print(self.firstname,self.lname)
    def std(self):
        print("name is sujit" + self.firstname)
class sujit(person):
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
        self.graduvation_year=year
    def all(self):
        print("welcome",self.firstname,self.lname,"graduvate in a year",self.graduvation_year)
   
x=sujit("sujit","salunkhe",2020)
x.all()
# x.printname()   



"""
creating a big data base for 100 millon users
insert=the profile information for a new user.
find=the profile information of a user given their usernames
update=the profile information of  a user,given their username 
list =all the users of the platform,sorted by username 


"""

class userdatabase:
    def insert(self,user):
        pass
    def find(self,username):
        pass
    def update(self,user):
        pass
    def listall(self):
        pass