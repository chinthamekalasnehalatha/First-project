# In this program I am using global variables
import csv
student_fields = ['name', 'age', 'email', 'phone']
student_database = 'students.csv'
def display_menu():
    print(" Welcome to Student Management System")
    print("1. Add New Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Quit")
def add_student():
    global student_fields
    global student_database
    student_data = []
    for field in student_fields:
        value = input("Enter " + field + ": ")
        student_data.append(value)
 
    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])
 
    print("Data saved successfully")
    input("Press any key to continue")
    return
​
def view_students():
    global student_fields
    global student_database
 
    print("--- Student Records ---")
 
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")
 
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
 
    input("Press any key to continue")
def delete_student():
    global student_fields
    global student_database
 
    print("--- Delete Student ---")
    name = input("Enter name. to delete: ")
    student_found = False
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if name!= row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True
 
    if student_found is True:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("student_name. ", name, "deleted successfully")
    else:
        print("student_name. not found in our database")
 
    input("Press any key to continue")
while True:
    display_menu()
 
    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        delete_student()
    else:
        break
