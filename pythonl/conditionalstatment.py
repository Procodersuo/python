print("Press 1 for addition 2 for subtraction 3 for mulyiply 4 for divide")

choice = int(input())

if choice==1:
    num1 = int(input("Enter first number: "))
    num2= int(input("Enter Second Nunber"))
    print(num1+num2)
elif choice==2:
    num1 = int(input("Enter first number: "))
    num2= int(input("Enter Second Nunber"))
    print(num1-num2)
elif choice==3:
    num1 = int(input("Enter first number: "))
    num2= int(input("Enter Second Nunber"))
    print(num1*num2)
elif choice ==4:
    num1 = int(input("Enter first number: "))
    num2= int(input("Enter Second Nunber"))
    print(num1/num2)
else :
    print("Invalid choice")

