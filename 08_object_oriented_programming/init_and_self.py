# 08_object_oriented_programming/init_and_self.py

# __init__ is the constructor method called when an object is created
# self refers to the current instance of the class

class Car:
    def __init__(self, brand, year):
        self.brand = brand    # instance variable
        self.year = year

    def display_info(self):
        print(f"{self.brand} was made in {self.year}")

# Create objects
car1 = Car("Toyota", 2020)
car2 = Car("Ford", 2018)

car1.display_info()  # Toyota was made in 2020
car2.display_info()  # Ford was made in 2018

# self must always be the first parameter in instance methods

