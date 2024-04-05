# FUNCTIONS

x = 6
x = 'jatin'
x = 1.5
x = print


def show_loading():
    for _ in range(3):
        print("loading",".",(_+1))

show_loading()
a = 5
b = 7

print(a + b)
show_loading()

print(a-b)
show_loading()

print(a*b)
show_loading()


# Functions can take parameters

def sheldon_knock():
      for _ in range(3):
           print("knock knock knock penny")
        
sheldon_knock()


def sheldon_knock(name):
    for _ in range(3):
        print("knock knock knock", name)

sheldon_knock("leonard")

                                           
def sheldon_knock(name, times = 3):
     for _ in range(times):                         
          print("knock knock knock", name)
                                                 # Default Arguments
sheldon_knock("penny", 100)


# Return Statement

def add(a, b):
     return a + b
a = add(1, 2)
print(a)