num=input("Enter Number Which u want to get table")
lenght= int(input("Enter Lenght of your table"))
for i in range(1,lenght+1):
    print(num + "*" + str(i) + "=" + str(i*int(num)))