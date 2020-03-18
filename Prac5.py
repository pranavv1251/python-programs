class Student:
    def __init__(self, rollno, name, score):
        self.rollno = rollno
        self.name = name
        self.score = score

    def calcgrade(self):
        if(self.score >= 80 and self.score <= 100):
            grade = 'A'
        elif(self.score >= 60 and self.score <= 79):
            grade = 'B'
        elif(self.score >= 40 and self.score <= 59):
            grade = 'C'
        else:
            grade = 'D'
        print('The grade is: ', grade)


stud = Student(8672, "Pranav", 98)
stud.calcgrade()
