
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Before swap:")
print("a =", a)
print("b =", b)


a = a ^ b
b = a ^ b
a = a ^ b

print("After swap:")
print("a =", a)
print("b =", b)