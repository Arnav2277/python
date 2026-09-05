print("================================")
print("       POWER OF 2 SCANNER")
print("================================")

while True:
    number = input("\nEnter a number to scan (or type 'quit'): ")

    if number.lower() == "quit":
        print("Scanner shutting down...")
        break

    if not number.isdigit():
        print("Please enter a valid whole number.")
        continue

    number = int(number)

    if number > 0 and (number & (number - 1)) == 0:
        print("SCAN RESULT: YES")
        print(number, "is a power of 2.")

        power = 0
        value = 1

        while value < number:
            value *= 2
            power += 1

        print(number, "= 2^", power)

    else:
        print("SCAN RESULT: NO")
        print(number, "is NOT a power of 2.")

print("\nScanner closed.")