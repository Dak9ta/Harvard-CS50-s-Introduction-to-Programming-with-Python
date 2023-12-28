# Here we define the parameter value
def hello(to="world"):
    print ("hello, " + to)

# First the program says hello to the world
hello()
name = input("What's your name? ") 
# Now the program says hello to you
hello(name)