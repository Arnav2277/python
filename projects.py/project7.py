import random

def play_game(difficulty):
    ranges = {"easy": (1, 50), "normal": (1, 100), "hard": (1, 200)}
    low, high = ranges[difficulty]
    secret = random.randint(low, high)
    attempts = 0
    lower_bound, upper_bound = low, high

    print(f"\nI've picked a number between {low} and {high}. Good luck!\n")

    while True:
        try:
            guess = int(input(f"Range: [{lower_bound} ... {upper_bound}] — Your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < low or guess > high:
            print(f"Out of range! Guess between {low} and {high}.")
            continue

        attempts += 1

        if guess < secret:
            lower_bound = max(lower_bound, guess + 1)
            print("Too low!")
        elif guess > secret:
            upper_bound = min(upper_bound, guess - 1)
            print("Too high!")
        else:
            print(f"\nCorrect! You cracked it in {attempts} guess{'es' if attempts != 1 else ''}!")
            return attempts

def main():
    print("=== NEON GUESS ===")

    while True:
        print("\nSelect difficulty:")
        print("  1. Easy   [1–50]")
        print("  2. Normal [1–100]")
        print("  3. Hard   [1–200]")

        choice = input("Enter 1, 2, or 3: ").strip()
        difficulty_map = {"1": "easy", "2": "normal", "3": "hard"}

        if choice not in difficulty_map:
            print("Invalid choice, try again.")
            continue

        play_game(difficulty_map[choice])

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
    