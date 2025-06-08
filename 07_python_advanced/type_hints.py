# 07_python_advanced/type_hints.py

# Advanced Types Hints (PEP 484, PEP 586, PEP 589, PEP 604, etc.)

# Type hints add optional type information 

# Type hints improve readability, IDE support, static analysis (e.g. mypy, pyright).
# They do not affect runtime behavior unless explicitly checked.

from typing import (
    Optional, Union, Callable, Any, Literal, Final,
    NoReturn, TypedDict, TypeVar, Generic, ClassVar, Protocol
)
from dataclasses import dataclass


# Function signatures
def add(a: int, b: int) -> int:
    return a + b

def square_or_none(x: Optional[int]) -> Optional[int]:
    return None if x is None else x * x

def combine(a: int | float, b: int | float) -> float:
    return a + b

# Callable types
def operate(a: int, b: int, func: Callable[[int, int], int]) -> int:
    return func(a, b)

# Any and NoReturn
def accepts_any(x: Any) -> None:
    print("Accepted:", x)

def fatal_error(msg: str) -> NoReturn:
    raise RuntimeError(msg)

# Literal (fixed values)
def status(state: Literal["open", "closed"]) -> None:
    print("State:", state)

# TypedDict (typed dicts without defining a full class)
class UserDict(TypedDict):
    id: int
    name: str
    email: str

def send_email(user: UserDict) -> None:
    print("Email sent to", user["email"])

# Final (constants)
PI: Final = 3.14159

# ClassVar (shared across instances)
@dataclass
class Point:
    x: float
    y: float
    label: ClassVar[str] = "2D point"

# TypeVar and Generic
T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

int_stack = Stack[int]()
int_stack.push(42)

# Protocols (duck typing with structure, not inheritance)
class HasLength(Protocol):
    def __len__(self) -> int: ...

def show_length(obj: HasLength) -> None:
    print("Length is", len(obj))

show_length([1, 2, 3])  # OK
# show_length(42)       # Type checker would reject this

# Overloading
from typing import overload

@overload
def double(x: int) -> int: ...
@overload
def double(x: str) -> str: ...

def double(x):  # actual implementation
    return x * 2

print(double(5))     # 10
print(double("Hi"))  # "HiHi"


# Tools

# - mypy: static type checker
#     $ mypy type_hints.py

# - pyright: fast, powerful checker
#     $ pyright

# - IDEs like PyCharm, VS Code use type hints for autocomplete and validation

