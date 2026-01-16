def factorial(n: int) -> int:
    if n <= 0:
        return 1
    final = 1
    for i in range(2, n + 1):
        final *= i
    return final

if __name__ == "__main__":
    print(factorial(7))