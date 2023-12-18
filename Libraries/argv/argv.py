import sys

# Check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

# Print name line
print("hello, my name is", sys.argv[1])
    
# Try to prevent the error message
# try:
#     print("hello, my name is", sys.argv[1]) # Is like an input, but you have to enter your name after the program name: "python program.py name"
    
# except IndexError:
#     print("You have to enter your name after the program name")