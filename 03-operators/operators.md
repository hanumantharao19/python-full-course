

```

```
## Basic Math Operators
```
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)
```

## addition of strings
```
print("hanu" + "medikonda")
print("hanu" + str(30))
print("hanu"+30) # given error
```

```
name = "hanu"
age = 30
print(name + " is " + str(age) + " years old.")
```
## Compound Assignment Operators
## Using += to Add and Assign
```
number = 5 
number += 2 # same as number = number+2
print(number)
```
## Using -= to Subtract and Assign
```
balance = 100
balance -= 25  # same as: balance = balance - 25
print(balance)
```
## Using *= to Multiply and Assign
```
points = 10
points *= 3  # same as: points = points * 3
print("After *= :", points)  # Output: 30
```
##  Using /= to Divide and Assign
```
total = 20
total /= 4  # same as: total = total / 4
print(total)  # Output: 5.0
```
## Using //=, %=, **=
```
num = 10
num //= 3  # Floor division
print("After //= :", num)  # Output: 3

num = 10
num %= 3  # Modulus
print("After %= :", num)  # Output: 1

num = 2
num **= 3  # Exponentiation
print("After **= :", num)  # Output: 8
```
## Relational Operators
```
a = 10
b = 20

print(a == b)   # False → because 10 is not equal to 20
print(a != b)   # True  → because 10 is not equal to 20
print(a > b)    # False → 10 is not greater than 20
print(a < b)    # True  → 10 is less than 20
print(a >= b)   # False → 10 is not greater than or equal to 20
print(a <= b)   # True  → 10 is less than or equal to 20
```
## logical operator
## and opearator
```
x = 10
print(x > 5 and x < 15)   # True and True → True
print(x > 5 and x > 15)   # True and False → False
```
## or operator
```
x = 10
print(x < 5 or x < 15)    # False or True → True
print(x < 5 or x < 2)     # False or False → False
```
## not operator
```
x = 10
print(not(x > 5))         # not(True) → False
print(not(x < 5))         # not(False) → True
```
## bit wise operator
```
a = 5   # Binary: 0101
b = 3   # Binary: 0011

a & b (AND)
print(a & b)  # 0101 & 0011 = 0001 → Output: 1

a | b (OR)
print(a | b)  # 0101 | 0011 = 0111 → Output: 7

a ^ b (XOR)
print(a ^ b)  # 0101 ^ 0011 = 0110 → Output: 6

~a (NOT)
print(~a)     # ~0101 = -(a+1) = -6

a << 1 (Left Shift)
print(a << 1) # 0101 << 1 = 1010 → Output: 10

a >> 1 (Right Shift)
print(a >> 1) # 0101 >> 1 = 0010 → Output: 2

```
# Ternary Operator in Python
```
age = 20
result = "Adult" if age >= 18 else "Minor"
```
# Python Operator Precedence (from highest to lowest)
| Precedence  | Operator(s)                                                      | Description                       |            |
| ----------- | ---------------------------------------------------------------- | --------------------------------- | ---------- |
| 1 (Highest) | `()`                                                             | Parentheses (grouping)            |            |
| 2           | `**`                                                             | Exponentiation                    |            |
| 3           | `+x, -x, ~x`                                                     | Unary plus, minus, bitwise NOT    |            |
| 4           | `*`, `/`, `//`, `%`                                              | Multiplication, division, modulus |            |
| 5           | `+`, `-`                                                         | Addition and subtraction          |            |
| 6           | `<<`, `>>`                                                       | Bitwise shift operators           |            |
| 7           | `&`                                                              | Bitwise AND                       |            |
| 8           | `^`                                                              | Bitwise XOR                       |            |
| 9           | \`                                                               | \`                                | Bitwise OR |
| 10          | `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `is not`, `in`, `not in` | Comparisons                       |            |
| 11          | `not`                                                            | Logical NOT                       |            |
| 12          | `and`                                                            | Logical AND                       |            |
| 13          | `or`                                                             | Logical OR                        |            |
| 14          | `if ... else`                                                    | Ternary conditional expression    |            |
| 15 (Lowest) | `=`, `+=`, `-=`, etc.                                            | Assignment operators              |            |