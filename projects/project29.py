
n = input("Enter the number of elements: ")

elements = []
for i in range(n):
    elements.append(input(f"Enter element {i + 1}: "))

print("\nAll subsets:")

for mask in range(1 << n):
    subset = []

    for i in range(n):
        if mask & (1 << i):
            subset.append(elements[i])

    print(subset)