#unorder collection of data 
#its like a key pair value
#it is mutuable
myDic ={
    "Name": ["Talha","Ali"],
    "age":22,
    "Role":"AI Engineer",
}

print(myDic["Name"][1])
myDic["Name"][1]="fURQAN"
print(myDic["Name"][1])
print(type(myDic["age"]))

print(myDic.values()) # extract values of keys from dic...
print(myDic)
myDic["Country"]="Pakistan"
print(myDic)
myDic2={
    "Project":"AI DRIVEN cARS"
}
#CONCATENATION OF DICTIONARIES
myDic.update(myDic2)
print(myDic)