class Student(object):
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks
    def printName(self):
        print(self.name)
    def printMarks(self):
        print(self.marks)
    

s1 = Student("Kushaan",100)
s1.printMarks()

s2 = Student("Soham",2)
s2.printMarks()
s2.printName()
