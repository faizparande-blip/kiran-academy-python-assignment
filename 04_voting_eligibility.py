age = int(input("Enter your age: "))

if age < 0 or age > 120:
    print("Invalid Age")

elif age >= 18:
    print("Valid Age")
    print("You are eligible for voting")

else:
    print("Valid Age")
    print("You are not eligible for voting")