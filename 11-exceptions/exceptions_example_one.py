# Custom Exception Class
class InvalidMarksError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Function to check marks
def check_marks(marks):
    if marks < 0 or marks > 100:
        raise InvalidMarksError(f"Invalid marks: {marks}. Marks should be between 0 and 100.")
    else:
        print(f"Marks are valid: {marks}")

# Test the function
try:
    check_marks(120)  # This will raise an exception
except InvalidMarksError as e:
    print("Error:", e)

