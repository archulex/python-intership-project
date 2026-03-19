num1=float(input("enter the first number"))
num2=float(input("enter the first number"))


#choice the one option
print("choice the one option:")
print("1. addition(+)")
print("2. multiply(*)")
print("3. division(/)")
print("4 . Subtraction(-)")

choice = input("Enter choice (1/2/3/4): ")

# Perform calculation
if choice == "1":
    print("Result:", num1 + num2)

elif choice == "2":
    print("Result:", num1 - num2)

elif choice == "3":
    print("Result:", num1 * num2)

elif choice == "4":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero not allowed!")

else:
    print("Invalid choice!")

