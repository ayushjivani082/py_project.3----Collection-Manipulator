# =====================WELCOME===============================
# Student Data Organizer
# Collection Manipulator Project
# Creat By : Ayush jivani
# ==============================================================

# LIST - stores all student records
student_records = []

# DICTIONARY - keys are Student IDs
students = {}

# SET - stores unique subjects
subjects_offered = set()


def line():
    print("=" * 65)


def is_valid_dob(dob):
    """Check if Date of Birth is in YYYY-MM-DD format"""
    if len(dob) != 10:
        return False
    if dob[4] != "-" or dob[7] != "-":
        return False

    year = dob[0:4]
    month = dob[5:7]
    day = dob[8:10]

    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False

    year = int(year)
    month = int(month)
    day = int(day)

    if year < 1980 or year > 2020:
        return False
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False

    return True


def add_student():
    print("\n--- Add Student ---")

    # Type Casting
    try:
        student_id = int(input("Student ID: "))
    except ValueError:
        print("Invalid Student ID! Please enter a number.")
        return

    if student_id in students:
        print("Student ID already exists!")
        return

    # Name with empty check + lower() + title()
    name = input("Name: ").strip()
    if name == "":
        print("Name cannot be empty!")
        return
    name = name.lower().title()          # lower() used here

    try:
        age = int(input("Age: "))
        if age < 1 or age > 120:
            print("Age should be between 1 and 120.")
            return
    except ValueError:
        print("Invalid age!")
        return

    grade = input("Grade: ").strip().upper()
    if grade == "":
        print("Grade cannot be empty!")
        return

    # Date of Birth validation
    dob = input("Date of Birth (YYYY-MM-DD): ").strip()
    if not is_valid_dob(dob):
        print("Invalid Date of Birth! Please use format YYYY-MM-DD")
        return

    subjects_input = input("Subjects (comma-separated): ").strip()
    subject_list = [s.strip().title() for s in subjects_input.split(",") if s.strip()]
    subject_list = list(dict.fromkeys(subject_list))

    if not subject_list:
        print("Please enter at least one subject.")
        return

    # TUPLE - immutable (Student ID + DOB)
    identity = (student_id, dob)

    student_data = {
        "identity": identity,
        "name": name,
        "age": age,
        "grade": grade,
        "subjects": subject_list
    }

    # Add to LIST
    student_records.append(student_data)

    # Add to DICTIONARY
    students[student_id] = student_data

    # Add to SET
    subjects_offered.update(subject_list)

    print("\nStudent added successfully!")

    # All three string formatting methods
    print(f"Student ID: {student_id} | Name: {name}")                    # f-string
    print("Age: {} | Grade: {}".format(age, grade))                      # .format()
    print("Date of Birth: %s" % dob)                                     # % formatting


def display_all_students():
    print("\n--- Display All Students ---")

    if not student_records:
        print("No student records available.")
        return

    for record in student_records:
        student_id, dob = record["identity"]
        subjects = ", ".join(record["subjects"])

        print(f"Student ID: {student_id} | Name: {record['name']} | Age: {record['age']} | Grade: {record['grade']} | Subjects: {subjects}")
        print("Date of Birth: %s" % dob)
        print("-" * 65)


def update_student():
    print("\n--- Update Student Information ---")

    try:
        student_id = int(input("Enter Student ID: "))
    except ValueError:
        print("Invalid ID!")
        return

    if student_id not in students:
        print("Student not found!")
        return

    student = students[student_id]

    print("\nStudent found!")
    print("Note: Student ID and Date of Birth cannot be changed (Tuple)")

    print("\n1. Update Name")
    print("2. Update Age")
    print("3. Update Grade")
    print("4. Update Subjects")
    print("5. Back")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        new_name = input("Enter New Name: ").strip()
        if new_name == "":
            print("Name cannot be empty!")
            return
        student["name"] = new_name.lower().title()     # lower() used
        print("Name updated successfully!")

    elif choice == "2":
        try:
            new_age = int(input("Enter New Age: "))
            if 1 <= new_age <= 120:
                student["age"] = new_age
                print("Age updated successfully!")
            else:
                print("Age should be between 1 and 120.")
        except ValueError:
            print("Invalid age!")

    elif choice == "3":
        new_grade = input("Enter New Grade: ").strip().upper()
        if new_grade == "":
            print("Grade cannot be empty!")
            return
        student["grade"] = new_grade
        print("Grade updated successfully!")

    elif choice == "4":
        subjects_input = input("Enter Subjects (comma-separated): ").strip()
        new_subjects = [s.strip().title() for s in subjects_input.split(",") if s.strip()]
        new_subjects = list(dict.fromkeys(new_subjects))

        if not new_subjects:
            print("Please enter at least one subject.")
            return

        student["subjects"].clear()
        student["subjects"].extend(new_subjects)

        # Rebuild SET
        subjects_offered.clear()
        for record in student_records:
            subjects_offered.update(record["subjects"])

        print("Subjects updated successfully!")

    elif choice == "5":
        return
    else:
        print("Invalid choice!")


def delete_student():
    print("\n--- Delete Student ---")

    try:
        student_id = int(input("Enter Student ID: "))
    except ValueError:
        print("Invalid ID!")
        return

    if student_id not in students:
        print("Student not found!")
        return

    # Remove from LIST using del
    for i, record in enumerate(student_records):
        if record["identity"][0] == student_id:
            del student_records[i]
            break

    # Remove from DICTIONARY using del
    del students[student_id]

    # Rebuild SET
    subjects_offered.clear()
    for record in student_records:
        subjects_offered.update(record["subjects"])

    print(f"Student ID {student_id} deleted successfully!")


def display_subjects():
    print("\n--- Subjects Offered ---")

    if not subjects_offered:
        print("No subjects available.")
        return

    print("Total Unique Subjects: {}".format(len(subjects_offered)))
    print()

    for i, subject in enumerate(sorted(subjects_offered), 1):
        print("%d. %s" % (i, subject))

    print("\nNote: Duplicate subjects are automatically removed using Set.")


def main():
    print()
    line()
    print("Welcome to the Student Data Organizer!".center(65))
    line()
    print("This program uses List, Tuple, Set and Dictionary")
    print("to manage student records.")
    print()

    while True:
        print("\nSelect an option:")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Update Student Information")
        print("4. Delete Student")
        print("5. Display Subjects Offered")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            display_all_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            display_subjects()
        elif choice == "6":
            print("\nThank you for using the Student Data Organizer!")
            print("Program exited successfully.")
           
            break
        else:
            print("Invalid choice! Please select from 1 to 6.")


if __name__ == "__main__":
    main()
