class Students:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks

    def displayDetails(self):
        print("Name " + self.name)
        print("Roll No "+ self.rollno)
        print("Marks "+ str(self.marks))
    
    def isPassed(self):
        if self.marks>40:
            print(self.name + "Pass")
        else:
            print(self.name +" Fail")

student1=Students("TALHA","1044",44)
student1.displayDetails()
student1.isPassed()
student2=Students("Ali","1057",41)
student2.displayDetails()
student2.isPassed()
student3=Students("Asad","1041",10)
student3.displayDetails()
student3.isPassed()



