from unicodedata import name


class employee:
    def __init__(self,name,work,time) -> None:
        self.name=name
        self.work=work
        self.time=time
    def printdetails(self):
        return (f"My name is {self.name} And My work is {self.work} And My working hours is {self.time} ")
    @classmethod
    def fromdash(cls,str):
        a=str.split("-")
        return cls(a[0],a[1],a[2])
    @staticmethod
    def printgood(string):
        return("he is a good employee "+ string)

sujit=employee("sujit","software develeper",1)
prashant=employee.fromdash("prashant-devleper-4")
# yogesh=employee(sujit.printgood('sujit'))
class programer(employee):
        def __init__(self,name,work,time,languages):
            self.name=name
            self.work=work
            self.time=time
            self.languages=languages
        def details(self):
            return (f"I am a programer and my name is {self.name} And my salary is {self.work} The languges are {self.languages}")
            
vaishnav=programer("vaishnav","zandu",3,["python","bas itna he python bhi adha he ata hai"])
print(sujit.printdetails())
print(sujit.printgood("sujit"))

class player:
    no_of_games=4
    def __init__(self,name,game) -> None:
        self.name=name
        self.game=game
    def details_print(self):
        return f"Hey my name is {self.name},And I am playing {self.game}"
aniket=player("aniket",["football","cricket","tennis","chess"])
class CoolProgrammer(employee,player):
    pass
tiger=CoolProgrammer("tiger","JavaDevleper",0.2,)
print(tiger.printdetails())

    

