
## 1 how to define the class
```
class Student:
      ...

def main():
    student = get_student()
    print(f"{student.name} form {student.house}")
    
def get_student():
    student  = Student()
    student.name = input("name:")
    student.house = input("house")
    return student
  
if __name__ == "__main__":
    main()
```
## 2 initilating the init constrcuter
```
class Student:
    def __init__(self,name,house):
        self.my_name = name
        self.my_house = house


def main():
    student = get_student()
    print(f"{student.my_name} form {student.my_house}")
    
def get_student():
    
   name = input("name:")
   house = input("house")
   student = Student(name,house)
   return student
  
if __name__ == "__main__":
    main()
```
## 3 initilating the init and str constrcuter
```
class Student:
    def __init__(self,name,house):
        self.name = name
        self.house = house
    def __str__(self):
        return f"{self.name} form {self.house}"


def main():
    student = get_student()
    print(student)
    
    
def get_student():
    
   name = input("name:")
   house = input("house")
   student = Student(name,house)
   return student
  
if __name__ == "__main__":
    main()
```
## 4 initilating the init and str constrcuter and case function
```
class Student:
    def __init__(self,name,house,street):
        self.name = name
        self.house = house
        self.street = street
    def __str__(self):
        return f"{self.name} form {self.house}"
    def streetname(self):
        match self.street:
            case "ram":
               return "ram street"
            case "arjun":
                return "Arjun Street"
            case "abhay":
                return "Abhay Street"


def main():
    student = get_student()
    print(student)
    print(student.streetname())
    
    
def get_student():
    
   name = input("name: ")
   house = input("house: ")
   street = input("street: ")
   student = Student(name,house,street)
   return student
  
if __name__ == "__main__":
    main()
```