# parent class
class Animal:
    def eat(self):
        print(f'Animal is eating the food.')
        print("--------------------")


# child class
class Dog(Animal):
    pass


def main():
    dog1 = Dog()
    dog1.eat()


if __name__ == "__main__":
    main()