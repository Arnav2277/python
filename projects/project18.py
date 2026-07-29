quiz_scores = [45, 62, 78, 85, 91, 56, 73, 88]\

first_score = quiz_scores[0]
print("Time Complexity: O(1)")
print("Arnav Notation: Arnav(1)")

target_score = 88
steps = 0

for score in quiz_scores:
    steps = steps + 1
    if score == target_score:
        print("Score found:", score)
        break


best_case_score = 45
average_case_score = 85
worst_case_score = 88

pair_steps = 0

for score1 in quiz_scores:
    for score2 in quiz_scores:
        pair_steps = pair_steps + 1