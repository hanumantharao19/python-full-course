### functions concept ####
## Positional Arguments with simple print function
```
print("Hello", "world")
```
## Positional Arguments with function use case
```
def person_details(name, age):
    print(f"Hello {name}, you are {age} years old.")

person_details("hanu", 30)
```

## Keyword Arguments with simple print function
```
print("I read the whole", end="")
print("line at one glance", end="!")

```
## Keyword Arguments with function use 
```
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet(age=30n,age="hanu")
```

## Positional Arguments
- You pass arguments by position (order).
- You must provide them in the correct order.

## Keyword Arguments
- You pass arguments by name (keyword)..
- You can mix with positional arguments (but positional must come first).

## 1) print the input value by using function

```
def input_number():
     return input("enter your number:")
result = input_number()
print(result)
print(type(result))
```
## 2) add two numbers
```
def addition(a,b):
   return  a+b
result = addition(10,20)
print(result)
```
## 3)  Local and global varaiables
```
a = 100
b = 50
def calculation():
      b = 40
      x = a + b
      y = a - b
      z = a * b
      return  x , y ,z
result = calculation()
print(result)
```
## 4)Find even and odd numbers in the give number range
```
def even_odd_number(numbers):
   even_numbers = [ x for x in numbers if x % 2 == 0 ]
   odd_numbers = [ y for y in numbers if y % 2 != 0 ]
   return even_numbers,odd_numbers
number_list = list(range(1,21))
even ,odds = even_odd_number(number_list)
print(even)
print(odds)
```
## 5) calculate the salary for one year
```
def salary_of_employee(months):
   return int(input("enter salry per month:"))*months
total_salary = salary_of_employee(30)
print(total_salary)

```
## 6) multiplication
```
def multiply_values(list):
    multiplied_values = []
    for x in list:
        multiplied_values.append(x*2)
    return multiplied_values
result = multiply_values([10,20,30,40])
print(result)
```
## 7) print the name and house by calling the main function

## Returning Values One by One
```
def main():
    name = get_name()
    house = get_home_name()
    print(f"{name} from {house}")

def get_name():
    return input("Name: ")

def get_home_name():
    return input("House: ")

if __name__ == "__main__":
    main()

```
## Explanation:
- get_name() and get_home_name() return values separately.
- Main function collects them individually.
- Good for beginners, but not scalable when more attributes are added.

## Returning a Tuple
```
def main():
    name, house = get_student()
    print(f"{name} from {house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house   # returns a tuple

if __name__ == "__main__":
    main()
```
## Explanation:
- Function returns two values in a tuple.
- Easy unpacking with name, house = ....
- Cleaner than writing two separate functions.

# Returning a Tuple (Access by Index)
```
def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)

if __name__ == "__main__":
    main()

```
## Explanation
- Still uses a tuple, but values are accessed by index.
- Less readable than unpacking (student[0], student[1]).
- Not recommended if you want clean code.
## Returning a Dictionary
```
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student

if __name__ == "__main__":
    main()

```
## Explanation
- Returns a dictionary.
- Easy to extend if we want more fields (like age, grade).
- Very readable because we use keys (student['name']).

## Returning a Dictionary (Cleaner Version)

```
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return { "name": name, "house": house }

if __name__ == "__main__":
    main()

```
- Same as Example 4, but dictionary is returned directly.
- Clean, short, and widely used in real-world code.