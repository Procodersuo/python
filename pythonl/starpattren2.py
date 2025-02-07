i=1
j=1
while i<=5:
    while j<i:
        print(" ", end=" ")
        j=j+1
    # reinitiliazing value
    k=5
    j=1
    while k>=i:
        print("*", end=" ")
        k=k-1
    print()
    i=i+1


for i in range(0,5):
    for j in range(0,i):
        print(" ", end=" ")
    for k in range(i,5):
        print("*", end=" ")
    print()


