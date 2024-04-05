# Math modules
#def calculate_area_of_circle(radius):
   # PI = 3.14
   # return PI * radius * radius

#def calculate_area_of_circle_using_math(radius):
 #   return math.pi * radius * radius


#radius=int(input("enter the value of the radius-"))
#area = calculate_area_of_circle(radius)
#print(areaOne)
#print(areaTwo)


# Strong Numbers
# n--> upper_range--> 1000--> 1 - 1000
# 145--> 1! + 4! +5!

# Functions to find a factorial of a given number
#def factorial(num) -> int:
 #   if(num == 0):
  #      return 1
   # return num * factorial(num-1)

# Function to check for a strong number
#def isstrong(num)->bool:
    # Reverse a number ->FORMULA
 #   medium = str(num)
    # loop can access each digit the number
  #  for i in range(len(medium)):
   #     sum += factorial(int(medium(i)))

    #if(sum == num):
     #   return True
    #else:
     #   return False

# Driver code
#n = int(input("enter an upper range - "))
#for value in range(1, n+1):
 #   if(isstrong(value) ):
  #      print(value)


# Math Module
#import math

# Math Module -> Constants
#print(math.pi)
#print(math.tau)
#print(math.e)
#print(math.inf)
#print(-math.inf)

# Methods
# 1. ceil()
#print(math.ceil(2.35))
#print(math.floor(2.35))

# 2.factorial
#print(math.factorial(5))

# Absolute value -> fabs(number) -> float
#print(math.fabs(-10))

# Logarithemic Operations
#x = 10
#print('e^x is - ',math.e ** x)

#print(math.log(x))
#print(math.log2(x))
#print(math.log10(x))

# Trigonometric Functions
#x = 10
#print(math.sin(x))
#print(math.cos(x))
#print(math.tan(x))

# Square root
#print(math.sqrt(x))



class Dog:
    # statements
    name = "Tommy"
    def bark(self):
        print("{} is barking".format(self.name))


Tommy_obj = Dog()
Tommy_obj.bark()   #self -> Tommy_obj

Tiger_obj = Dog()
Tiger_obj.name = "Tiger"
Tiger_obj.bark()   # self -> Tiger_obj

#print(Tommy_obj.name)


class Person:
    # class variable 
    breed = "Mammals"
    # Constructor : initialise objects during thier creation
    def __init__(self, name1, age, gender):
      self.name = name1    # object variable or instance variable
      self.age = age
      self.gender = gender

    def printName(self):
        print("Hello, my name is", self.name)

    def changeName(self, name):
         self.name = name



vegitha = Person("Vegitha Tangde", 18, "Female")
vegitha.printName()   # Person.printName(vegitha, )
print(Person.breed)

print(vegitha.breed)

vegitha.changeName("Samitha")
vegitha.printName()

class ComplexNumber:
    def __init__(self, r, i):
        self.real = r
        self.imag = i

    def get_data(self):
        print(f'{self.real} + i{self.imag}')

num1 = ComplexNumber(2, 3)
num1.get_data()

num2 = ComplexNumber(5)
num2.get_data()

num2.attr = 10

print(num2.real, num1.imag, num2.attr)
