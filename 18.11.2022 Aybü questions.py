#Can Kankılıç
n = int(input("Please enter a number"))
list1 = str(n)
a=1
b=0
while b<n:
    b=b+1
    a=a+1
    for x in range(1,a,1):
        print(x,end=" ")
    print(" *"*(n-a+1))
    print("\n")

    