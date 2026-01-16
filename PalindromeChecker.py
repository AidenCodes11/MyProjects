def ispalindrome(n: str) -> bool:
    return n == n[::-1]

if __name__ == "__main__":
    while True:
        n = input("Choose a word: ")
        print(f"Is \"{n}\" a palindrome: {ispalindrome(n)}")
