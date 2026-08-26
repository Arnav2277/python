

print("=== SMART SWITCH BIT MONITOR ===")

bits = input("Enter switch states (0 = OFF, 1 = ON): ").replace(" ", "")


if all(bit in "01" for bit in bits):
    print("\nSwitch Status:")

    for i, bit in enumerate(bits, start=1):
        if bit == "1":
            print(f"Switch {i}: ON")
        else:
            print(f"Switch {i}: OFF")

    
    on = bits.count("1")
    off = bits.count("0")

    print("\n=== SUMMARY ===")
    print("Total switches:", len(bits))
    print("Switches ON:", on)
    print("Switches OFF:", off)

else:
    print("Error: Only 0 and 1 are allowed.")