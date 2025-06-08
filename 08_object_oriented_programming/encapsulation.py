# 08_object_oriented_programming/encapsulation.py

# Encapsulation in Python

# Encapsulation is about hiding internal data and implementation details.
# Python uses naming conventions rather than strict access control like other languages.


# 1. Encapsulating internal state with "private" attributes

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # "__" = name mangling for pseudo-private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

# Usage
acc = BankAccount("Alice", 1000)
acc.deposit(200)
acc.withdraw(150)
print("Balance:", acc.get_balance())  # 1050


# 2. Attempt to access private attribute (not allowed directly)

# print(acc.__balance)  # AttributeError: attribute is "private"

# You *can* force access using name mangling (not recommended)
print("Forced access:", acc._BankAccount__balance)  # 1050


# 3. Using single underscore for "protected" attributes (convention only)

class User:
    def __init__(self, username):
        self._username = username  # _name = protected by convention

class Admin(User):
    def reveal(self):
        print("Accessing protected:", self._username)

a = Admin("root")
a.reveal()

# External code *can* still access _username — it’s a convention, not enforcement
print("Direct access:", a._username)


# 4. Using @property for controlled read/write access

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price >= 0:
            self._price = new_price
        else:
            raise ValueError("Price cannot be negative")

p = Product(50)
print("Price:", p.price)   # Getter
p.price = 80               # Setter
print("New price:", p.price)

# p.price = -10  # Raises ValueError


# 4b. Manual getters and setters (before @property)

class Student:
    def __init__(self, name):
        self._name = name  # treated as "private" by convention

    def get_name(self):
        return self._name

    def set_name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

s = Student("Bob")
print(s.get_name())   # Bob
s.set_name("Alice")
print(s.get_name())   # Alice

# Classic style still seen in legacy code and some Java-style libraries


# 4c. Replacing getters/setters with @property

class ModernStudent:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

m = ModernStudent("Charlie")
print(m.name)        # Calls getter
m.name = "Dana"      # Calls setter
print(m.name)

# This is the modern, Pythonic way to expose controlled access


# 5. Why encapsulation matters

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    def to_fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    def set_celsius(self, value):
        # validation logic here
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = value

    def get_celsius(self):
        return self._celsius

t = Temperature(25)
print("F:", t.to_fahrenheit())

t.set_celsius(0)
print("Updated C:", t.get_celsius())

# t.set_celsius(-300)  # Raises ValueError


# 6. Avoiding access via __dict__ or introspection

# Python allows bypassing all conventions via introspection.
# This should not be done in production code unless debugging.

print("Hacky access via __dict__:", acc.__dict__)  # Shows all internal data


# Summary (in-line, no extra block):
# - __double underscores = name mangling (not true private)
# - _single underscore = "protected" by convention
# - Use @property for safe public access with validation
# - Avoid accessing internals directly — respect encapsulation
