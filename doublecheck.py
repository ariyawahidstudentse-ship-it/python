num = int(input("Enter a number to check: "))

if num>50:
    print(num, "is greater than 50")
    if num%2==0:
        print(num, "is also an Even number")
    else:
        print(num, "is also an Odd number")
else:
    print(num, "is not greater than 50")
