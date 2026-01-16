def isprime(n: int) -> bool:
    if isinstance(n, complex):
        return False
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    for i in range(1000, 10001):
        print(f"Is {i} prime: {isprime(i)}")