students = {}

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    grades = []
    n = int(input("How many grades? "))
    for i in range(n):
        grade = float(input(f"Enter grade {i+1}: "))
        grades.append(grade)
    info_tuple = (student_id, name)
    students[student_id] = {
        "info": info_tuple,
        "age": age,
        "grades": grades
    }
    print("Student added successfully!\n")

def display_students(source="memory"):
    if not students:
        print("No student data found.\n")
        return
    print(f"\n--- Students ({source}) ---")
    for sid, details in students.items():
        print(f"ID: {details['info'][0]}, Name: {details['info'][1]}, Age: {details['age']}")
        print("Grades:", end=" ")
        for g in details["grades"]:
            print(g, end=" ")
        print("\n")
    print()

def update_student():
    sid = input("Enter Student ID to update: ")
    if sid in students:
        print("What do you want to update?")
        print("1. Name")
        print("2. Age")
        print("3. Grades")
        choice = input("Enter choice: ")

        if choice == "1":
            new_name = input("Enter new name: ")
            students[sid]["info"] = (sid, new_name)
            print("Name updated!\n")
        elif choice == "2":
            new_age = int(input("Enter new age: "))
            students[sid]["age"] = new_age
            print("Age updated!\n")
        elif choice == "3":
            new_grades = []
            n = int(input("How many grades? "))
            for i in range(n):
                grade = float(input(f"Enter grade {i+1}: "))
                new_grades.append(grade)
            students[sid]["grades"] = new_grades
            print("Grades updated!\n")
        else:
            print("Invalid choice!\n")
    else:
        print("Student not found!\n")


def delete_student():
    sid = input("Enter Student ID to delete: ")
    if sid in students:
        del students[sid]
        print("Student deleted!\n")
    else:
        print("Student not found!\n")

def save_to_file(filename="students.txt"):
    with open(filename, "w") as file:
        for sid, details in students.items():
            row = [sid, details["info"][1], str(details["age"])] + [str(g) for g in details["grades"]]
            file.write(",".join(row) + "\n")
    print("Data saved to file.\n")

def load_from_file(filename="students.txt"):
    try:
        with open(filename, "r") as file:
            for line in file:
                row = line.strip().split(",")
                sid, name, age, *grades = row
                students[sid] = {
                    "info": (sid, name),
                    "age": int(age),
                    "grades": [float(g) for g in grades]
                }
        print("Data loaded from file.\n")
    except FileNotFoundError:
        print("File not found.\n")

average = lambda grades: sum(grades)/len(grades) if grades else 0

while True:
    print("===== Student Information System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Save to File")
    print("6. Load from File")
    print("7. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        save_to_file()
    elif choice == "6":
        load_from_file()
    elif choice == "7":
        print("Exiting program... Goodbye!")
        break
    else:
        print("Invalid choice, try again!\n")
        continue
