import math

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

lcm = abs(num1 * num2) // math.gcd(num1, num2)

print("The LCM is:", lcm)