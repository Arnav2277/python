def is_armstrong(n: int) -> bool:
    digits = str(n)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == n


def main() -> None:
    raw = input("Enter a non-negative integer: ").strip()

    if not raw.isdigit():
        print("Invalid input. Please enter only digits (0-9).")
        return

    n = int(raw)
    digits = [int(d) for d in str(n)]
    power = len(digits)
    terms = [f"{d}^{power}" for d in digits]
    total = sum(d ** power for d in digits)

    print(f"\nDigits: {digits}")
    print(f"Number of digits (power): {power}")
    print(f"Calculation: {' + '.join(terms)} = {total}")

    if total == n:
        print(f"{total} == {n}  →  {n} IS an Armstrong number.")
    else:
        print(f"{total} != {n}  →  {n} is NOT an Armstrong number.")


if __name__ == "__main__":
    main()