class Person():
    def __init__(self, initialAge):
        if initialAge > 0:
            self.age = initialAge
        else:
            print("Age is not valid, setting it to 0.")
            self.age = 0

    def amIOld(self):
        if self.age  < 13:
            print("You are young")

        elif self.age >= 13 and self.age < 18:
            print("You are a teenager")

        else:
            print("Youre old")

    def YearPasses(self):
        self.age +=1


Tom = Person(13)

print(Tom.amIOld())
