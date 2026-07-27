
class student():
    age = 19
    college = "Yes"
    job = "No"
    def get_info(self):
        print("Name: ",self.name)
        print("age: ",self.age)
        print("college: ",self.college)
        print("job: ",self.job)

class faculty():
    experiance = "yes"
    salary = "70000"
    years_working = int(input("Enter the number of working years"))
    def get_info(self):
        print("Name: ",self.name)
        print("experience: ",self.experiance)
        print("salary: ",self.salary)
        print("years: ",self.years_working)

class authority():
    department = "Data Science"
    nature = "Strict"
    years = 3
    def get_info(self):
        print("Name: ",self.name)
        print("department: ",self.department)
        print("nature: ",self.nature)
        print("years: ",self.years)

A = student()
B = faculty()
C = authority()
A.name = str(input("Enter the name of the student"))
B.name = str(input("Enter the name of the faculty"))
C.name = str(input("Enter the name of the authority"))

A.get_info()
B.get_info()
C.get_info()

