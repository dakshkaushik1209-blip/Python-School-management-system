import json
from abc import ABC,abstractmethod
from pathlib import Path

database="database.json"
#Temporary data
data={"Student" : [],"Teacher" : []}

if Path(database).exists():
    with open(database,"r") as f:
        content=f.read()
        if content:
            data=json.loads(content)
    
def save():
    with open(database,"w") as f:
        json.dump(data,f,indent=4)

class Person(ABC):
    @abstractmethod
    def get_roles(self):
        pass
    
    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def show_details(self):
        pass

    @staticmethod           #it does not depend on class or object
    def validate_email(email):
        if "@" in email and "." in email:
            return True
        else:
            return False
    

class Student(Person):
    def get_roles(self):
        return "Student"

    def register(self):
        name=input("Enter name:- ")
        age=int(input("Enter age:- "))
        email=input("Enter mail:- ")
        roll_no=int(input("Enter roll number:- "))
        
        if not Person.validate_email(email):
           print("Invalid email") 
           return

        for i in data['Student']:
            if i['roll_no'] == roll_no:
                print("Student already exists ")
                return                          #return ke 2 kaam hote hai ek to vo chiz return karta hai or ek function ko rok deta hai.yaha rok rha hai 

        data["Student"].append({
            "name":name,
            "age":age,
            "email":email,
            "roll_no":roll_no,
            "Grade":{}
            })

        save()
        print(f"Student {name} registered successfully")

    def add_grade(self):
        roll_no=int(input("Enter your roll number:- "))
        subject=input("Enter subject:- ")
        marks=float(input("Enter marks:- "))

        for i in data['Student']:
            if i['roll_no']==roll_no:
                i['Grade'][subject]= marks
                save()
                print(f"Marks added succesfully")
                return
        else:
            print("Student not found")
    
    def show_details(self):
        roll_no=int(input("Enter roll number:- "))
        for i in data['Student']:
            if i['roll_no']==roll_no:
                print(f"Name = {i['name']}")
                print(f"Roll number = {roll_no}")
                grades=i["Grade"]
                if grades:
                    print(f"Percentage={sum(grades.values())/len(grades)}%")
                else:
                    print("Percentage = 0")
                print(f"Grades = {i['Grade']}")
                print(f"Age = {i['age']}")    
                print(f"Email = {i['email']}")
                return
        else:
            print("Student not found")
student=Student()

class Teacher(Person):
    def get_roles(self):
        return "Teacher"
    
    def register(self):
        name=input("Enter name:- ")
        age=int(input("Enter age:- "))
        email=input("Enter email:- ")
        Subject=input("Enter subject:- ")
        Employe_id=int(input("Enter your id:- "))

        if not Person.validate_email(email):
            print("Invalid email")
            return

        for i in data['Teacher']:
            if i['Employe_id']==Employe_id:
                print("Teacher already exists")
                return
        
        data["Teacher"].append({
            "name":name,
            "age":age,
            "email":email,
            "Subject":Subject,
            "Employe_id":Employe_id
        })
        save()
        print(f"Teacher {name} registered succesfully")
    def show_details(self):
        Employe_id=int(input("Enter Employe id:- "))
        for i in data['Teacher']:
            if i['Employe_id']==Employe_id:
                print(f"Name = {i['name']}")
                print(f"Employe id = {Employe_id}")
                print(f"Age = {i['age']}")    
                print(f"Email = {i['email']}")    
                print(f"Subject = {i['Subject']}")
                return
        else:
            print("Teacher not found")

teacher=Teacher()

print("Press 1 to register a student")
print("Press 2 to register a teacher")
print("Press 3 to add grades")
print("Press 4 to show a student details")
print("Press 5 to show a teacher details")

choice= int (input("Enter your choice:- "))

if choice==1:
    student.register()

elif choice==2:
    teacher.register()

elif choice==3:
    student.add_grade()

elif choice ==4:
    student.show_details()

elif choice ==5:
    teacher.show_details()

else:
    print("Invalid choice")