# This is a little exercise where we have to create a mario obstacle
def main():
    print_column(3)
    print_row(4)
    print_square(3)

# Prints one column    
def print_column(height):
    print("#\n" * height, end="")

# Print one row
def print_row(width):
    print("#" * width)

# Print a block 3x3
def print_square(size):
    for i in range(size):
        print_row(size)

# def print_square(size):
#     # For each row in square
#     for i in range(size):
#         # For each brick in row
#         for j in range(size):   
#             # Print brick
#             print("#", end="")
#         print()

# Compact version
# def print_square(size):
#     for i in range(size):
#     print("#" * size)
        
        

main()