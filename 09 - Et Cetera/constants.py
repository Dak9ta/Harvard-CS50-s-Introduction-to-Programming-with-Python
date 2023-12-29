class Cat:
    MEOWS = int(input("How many times the cat meows? "))
    
    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")
            
cat = Cat()
cat.meow()