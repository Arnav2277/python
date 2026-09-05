print("======================================")
print("     BINARY CLUE INVESTIGATOR")
print("======================================")

clues = {
    "10100": "20",
    "10001": "17",
    "11010": "26",
    "01001": "9",
    "11111": "31"
}

print("\nYou are a Binary Clue Investigator!")
print("Decode the binary clues to solve the mystery.")
print("Type 'quit' to exit.\n")

score = 0

for binary, answer in clues.items():
    print("--------------------------------------")
    print("Binary clue:", binary)

    user_answer = input("What is the decimal number? ")

    if user_answer.lower() == "quit":
        break

    if user_answer == answer:
        print("Correct! You found a clue.")
        score += 1
    else:
        print("Incorrect!")
        print("The answer was:", answer)

print("\n======================================")
print("INVESTIGATION COMPLETE")
print("======================================")
print("Your score:", score, "/", len(clues))

if score == len(clues):
    print("Excellent! You solved every clue!")
elif score >= 3:
    print("Good investigation!")
else:
    print("Keep practising binary numbers!")