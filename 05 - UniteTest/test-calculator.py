from calculator import square

def main():
    test_square()

# I've made it this way, because it easier to test errors like this
def test_square():
    for n in range(-10,10):
        if square(n) != n*n:
            print(f"{n} square was not {n*n}")
        n += 1
        
if __name__ == "__main__":
    main()