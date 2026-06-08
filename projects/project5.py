def fibonacci(n):
    """Return the first n Fibonacci numbers as a list."""
    if n <= 0:
        return []
    if n == 1:
        return [0]

    seq = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq


def fibonacci_generator(n):
    """Yield Fibonacci numbers one at a time (memory-efficient)."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def fibonacci_recursive(n, memo={}):
    """Return the n-th Fibonacci number using memoized recursion."""
    if n < 2:
        return n
    if n not in memo:
        memo[n] = fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    return memo[n]


if __name__ == "__main__":
    n = 10
    print(f"First {n} Fibonacci numbers (list):")
    print(fibonacci(n))

    print(f"\nFirst {n} Fibonacci numbers (generator):")
    print(list(fibonacci_generator(n)))

    print(f"\n{n}-th Fibonacci number (recursive):")
    print(fibonacci_recursive(n))