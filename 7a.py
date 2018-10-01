class student:
        'common base class for all employee'
        studentcount=0

        def __init__(self,name,age):
                self.name=name
                self.age=age
                student.studentcount+=1

        def displaycount(self):
                print('total student',student.studentcount)

        def displaystudent(self):
                print('name:',self.name,'\n','Age:',self.age)

stud1=student('Dhiraj kumar',19)
stud2=student('Sinha',19)
stud1.displaystudent()
stud2.displaystudent()
print('total student are',student.studentcount)
