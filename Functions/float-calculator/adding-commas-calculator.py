# This is a rounding calculator that adds commas in big numbers
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

print(f"{z:,}")