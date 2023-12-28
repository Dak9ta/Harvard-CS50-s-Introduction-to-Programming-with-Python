# This is a correct function use
def main():
    name = input("What's your name? ")
    hello(name)
    
def hello(to="world"):
    print ("hello, " + to)
    
# To not get an error when running the program you have to define main to the bottom
main()