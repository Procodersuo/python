class Students:
    def __intit__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks

    def displayDetails(self):
        print("Name " + self.name)
        print("Roll No "+ self.rollno)
        print("Marks "+ self.marks)
    
    def isPassed(self):
        if self.marks>40:
            print("Student Pass")
        else:
            print("Student Fail")

student1=Students("TALHA","1044",44)
student1.displayDetails()
student1.isPassed()
student2=Students("Ali","1057",41)
student2.displayDetails()
student2.isPassed()



