scores = [12, 25, 33, 41, 50, 67, 72, 85, 91, 98]
n, target = len(scores), 98
print("=== Quiz Score Finder (n ="n, n, "scores)===")
print("Scores:", scores, "| Target:", target)
print()



steps = 0
for i in range (n):
    steps += 1
    if scores[i] == target:
        print("Linear search : index =", i,"|steps =", steps, "| O(n)")
        break
print()

lo, hi, steps = 0, n - 1, 0
while lo <= hi:
    mid = (lo + hi)// 2
    steps += 1
    if scores[mid] == target:
        print("Binary search : index =", mid, "| steps =", steps,"| O(n)")