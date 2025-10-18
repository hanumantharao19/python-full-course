class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    students = get_students()
    print("\n--- Student List ---")
    for student in students:
        print(student)


def get_students():
    students = []
    count = int(input("How many students do you want to add? "))
    for x in range(count):
        name = input("Name: ").strip()
        house = input("House: ").strip()
        student = Student(name, house)
        students.append(student)
    return students


if __name__ == "__main__":
    main()
