num1=int(input("Enter A number For Which you want to get table "))
num2=int(input("Enter THE limit for table "))

for i in range(1,num2+1):
    ans=num1*i
    print(str(num1) + "*" + str(i) + "=" +   str(ans) )