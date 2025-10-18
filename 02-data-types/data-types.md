## Applications of Python
| S.No | Area                         | Description                                                                 |
| ---- | ---------------------------- | --------------------------------------------------------------------------- |
| 1️⃣  | **Desktop Applications**     | GUI apps using tools like Tkinter, PyQt, Kivy                               |
| 2️⃣  | **Web Applications**         | Backend development using Django, Flask, FastAPI                            |
| 3️⃣  | **Database Applications**    | Applications that store/retrieve data using MySQL, PostgreSQL, SQLite       |
| 4️⃣  | **Networking Applications**  | Network tools, socket programming, automating network tasks                 |
| 5️⃣  | **Games**                    | Simple to complex games using Pygame, Panda3D                               |
| 6️⃣  | **Data Analysis**            | Libraries like Pandas, NumPy, Matplotlib for analyzing and visualizing data |
| 7️⃣  | **Machine Learning**         | ML models using Scikit-learn, TensorFlow, PyTorch                           |
| 8️⃣  | **Artificial Intelligence**  | AI apps: speech, vision, chatbots, NLP                                      |
| 9️⃣  | **IoT (Internet of Things)** | Python is used in Raspberry Pi & microcontroller-based applications         |

## Features of Python
| No.    | Feature                             | Explanation                                                 |
| ------ | ----------------------------------- | ----------------------------------------------------------- |
| 1️⃣    | **Simple and Easy to Learn**        | Python has clean syntax similar to English                  |
| 2️⃣    | **Freeware and Open Source**        | Free to download, use, and modify                           |
| 3️⃣    | **High-Level Programming Language** | You don’t need to manage memory or hardware details         |
| 4️⃣    | **Platform Independent**            | Runs on Windows, Linux, macOS, etc.                         |
| 5️⃣    | **Portable**                        | Write once, run anywhere                                    |
| 6️⃣    | **Dynamically Typed**               | No need to declare variable types                           |
| 7️⃣    | **Procedural and Object-Oriented**  | Supports both styles of programming                         |
| 8️⃣    | **Interpreted Language**            | Code is executed line by line                               |
| 9️⃣    | **Extensible**                      | Can include C/C++ code in Python                            |
| 🔟     | **Embeddable**                      | Python code can be embedded in other languages (like C/C++) |
| 1️⃣1️⃣ | **Extensive Library Support**       | Rich standard and third-party libraries for every need      |

## limitation
1) performance issue
2) not used much in mobile applicatons

## Python supports various built-in data types:

| Type        | Description                   | Example                |
| ----------- | ----------------------------- | ---------------------- |
| `int`       | Integer numbers               | `x = 10`               |
| `float`     | Decimal numbers               | `pi = 3.14`            |
| `complex`   | Complex numbers               | `z = 3 + 4j`           |
| `bool`      | Boolean values                | `True`, `False`        |
| `str`       | String/text                   | `"Hello"`              |
| `range`     | Sequence of numbers           | `range(5)`             |
| `list`      | Ordered, mutable collection   | `[1, 2, 3]`            |
| `tuple`     | Ordered, immutable collection | `(1, 2, 3)`            |
| `set`       | Unordered, unique values      | `{1, 2, 3}`            |
| `frozenset` | Immutable set                 | `frozenset([1, 2, 3])` |
| `dict`      | Key-value pairs               | `{"name": "Hanuman"}`  |
| `None`      | Represents no value or null   | `x = None`             |


## Print a Name in Python
```
print("This is Hanumantharao")
```
## How to Comment in Python
```
"""
This is a multi-line comment.
Author: Hanumantharao Medikonda
Location: NRT, Andhra Pradesh
"""
print("This is Hanu")
```
## Python Data Types
```
age = 20                    # int
price = 19.23               # float
name = "Hanu"               # string
are_coming = False          # boolean
number = 10+20J             # complex

print(age)
print(price)
print(name)
print(are_coming)
```

## Type Checking in Python
```
x = 25
y = "Hello"
z = 3.14
a = 10+20J

print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>
print(type(z))  # <class 'float'>
print(type(a))  # <class 'complex'>
```
## Accessing characters using index
```
name = "hanumantharo"
print(name[0])     # h
print(name[1])     # a
print(name[4])     # m
print(name[-1])    # o (last character)
print(name[-4])    # h (4th character from the end)
```
##  Slicing operation on string
-  Syntax: sequence[start:stop]
-  It returns a substring from start to stop-1 index
- Syntax: sequence[start:stop:step]
```
print(name[1:4])    # anu
print(name[3:6])    # uma
print(name[1:])     # anumantharo → from index 1 to end
print(name[:5])     # hanum → from start to index 4
```
## Negative indexing
```
print(name[-1:-4])   # '' (empty string because start > stop)
print(name[-4:-1])   # har → characters from -4 to -2