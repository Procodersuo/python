print(2+2) #addition
print(2*2) #Multiplication
print(2/2) #divide
print(2%2) #remider
print(2//2) # divide but answer in int
print(2**7) # power
def power(number,power):
    n=0
    ans=1
    while n!=power:
        ans=ans*number
        n=n+1
    print(ans)
number=int(input("Enter Number ? "))
powe=int(input("Entter Power "))
power(number,powe)

#python run operators in PEMDAS
#1. Parentheses
#2. Exponents
#3. Multiplication and Division (from left to right)
#4. Addition and Subtraction (from left to right)



