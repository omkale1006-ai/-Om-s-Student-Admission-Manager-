import random

# Program to save the student info

class Student:
    roll_counter = 1  # starting roll number
    def __init__(self, name, mother, phone, email):
        self.name = name
        self.mother = mother
        self.phone = phone
        self.email = email
        Student. roll_counter += 1  
        self.roll = Student.roll_counter
    def show(self):
        print(f"\n🎓 {self.name}, Welcome to Om's School!")
        print(f"👩 Mother's Name: {self.mother}")
        print(f"📞 Phone: {self.phone}")
        print(f"📧 Email: {self.email}")
        print(f"🆔 Roll Number: {self.roll}")

        with open("student.txt", "a", encoding="utf-8") as f:
            f.write(f"\n🎓 Name:  {self.name}\n")
            f.write(f"👩 Mother's Name: {self.mother}\n")
            f.write(f"📞 Phone: {self.phone}\n")
            f.write(f"📧 Email: {self.email}\n")
            f.write(f"🆔 Roll Number: {self.roll}\n")
            f.write("-" * 40 + "\n")   # separator line


while True:
    print("\n--- Welcome to Om's School ---")
    name = input("Enter your child name: ").title()
    mother = input("Enter the mother name: ").title()

    # Phone number check
    while True:
        phone = input("Enter your phone number: ")
        if len(phone) != 10 or not phone.isdigit():
            print("❌ Please enter a correct 10-digit phone number.")
        else:
            break

    # Email check
    while True:
        email = input("Enter the Email Id: ")
        if not email.endswith("@gmail.com"):
            print("❌ Please enter a valid Gmail ID.")
        else:
            break

    # Create student object
    student = Student(name, mother, phone, email)
    student.show()
