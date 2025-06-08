# 05_data_structures/namedtuple_and_typeddict.py

from collections import namedtuple
from typing import TypedDict

# namedtuple: lightweight immutable classes with named fields

Point = namedtuple('Point', ['x', 'y'])
p1 = Point(10, 20)
print(p1)            # Point(x=10, y=20)
print(p1.x, p1.y)    # 10 20

# Namedtuples are immutable
# p1.x = 30  # AttributeError

# TypedDict: type-checked dictionary with specified keys (Python 3.8+)

class Movie(TypedDict):
    title: str
    year: int
    rating: float

movie: Movie = {
    'title': 'Inception',
    'year': 2010,
    'rating': 8.8,
}

print(movie['title'])   # Inception
print(movie)

# TypedDict helps static type checkers and IDEs

