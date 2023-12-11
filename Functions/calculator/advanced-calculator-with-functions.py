# This is an advanced version of the calculator with defined functions
def main():
    x = int(input("What's x? "))
    print ("x squared is", square(x))
    
def square(n):
    return pow(n, 2) #you can use pow instead of writing n*n, is your preference
    
    
main()