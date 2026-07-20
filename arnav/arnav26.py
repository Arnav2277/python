n = 4
print("=== Counting Game Points (n =", n, "rounds) ")
print()


total = n +(n + 1) // 2
print("Formula way : total =", total, "| steps = 1")


total = 0
steps = 0
for round_num in range(1, n + 1):
    total += round_num
    steps += 1
print("Loop way    : total =", total, "| steps=", steps)    