# This is program starts with an infinite loop breaked if the num > 0 
while True:
    num = int(input("How many times does the cat meow? "))
    
    if num > 0:
        break
    
for i in range(num):
    print("meow")