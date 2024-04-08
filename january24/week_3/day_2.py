# a=45
# b=34
import math
# a=25
# print(math.sqrt(a))


def findroutes(a,b):
    i = int(math.ceil(math.sqrt(a)))
    count = 0
    while i * i <= b:
        count +=1
        i += 1
    return count    


# print(findroutes(3,9))


# print(int(math.ceil(math.sqrt(3))))
# class person:
#     def __init__(self,initialAge):
#         # Add some more code to run some checks on initialAge
#         if initialAge < 0:
#             self.age = 0
#             print('Age is not valid, setting age to 0.')
#         else:
#             self.age = initialAge
            
#     def amIOld(self):
#         # Do some computations in here and print out the correct statement to the console
#         if self.age < 13:
#             print('You are young.')
#         elif self.age in range(13, 18):
#             print('You are a teenager.')
#         else:
#             print('You are old.')
            
#     def yearPasses(self):
#         # Increment the age of the person in here
#         self.age += 1

dimensions = [
[1, 1, 1, 0, 0, 0],
[0 ,1 ,0 ,0 ,0 ,0],
[1 ,1, 1, 0, 0, 0],
[0 ,0, 2 ,4 ,4 ,0],
[0, 0, 0, 2, 0, 0],
[0 ,0 ,1 ,2 ,4 ,0]]

dimensions2 =[[
     0, -4, -6, 0 ,-7, -6],
[-1 ,-2 ,-6 ,-8 ,-3 ,-1],
[-8, -4, -2, -8, -8, -6],
[-3 ,-1 ,-2 ,-5 ,-7 ,-4],
[-3, -5, -3, -6, -6, -6],
[-3, -6, 0, -8, -6, -7]
]
sum = float('-inf')
new_sum = 0
# for i in range(4):
for k in range(0,len(dimensions2)-2):
    for j in range(0,len(dimensions2[1])-2):
            new_sum = dimensions2[k][j] + dimensions2[k][j+1] + dimensions2[k][j+2] + dimensions2[k+1][j+1] + dimensions2[k+2][j] +  dimensions2[k+2][j+1] +  dimensions2[k+2][j+2] 
            if new_sum > sum:
                sum = new_sum
print(sum)

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    def calculate(self):
        self.avg = sum(self.scores)/len(self.scores)
        self.grade = ''
        if self.avg <= 100 and self.avg >=90:
            self.grade = 'O'
            return self.grade
        elif self.avg < 90 and self.avg >=80:
            self.grade = 'E'
            return self.grade
        elif self.avg < 80 and self.avg >=70:
            self.grade = 'A'
            return self.grade
        elif self.avg < 70 and self.avg >=55:
            self.grade = 'P'
            return self.grade
        elif self.avg < 55 and self.avg >=40:
            self.grade = 'D'
            return self.grade
        elif self.avg < 40:
            self.grade = 'T'
            return self.grade

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())


def insert(self,head,data): 
    if head == None:
        head = Node(data)
    else:
        current = head
        while current.next:
            current = current.next
        current.next = Node(data)
        return head
 

