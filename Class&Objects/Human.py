class Human:

    # Constructor
    def __init__(self):
        self.name = ""
        self.age = 0
        self.country = ""
        self.fathers_name = ""

        print("Object of Human is created:", self.name)

    def eat(self):
        print(f'{self.name} is eating the food.')
        print(f'whose age is {self.age}')
        print("----------------")

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Country:", self.country)
        print("Father's Name:", self.fathers_name)
        print("----------------")


def main():
    print("Program Started")

    # Human 1
    human1 = Human()

    human1.name = "ankit"
    human1.age = 20
    human1.country = "INDIA"
    human1.fathers_name = "John"

    human1.display()
    human1.eat()

    # Human 2
    human2 = Human()

    human2.name = "uttam"
    human2.age = 30
    human2.country = "USA"
    human2.fathers_name = "Amit"

    human2.display()
    human2.eat()


# Call main function
main()