from calculator import square

def main():
    test_square()

def test_square():
    for n in range(0,100000):
        if square(n) != n*n:
            print(f"{n} square was not {n*n}")
        n += 1
        
if __name__ == "__main__":
    main()