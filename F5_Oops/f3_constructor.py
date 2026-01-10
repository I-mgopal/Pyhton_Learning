class Learner:
    student_count = 3 #class attribute
    #constructor method
    def __init__(self, course,name,age):
        self.course = course #instance attributes
        self.name = name
        self.age = age

    def show(self): #instance method
        print(f"All details are: Course: {self.course}, Name: {self.name}, Age: {self.age}")
    
    @classmethod
    def total_students(cls): #class method
        return cls.student_count
    
    @staticmethod
    def info(): #static method
        print("This is a Learner class to demonstrate constructor, class method and static method.")

Studetn1 = Learner("Python","John",20)
Studetn2 = Learner("Js","Doe",21)
Studetn3 = Learner("Solana","Alice",22)

# Learner("Python","John",20).show()
print("Total Students:", Learner.student_count)
Studetn1.show()
Studetn2.show()
Studetn3.show()

print("Total Students using class method:", Learner.total_students())
Learner.info()

