
"""
Student Management System (Python OOP Project)

This is a simple CLI-based Student Management System that allows users to
perform basic CRUD operations like Add, Search, View, Update, and Delete student records.

Features:
- Add student details
- Search student by roll number
- View all students
- Update student information
- Delete student record

Concepts used:
- Object-Oriented Programming
- Lists
- Loops
- Conditional statements
- Functions
- Enumerate
- File Handling
- Exception Handling

Author: Ayushi walia
"""


student_lst = []


class Students:
    def __init__(self ,roll,name,grade,course):
        self.roll = roll
        self.name = name
        self.grade = grade
        self.course = course

    def __str__(self):
       
        return (
        f"Name: {self.name}\n"
        f"Roll: {self.roll}\n"
        f"Grade: {self.grade}\n"
        f"Course: {self.course}"
        )

 # Function to add student details   
def add_student():
    try:
        roll_no= int(input("Enter roll number: "))
    except ValueError:
        print("Invalid input! Enter a number!")
        return  
          
        
    for student in student_lst:
                if student.roll == roll_no:
                    print("STUDENT ALREADY EXIST !")
                    break

    else:
                student = Students(roll_no,
                input("Enter name: ").capitalize(),
                input("Enter grade: ").capitalize(),
                input("Enter course: ").capitalize())
                student_lst.append(student)
                save_data()
                print("STUDENT ADDED SUCCESFULLY !!")


# Function to search student details
def search_student():
    try:
        ent_roll = int(input("Enter the roll_no: "))
    except  ValueError:
         print("Invalid input! Enter a number!")
         return
     
    for student in student_lst:
        if student.roll == ent_roll:
            print()
            print("STUDENT FOUND!")
            print(f"name: {student.name}")
            print(f"roll_no: {student.roll}")
            print(f"grade: {student.grade}")
            print(f"course: {student.course}")
            break
    else:
        print()
        print("STUDENT NOT FOUND!! ")  

# Function to view student details
def view_student():
     
    if student_lst== []:
        print()
        print("NO DATA YET!")
    else:
        print()
        print("ALL STUDENT ")
        for student in student_lst:
            print("--------------")
            print(student)    

# Function to detail student details
def delete_student():
    try:
        roll_no = int(input("Enter roll_no: "))
    except ValueError:
        print("Invalid input! Enter a number!") 
        return   

    if student_lst == []:
        print("DON'T HAVE STUDENT YET!!")
    else:    
        for i,student in enumerate( student_lst):   # enumerate() gives both index and value at the same time in a loop.
            if student.roll == roll_no:
                del student_lst[i]    # we didn't use remove here it will give problem when we wanna delete multiplrstudent at a time nm
                save_data()
                print("STUDENT DELETED!!")
                break

        else:
            print("STUDENT NOT FOUND !!")

# Function to update student details
def update_student():
    try:
        roll_no = int(input("Enter roll number: "))
    except ValueError:
        print("Invalid input! Enter a number!")
        return
    
    for student in student_lst:
        if student.roll == roll_no:
            try:
                change = int(input("what to change (1.name/ 2.grade/ 3.course): "))
            except ValueError:
                print("Invalid input! Enter a number!")
                return
            
            if change  == 1:
                name = input("Enter new name: ")
                student.name = name
                print("student name updated succesfully!")
                save_data()
                break
            elif change  ==2:
                grade = input("Enter new grade: ")
                student.grade = grade
                print("student grade updated succesfully!")
                save_data()
                break
            elif change == 3:
                    course = input("Enter new course: ")
                    student.course = course
                    save_data()
                    print("student course updated succesfully!")
                    break
            else:
                print("invalid choice!")
    else:
            print("student not found!")

def save_data():
    
    
    with open("students.txt","w") as file:
       for student in student_lst:
            file.write(f"{student.roll},{student.name},{student.grade},{student.course}\n")

def load_data():
    try:
        with open("students.txt","r") as file:
            for line in file.readlines():
                data = line.strip().split(",")
                student = Students(int(data[0]),data[1],data[2], data[3])
                student_lst.append(student)
    except FileNotFoundError:
         pass        
    
load_data()

while True:
    print()
    print("---------------------")
    print("1. ADD STUDENT ")
    print("2. SEARCH  STUDENT ")
    print("3. VIEW STUDENT ")
    print("4. DELETE STUDENT")
    print("5. UPDATE STUDENT")
    print("6. EXIT  ")
    print("----------------------")
    print()
    
    try:
        choice  = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Enter a number!")
        continue     
    
    
    
    #add student
    if choice == 1:
        add_student()
       

   #search student
    elif choice == 2:
        search_student()

  #view student
    elif choice == 3:
        view_student()


    # DELETE STUDENT
    elif choice == 4:
        delete_student()

    
    elif choice == 5:
        update_student()
        
    #exit
    elif choice == 6:
        print("Exiting System... Thank you!")
        break

    else:
        print()
        print("INVALID CHOICE!!")

print("\nProgram Ended Successfully.")        






    





