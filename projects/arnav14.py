file = open("bucket-list.txt","w")
file.write("1. Visit the Eiffel Tower\n")
file.write("2. Learn to play the guitar\n")
file.write("3. Code my own game\n")
file.close()
print("bucket list saved to bucket-list-txt!")


file = open("bucket-list.txt", "r")
content = file.read()
print("\n=== My bucket List ===")
print(content)
file.close()

file = open("bucket-list.txt", "r")
lines = file.readlines()
print(f"You have {len(lines)} items on your bucket list.")
file.close()