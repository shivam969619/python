n = float(input("Please enter the first number: "))  # Convert input to float
m = float(input("Please enter the second number: "))  # Convert input to float
t = input("Please enter the operation you want to do (+, *, /, -): ")

ans = 0

if t == "+":  # Use == for comparison
    ans = n + m
elif t == "-":  # Use elif instead of else if
    ans = n - m
elif t == "*":
    ans = n * m
elif t == "/":
    if m != 0:  # Check for division by zero
        ans = n / m
    else:
        print("Error: Division by zero!")
else:
    print("Error: Invalid operation!")

print("Result:", ans)
