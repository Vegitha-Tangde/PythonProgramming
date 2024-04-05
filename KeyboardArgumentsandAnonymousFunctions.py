# Keyword Arguments

def hello():
    print("Hello World !")
    return 1

hello()



a = 1
a = hello
print(a())

print(type(hello))

hello = 2
print(hello)

print(a())

def func():
    print("Hello")

def func(a):
    print(a)

#func()     # Error
#func(1)       


def func(a, b, c):
    print(a)
    print(b)
    print(c)

func(1, 2, 3)
func(c = 1, a = 2, b = 3)


#print(1, 2, 3, 4, 5, sep = ",")

# *args and **kwargs

#func(1, c = 5)

'''Arguments in other languages'''
# Required arguments func(a)
# Default arguments func(b=1)

'''Arguments in python'''
# Required arguments
# Default arguments
# Optional positional only arguments
# Required Keyworded only arguments
# Default Keywords only arguments
# Optional Keyworded only arguments

def func(a, b):
    print(a, b)
func(1, 2)

def func(a = 1, b = 2):
    print(a, b)

func()
func(1)
func(3, 4)

def func(a, b, *c):
    print(a)
    print(b)
    print(c)

func(1, 2, 3, 4, "jathin", 1.5)

def func(*c):
    print(c)

func()

def func(a, b, *c, d):
    print(a)
    print(b)
    print(c)
    print(d)

func(1, 2, 3, 4, 5, 6, 7, d = 8)

def func(a, b, *c, d, e = "jatin"):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

func(1, 2, 3, 4, d = "something", e = "asif")
def func(a, b = 1, *c, d, e = "", **k):
    print(k)
#func(name = "jatin")

a = 1
b = 2
c = print(a+b)

print(c)


# Anonymous function or lambda functions

def func(a):
    print(a())

def asdf():
    print("gibberish")

func(a = lambda:
    print("hello"))
