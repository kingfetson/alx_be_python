class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Student Age: {self.age}")


# Example usage (optional for testing)
if __name__ == "__main__":
    student1 = Student("Alice", 16)
    student2 = Student("John", 20)
    student1.display_info()
    student2.display_info()
