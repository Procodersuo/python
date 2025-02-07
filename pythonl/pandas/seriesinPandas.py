import pandas as pd
x=[1,2,3,4,5,6,7,8,9]
#print a series in one dimensional
var=pd.Series(x)
print(var)
#change index and type of our dATA and change name of your data
# var =pd.Series(x, index= ["a","b"----], dtype= "float", NAME = "mYdata")
student = {
    "Name" : ["A","B"],
    "Class": ["Seven","SIX"],
    "Age":[8,9]
}
var=pd.Series(student,)
print(var)
myData =[2,4,5,6,7,8]
print(pd.Series(myData + var))


