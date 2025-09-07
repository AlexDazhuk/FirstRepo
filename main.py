a = 12
b = 34
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)
print(a % b)

import math
print(math.ceil(a / b))
print(math.floor(a / b))

def plus(x: int, y: int) -> int:
    return x + y
print(plus(190, 15))

def minus(x: int, y: int) -> int:
    return x - y
print(minus(190, 15))

def multiply(x: int, y: int) -> int:
    return x * y
print(multiply(190, 15))

def mul_1(x: float, y: float) -> float:
    return x * y
print(mul_1(190.5, 15))

def divide(x: int, y: int) -> float:
    return x / y
print(divide(190, 15))

def div_1(x: float, y: float) -> float:
    return x / y
print(div_1(190.5, 15.1))