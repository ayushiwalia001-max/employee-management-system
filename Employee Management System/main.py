import mysql.connector as sql 
from dotenv import load_dotenv
import os

load_dotenv()

 # THIS IS CONNECTION

conn = sql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

# EXECUTE SQL QUERY
cursor = conn.cursor()

if conn.is_connected():
    print("Connected to MySQL successfully!! ")



def add_employee():
    email_id = input("Enter employee email id: ").strip().lower()
    if email_id.count('@')!=1  or " " in email_id or "@gmail.com" not in email_id:
        print("please enter a valid email_id!!")
        return
    
    query  ="""  
        SELECT  * FROM EMPLOYEE 
        WHERE EMAIL_ID = %s
        """
    values = (email_id,)
    cursor.execute(query,values)
    employee = cursor.fetchone()
    if employee is None:
    
        query = """ 
                INSERT INTO EMPLOYEE (
                NAME, AGE, DEPARTMENT, DESIGNATION,
                SALARY, PHONE_NO, EMAIL_ID, JOINING_DATE, REMARK
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
        try:
            name = input("Enter name: ").strip().capitalize()
            age = int(input("Enter age: "))
            if age < 18:
                print("Employee age must be 18 or above!")
                return
            
            department = input("Enter department: ").strip().upper()
            designation = input("Enter designation: ").strip().title()
            salary = float(input("Enter salary: "))
            if salary <= 0:
                print("Salary must be greater than 0!")
                return
            
            phone = input("Enter phone number: ").strip()
            if not phone.isdigit() or len(phone)!=10 or phone[0] not in "6789":
                print("Please enter a valid phone number!!")
                return
            
            email = email_id
            joining_date = input("Enter joining date (YYYY-MM-DD): ").strip()
            remark = input("Enter remark: ").strip().capitalize()

            values = (name, age, department, designation, salary, phone, email, joining_date, remark)
            
            cursor.execute(query,values)
            conn.commit()
            print("Employee added successfully!!")

        except ValueError:
            print(" Invalid input !Please enter valid age / salary!") 
            return   
        except Exception as e:
            print("Something went wrong!!")
            print(e)
            return
     
    else:
        print("Employee already exists!!")


def view_employee(): 
    query = """ SELECT * FROM Employee """
    cursor.execute(query)
    data = cursor.fetchall()
    if data ==[]:
        print("No employees found in database!!")
    else:
        print("ALL EMPLOYEES!!")
        for employee in data :
            
            print("------------------------")
            print(f"EMP_ID : {employee[0]}") # id
            print(f"NAME : {employee[1]}") # name
            print(f"AGE : {employee[2]}")
            print(f"DEPARTMENT : {employee[3]}") # department
            print(f"DESIGNATION : {employee[4]}") # designation
            print(f"SALARY : {employee[5]}") # salary
            print(f"PHONE : {employee[6]}") # phone
            print(f"EMAIL : {employee[7]}") # email
            print(f"JOINING DATE : {employee[8]}") #joining date 
            print(f"REMARK : {employee[9]}") # remark
            print("------------------------")
                
def search_employee():
    try:
        search = int(input("Enter employee id: "))
        query = """
        SELECT * FROM EMPLOYEE 
        WHERE EMP_ID = %s
        """
        value = (search,)  # mysql expect values as tuple
        cursor.execute(query,value)
        employee_detail = cursor.fetchone()

        if employee_detail is None:
            print()
            print("No employee found with this ID.")
        else:
            print()
            print("EMPLOYEE FOUND!!")
            print(f"EMP_ID : {employee_detail[0]}")
            print(f"NAME : {employee_detail[1]}")
            print(f"AGE: {employee_detail[2]}")
            print(f"DEPARTMENT : {employee_detail[3]}")
            print(f"DESIGNATION : {employee_detail[4]}")
            print(f"SALARY : {employee_detail[5]}")
            print(f"PHONE: {employee_detail[6]}")
            print(f"EMAIL: {employee_detail[7]}")
            print(f"JOINING DATE : {employee_detail[8]}")
            print(f"REMARK: {employee_detail[9]}")

    except ValueError:
        print()
        print("Please enter a valid employee id!")  
        return      
    except Exception as e:
        print("Something went wrong!")
        print(e)
        return
                
          

def update_employee():
   columns = {
        1: "NAME",
        2: "AGE",
        3: "DEPARTMENT",
        4: "DESIGNATION",
        5: "SALARY",
        6: "PHONE_NO",
        7: "EMAIL_ID",
        8: "JOINING_DATE",
        9: "REMARK"
    }
   try:
        change = int(input("What to update?\n1. NAME\n2. AGE\n3. DEPARTMENT\n4. DESIGNATION\n5. SALARY\n6. PHONE\n7. EMAIL\n8. JOINING DATE\n9. REMARK\n>>>" ))
        emp_id = int(input("Enter Employee ID you want to update: "))
            
        if change in columns:
                column = columns[change]

                query = f""" 
                    UPDATE EMPLOYEE
                    SET {column} = %s
                    WHERE EMP_ID = %s
                    """    
            
                
                if change == 1:
                
                    new_name = input("Enter new name: ").strip().capitalize()
                    values = (new_name,emp_id)

                    cursor.execute(query,values)
                
                

                elif change == 2:  
                
                    new_age = int(input("Enter new age: "))
                    if new_age < 18:
                        print("Employee age must be 18 or above!")
                        return
                    values = (new_age,emp_id)

                    cursor.execute(query,values)
                
                
                

                elif change ==3:
                
                    new_dep = input("ENter new department : ").strip().upper()
                    values = (new_dep,emp_id)

                    cursor.execute(query,values)
                    

                elif change ==4:
                
                    new_des = input("Enter new designation : ").strip().title()
                    values = (new_des,emp_id)

                    cursor.execute(query,values)
                

                elif change ==5:
                
                    new_salary = float(input("Enter new salary : "))
                    if new_salary <= 0:
                        print("Salary must be greater than 0!")
                        return
                    values = (new_salary,emp_id)

                    cursor.execute(query,values)
                

                elif change ==6:
                
                    new_num = input("Enter new number : ").strip()
                    if not new_num.isdigit() or len(new_num)!=10 or new_num[0] not in "6789":
                        print("Please enter a valid phone number!!")
                        return
                    values= (new_num, emp_id)

                    cursor.execute(query,values)
                
                
                elif change ==7:
                
                    new_email = input("Enter new email : ").strip().lower()
                    if new_email.count('@')!=1  or " " in new_email or "@gmail.com" not in new_email:
                        print("please enter a valid email!!")
                        return
                    values = (new_email,emp_id)

                    cursor.execute(query,values)
                

                elif change ==8:
                    new_joindate =input("Enter  new joining date (YYYY-MM-DD): ").strip()
                    values = (new_joindate,emp_id)

                    cursor.execute(query,values)
                

                elif change == 9:
                
                    new_remark = input("Enter new remark : ").strip().capitalize()
                    values = (new_remark,emp_id)

                    cursor.execute(query,values)
                    
                
                
                if cursor.rowcount == 0:  # check row affected or not
                    print("Employee not found with this ID!!")
                else:
                    conn.commit()
                    print(f"Employee {column}  updated successfully !!")     
        else:
                print("Invalid change!!")
                return
   except ValueError:
       print("Please enter a valid change or emp_id !!" )
       return
   except Exception as e:
       print("Something went wrong!!")
       print(e)
       return

def delete_employee():
    try:
        emp_id = int(input("Enter  employee id you want to delete: "))
        query = """ 
            DELETE FROM EMPLOYEE 
            WHERE EMP_ID = %s
            """
        values = (emp_id,)
        cursor.execute(query,values)
    

        if cursor.rowcount == 0:
            print("Employee Not Found!!")
        else:
            conn.commit()
            print("Employee Deleted successfully!!")

    except ValueError:
        print("please enter a valid employee ID !!")   
        return
    except Exception as e:
        print("Something went wrong!!") 
        print(e)    
        return 


while True:
    print("""
================================
    EMPLOYEE MANAGEMENT SYSTEM
================================

1. Add Employee
2. View All Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Exit

================================
""")
    try:
        choice = int(input("Enter choice: "))


        if choice == 1:
            add_employee()

        elif choice == 2:
            view_employee()

        elif choice ==3:
            search_employee()
        

        elif choice == 4:
            update_employee()
        
        
        elif choice == 5:
            delete_employee()
        
        elif choice == 6:
            break

        else:
            print("INVALID CHOICE!!")
    except ValueError:
        print("Please enter a valid numeric value!! ")


cursor.close()
conn.close()
print("Database connection closed. Goodbye!")
 

        