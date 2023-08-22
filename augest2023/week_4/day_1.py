# import cmath 
# c=1+2j
# p=input()
# k=abs(complex(c))
# print(k)
# print(cmath.phase(complex(c)))
import cmath
number,number2=input().split("+")
print(number,number2)
print(cmath.phase(complex(number)))
print(abs(complex(number2)))