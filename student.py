import json
import os
import re


DATA_FILE = "data/students.json"
COURSES = ["BCA", "BBA", "B.Tech", "MBA", "MCA"]


def ensure_data_file():
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)


def load_students():
    ensure_data_file()
    with open(DATA_FILE, 'r') as f:
        return json.load(f)


def save_students(students):
    with open(DATA_FILE, 'w') as f:
        json.dump(students, f, indent=4)


def is_valid_name(name):
    return len(name) >= 2 and name.isalpha()

def is_valid_reg_number(reg):
    return re.match(r'^REG-\d{4}-\d{4}$', reg)

def is_valid_age(age):
    return age.isdigit() and 18 <= int(age) <= 25

def is_valid_email(email):
    return re.match(r'^[a-z0-9\.-]+@[a-z0-9\.-]+\.[a-z]+$', email)

def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

def is_valid_course(course):
    return course in COURSES


def register_student():
    print("\n Register Student ")

    name = input("Name: ")
    if not is_valid_name(name):
        print(" Invalid name.")
        return

    reg = input("Registration Number (REG-YYYY-NNNN): ")
    if not is_valid_reg_number(reg):
        print(" Invalid registration number.")
        return

    age = input("Age: ")
    if not is_valid_age(age):
        print(" Age must be between 18 and 25.")
        return

    email = input("Email: ")
    if not is_valid_email(email):
        print(" Invalid email.")
        return

    phone = input("Phone (10 digits): ")
    if not is_valid_phone(phone):
        print(" Invalid phone number.")
        return

    print("Available Courses:", ", ".join(COURSES))
    course = input("Course: ")
    if not is_valid_course(course):
        print("Invalid course.")
        return

    student = {
        "Name": name,
        "Reg No": reg,
        "Age": int(age),
        "Email": email,
        "Phone": phone,
        "Course": course
    }

    students = load_students()
    students.append(student)
    save_students(students)
    print(" Student registered successfully.\n")


def list_students():
    print("\n Student List ")
    students = load_students()
    
    if not students:
        print(" No students found.")
        return

    for i, s in enumerate(students, start=1):
        print(f"{i}. {s['Name']} | {s['Reg No']} | Age: {s['Age']} | "
              f"{s['Email']} | {s['Phone']} | {s['Course']}")

