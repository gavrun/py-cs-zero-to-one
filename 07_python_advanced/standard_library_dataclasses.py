# 07_python_advanced/standard_library_dataclasses.py

# Dataclasses reduce boilerplate for class definitions
# Simplifies class creation for storing data (since Python 3.7)

from dataclasses import dataclass, field, asdict, astuple


# Basic dataclass

@dataclass
class Point:
    x: int
    y: int

p1 = Point(2, 3)
p2 = Point(2, 3)
p3 = Point(4, 5)

print(p1)         # Point(x=2, y=3)
print(p1 == p2)   # True (auto __eq__)
print(p1 == p3)   # False


# Fields with default values

@dataclass
class Person:
    name: str
    age: int = 0

person = Person("Alice")
print(person)     # Person(name='Alice', age=0)


# Custom field configuration

@dataclass
class Config:
    secret: str = field(repr=False)  # hidden in print
    internal: int = field(init=False, default=0)  # not in __init__
    debug: bool = field(default=False)
    version: str = field(default_factory=lambda: "1.0.0")

cfg = Config(secret="xyz")
print(cfg)        # Config(debug=False, version='1.0.0')
# cfg.secret is still accessible


# Frozen dataclass (immutable)

@dataclass(frozen=True)
class ImmutablePoint:
    x: int
    y: int

p = ImmutablePoint(1, 2)
# p.x = 10  # Error: FrozenInstanceError


# Convert to dict or tuple

print(asdict(p1))     # {'x': 2, 'y': 3}
print(astuple(p1))    # (2, 3)


# Post-initialization logic

@dataclass
class User:
    name: str
    email: str
    username: str = field(init=False)

    def __post_init__(self):
        self.username = self.email.split("@")[0]

u = User(name="Alice", email="alice@example.com")
print(u.username)  # alice


# Comparison controls

@dataclass(order=True)
class OrderedItem:
    name: str
    price: float

item1 = OrderedItem("A", 10.0)
item2 = OrderedItem("B", 12.5)
print(item1 < item2)  # True


# Inheritance with dataclasses

@dataclass
class Animal:
    name: str

@dataclass
class Dog(Animal):
    breed: str

d = Dog("Fido", "Labrador")
print(d)  # Dog(name='Fido', breed='Labrador')


# Slots for memory efficiency (Python 3.10+)

@dataclass(slots=True)
class CompactPoint:
    x: int
    y: int

cp = CompactPoint(1, 2)
print(cp)


# @dataclass                         → auto __init__, __repr__, __eq__
# field(default=..., init=False, repr=False, compare=False, default_factory=...)
# frozen=True                        → immutable object
# asdict(obj), astuple(obj)         → structured conversion
# __post_init__()                   → custom init logic
# order=True                        → enables <, >, <=, >=
# slots=True                        → smaller memory footprint

