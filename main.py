from auth import login
from student import register_student, list_students

def main_menu():
    while True:
        print("\n SCHOOL MANAGEMENT SYSTEM")
        print("1. Register Student" ,"2. List Students", "3. Exit " ,sep="\n")
        choice = input("Enter choice: ")
        if choice == '1':
            register_student()
        elif choice == '2':
            list_students()
        elif choice == '3':
            
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    print("Admin Login Required")
    if login():
        main_menu()
