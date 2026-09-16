
# PROJECT: COLLECTION MANIPULATOR
# Student Data Organizer


student_records = []          
student_data = {}             
subjects_offered = set()    

# WELCOME 

print("=" * 55)
print("          WELCOME TO THE STUDENT DATA ORGANIZER")
print("=" * 55)

# ADD STUDENT FUNCTION


def add_student():
    print("\n--- Add Student ---")

    # Type Casting 
    student_id = int(input("Student ID: "))

    if student_id in student_data:
        print("Student ID already exists!")
        return

    name = input("Name: ")
    age = int(input("Age: "))                   
    grade = input("Grade: ")
    dob = input("Date of Birth: ")
    subject_input = input("Subjects: ")

    # converet
    subject_list = [sub.strip().title()for sub in subject_input.split(",")]


    # Add subjects 
    for sub in subject_list:
        subjects_offered.add(sub)

    # Tuple 
    student_tuple = (student_id, dob)

    

    # Dictionary 
    student = {
        "id_info": student_tuple,     
        "name": name,
        "age": age,
        "grade": grade,
        "subjects": subject_list   
    }

    # List 
    student_records.append(student)

    # Dictionary with student
    student_data[student_id] = student

    print("\nStudent added successfully!")

# DISPLAY ALL STUDENTS


def display_students():
    print("\n--- Display All Students ---")

    if len(student_records) == 0:
        print("No student records found.")
        return

    for student in student_records:
        sid = student["id_info"][0]
        dob = student["id_info"][1]
        name = student["name"]
        age = student["age"]
        grade = student["grade"]
        subjects = ", ".join(student["subjects"])

        # 1. f-string formatting
        print(f"Student ID: {sid} | Name: {name} | Age: {age} | Grade: {grade} | DOB: {dob} | Subjects: {subjects}")

        # 2. .format() method
        print("Name: {} | Age: {}".format(name, age))

        # 3. % formatting
        print("Grade: %s | Subjects: %s" % (grade, subjects))

    

# UPDATE STUDENT 


def update_student():
    print("\n--- Update Student Information ---")

    student_id = int(input("Enter Student ID: "))

    if student_id not in student_data:
        print("Student not found!")
        return

    student = student_data[student_id]

    print("\nWhat do you want to update?")
    print("1. Name")
    print("2. Subjects")
    print("3. Age")
    print("4. Grade")

    choice = input("Enter choice: ")

    if choice == "1":
        new_name = input("Enter new name: ")
        student["name"] = new_name
        print("Name update successfully!")

    elif choice == "2":
        new_subject = input("Enter new subject:")
        subject_list = [sub.strip().title()for sub in new_subject.split(",")]
        student["subjects"] = subject_list

        for sub in subject_list:
            subjects_offered.add(sub)
            
        print("subject update successfully!")
    
            
        
    elif choice == "3":
        new_age = int(input("Enter new age:"))
        student["age"] = new_age
        print("age update successfully!")

    elif choice == "4":
        new_grade = input("Enter new grade:")
        student["grade"] = new_grade
        print("grade update successfully!")
    

    else:
        print("Invalid choice!")

# DELETE STUDENT 

def delete_student():
    print("\n--- Delete Student ---")

    student_id = int(input("Enter Student ID: "))

    if student_id not in student_data:
        print("Student not found!")
        return

    
    for i in range(len(student_records)):
        if student_records[i]["id_info"][0] == student_id:
            del student_records[i]
            break

    
    del student_data[student_id]

    print("Student deleted successfully using del keyword!")

# DISPLAY SUBJECTS 

def display_subjects():
    print("\n--- Subjects Offered (Unique) ---")

    if len(subjects_offered) == 0:
        print("No subjects available.")
        return

    print("Unique subjects offered by students:")
    for subject in sorted(subjects_offered):
        print("•", subject)

# MAIN MENU


while True:
    print("\n" + "=" * 65)
    print("Select an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

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
        display_subjects()
    elif choice == "6":
        print("\nThank you for using the Student Data Organizer!")
        print("Program exited successfully.")
        break
    else:
        print("Invalid choice! Please select between 1 to 6.")
