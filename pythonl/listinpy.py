numbers=[10,9,8,7,6,5,4,3,2,1,11]
add=0
for i in numbers:
    add+=i
print(add)
#min value in list
minnum=numbers[0]
for i in  numbers:
    if minnum>i:
        minnum=i
print("Minimum number in list :"+str(minnum))
#max value in list
maxnum=numbers[0]
for i in  numbers:
    if maxnum<i:
        maxnum=i
print("Maximum Number in list :" + str(maxnum))
#reversing a list
temp=0
listLength =int(len(numbers)/2)
k=1
for i in range(0, listLength):
    temp=numbers[i]
    numbers[i]=numbers[len(numbers)-k]
    numbers[len(numbers)-k]=temp
    k=k+1
print(numbers)
#reversing a list using appernd function
for i in range(len(numbers),0 ,-1):
    numbers.append(numbers.pop(i-1))
print(numbers)

