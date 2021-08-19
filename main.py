import sqlite3

connection = sqlite3.connect('manage.db')
cursor = connection.cursor()

def displayEmp():
    cursor.execute("SELECT * FROM employees")
    print("{:<5} {:<15} {:<15}".format("ID","Full Name","Age", "Dept ID"))
    print("{:<5} {:<15} {:<15}".format("---","---------","---","------"))
    for record in cursor.fetchall():
        print("{:<5} {:<15} {:<15}".format(record[0],record[1],record[2],record[3))

def addEmp():
    empName = input("Please enter the employee's full name: ")
    empAge = input("Please enter the employee's age: ")
    empDeptId = input("Please enter the employee's department: ")                                                                           
    values = (empName, empAge,empDeptId)
    cursor.execute("INSERT INTO employees (name, age, deptID) VALUES (?,?,?)", values)
    connection.commit()
    print("")
    print("Updated list:")
    displayEmp()
                                                                                
def editEmp():
    print("")
    displayEmp()
    empID = input("Please enter the ID of employee whose name needs to be changed: ")
    empName = input("Please input the new name: ")
    values = (empName, empID)
    cursor.execute("UPDATE employees SET name = ? WHERE id = ?", values)
    connection.commit()

def chooseEditEmp():
    print("1) Edit Employee Name")
    print("2) Cancel and Quit")
    editType = input("> ")
    if editType == "1":
        editEmp()
    elif editType == "2":
        print("")
        return

def delEmp():
    print("")
    displayEmp()
    empID = input("Please enter the ID of the departing employee: ")
    values = (empID,)
    cursor.execute("DELETE FROM employees WHERE id = ?", values)
    connection.commit()

userSelect = "1"
while userSelect != "9":
    print("What would you like to do?")
    print("1) Add a New Employee")
    print("3) Edit an Existing Employee")
    print("5) Display All Employees")
    print("7) Remove an Employee")
    print("9) Quit")
    print("")
    userSelect = input("> ")
    print("")
    if userSelect == "1":
        addEmp()
        print("")
    elif userSelect == "3":
        editEmp()
        print("")
    elif userSelect == "5":
        displayEmp()
        print("")
    elif userSelect == "7":
        deleteEmp()
        print("")                                                                      

connection.close()
