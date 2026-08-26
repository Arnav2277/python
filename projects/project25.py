

print("=== SECRET BIT SCANNER ===")

bits = input("Enter your secret binary code: ")


if all(bit in "01" for bit in bits):
    if len(bits) % 8 == 0:
        message = ""

        for i in range(0, len(bits), 8):
            byte = bits[i:i+8]
            character = chr(int(byte, 2))
            message += character

        print("Decoded message:", message)

    else:
        print("Error: The number of bits must be a multiple of 8.")
else:
    print("Error: Only 0 and 1 are allowed.")