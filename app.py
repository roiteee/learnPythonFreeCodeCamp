class Student:
    def __init__(self, name, major, gpa, is_on_probation):    #Constructor
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

student1 = Student("Jim", "Business", 3.1, False)
print(student1.name)

student2 = Student("Pam", "Art", 2.5, True)
print(student2.gpa)
