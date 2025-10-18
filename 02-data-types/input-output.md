##  Getting User Input Using input()
```
name = input("What is your name? ")
print("Hello " + name)

```
## Convert Data Types
```
birth_year = input("Enter your birth year: ")
age = 2025 - int(birth_year)
print("Your age is:", age)
```
## Add Two Float Numbers from User Input
```
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
sum_result = first_number + second_number
print("Sum result is: " + str(sum_result))
#Note: input function always return string