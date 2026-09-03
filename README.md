# py_project.3----Collection-Manipulator

 
 PROJECT : COLLECTION MANIPULATOR


 
 
CREAT BY : AYUSH JIVANI




PYTHON LANGUAGE 



A Python-based command-line application designed to manage student records effectively using core Python concepts including custom data structures (Lists, Tuples, Sets, and Dictionaries), string formatting, type casting, and mutability control.
---

📌 Project Overview & Objectives

Project Title: Collection Manipulator

Objective: Create a Python program that manages a collection of student records using intermediate Python concepts:
String Formatting & Manipulation: `f-strings`, `.format()`, `%` formatting.

Collection Data Types:
`List`: To store the master list of all student records.
`Tuple`: To store immutable unique data for each student (`Student ID`, `Date of Birth`).
`Set`: To store and display unique subjects offered across all students (ensuring zero duplicates).
`Dictionary`: To store dynamic details (`Name`, `Age`, `Grade`, `Subjects`) keyed by `Student ID`.
Mutability vs Immutability: Demonstrating mutable operations on lists/dictionaries and enforcing immutable student identifiers via tuples.
Type Casting & Data Operations: Safe type conversions for integer inputs and record deletion using the `del` keyword.
---
🔗 Quick Links & Resources
📁 GitHub Repository: 

📹 Demo Video / Explanation: 

---
✨ Key Features & Requirements

Welcome & Interactive Menu: Clean console UI with clear options for student management.
Add Student Record:
Captures Student ID, Name, Age, Grade, DOB (YYYY-MM-DD), and Subjects (comma-separated).
Stores ID & DOB as an immutable Tuple.
Cleans and stores subjects into a Set.
Packages record into a Dictionary and appends to the main student List.
Display All Students:
Formatted table/list using multiple Python string formatting methods (`f-strings`, `.format()`).
Update Student Information:
Allows modifying mutable properties such as Age, Grade, or Subjects while keeping immutable data safe.
Delete Student Record:
Utilizes the `del` keyword to remove student entries by ID from the main records collection.
Display Unique Subjects Offered:
Aggregates all subjects across all students into a master Set to automatically remove duplicates.
---
🖥️ Program Flow & Usage Example
```text
========================================
 Welcome to the Student Data Organizer!
=======================================

Select an option:
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit

Enter your choice: 1

Enter student details:
Student ID: 101
Name: Alice
Age: 20
Grade: B+
Date of Birth (YYYY-MM-DD): 2002-05-14
Subjects (comma-separated): Math, Science, English

✓ Student added successfully!

--- Display All Students ---
ID: 101 | Name: Alice | Age: 20 | Grade: B+ | Subjects: Math, Science, English
```
---
🚀 How to Run the Project
Clone the Repository:
```bash
   git clone https://github.com/your-username/your-repository-name.git
   cd your-repository-name
   ```
Run the Application:
```bash
   python main.py
   ```
---
📝 Assumptions & Notes
Unique IDs: Each student is assumed to have a unique integer Student ID.
Date Format: Dates of birth are entered in `YYYY-MM-DD` format and stored in a tuple along with the Student ID to prevent unintended modification.
Plagiarism Disclaimer: This project is original work created strictly adhering to academic integrity standards.
---
Shaping skills for scaling higher...!!!
