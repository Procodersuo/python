class Students:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    @staticmethod
    def college():
        print("Hello")
    
    def average(self):
        sum=0
        for i in self.marks:
            sum+=i
        
        sum=sum/len(self.marks)
        print("Average marks of " + self.name + "are" + str(sum))


s1=Students("TALHA",[10,20,30])
s1.average()
