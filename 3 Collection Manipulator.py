# Collection Manipulator

print("Welcome to the Student Data Organizer!!")

students = []
subjects_offered = set()

while True:
    print("\n1. Add Student")
    print("2. Display All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("\nEnter student details:")
        student_id = input("Student ID: ")
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        subjects = input("Subjects (comma-separated): ").split(",")
        subjects = set(sub.strip() for sub in subjects)

        id_dob = (student_id, dob)  # Tuple (immutable)
        student = {
            "id_dob": id_dob,
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects
        }

        students.append(student)
        subjects_offered.update(subjects)
        print("Student added successfully!")

    elif choice == "2":
        if not students:
            print("No student records.")
        else:
            print("\n--- Student Records ---")
            for s in students:
                sid, dob = s["id_dob"]
                print(f"ID: {sid} | Name: {s['name']} | Age: {s['age']} | Grade: {s['grade']} | Subjects: {', '.join(s['subjects'])}")

    elif choice == "3":
        sid = input("Enter Student ID to update: ")
        found = False
        for s in students:
            if s["id_dob"][0] == sid:
                s["age"] = int(input("Enter new age: "))
                new_subjects = input("New subjects (comma-separated): ").split(",")
                s["subjects"] = set(sub.strip() for sub in new_subjects)
                subjects_offered.update(s["subjects"])
                print("Student updated.")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == "4":
        sid = input("Enter Student ID to delete: ")
        for i in range(len(students)):
            if students[i]["id_dob"][0] == sid:
                del students[i]
                print("Student deleted sucessfully.")
                break
        else:
            print("Student not found.")

    elif choice == "5":
        print("\n--- Subjects Offered ---")
        for subject in sorted(subjects_offered):
            print(subject)

    elif choice == "6":
        print("Thank you for using Student Data Organizer!")
        break

    else:
        print("Invalid choice. Try again.")
 
  
