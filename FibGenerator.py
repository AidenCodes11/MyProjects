from sys import setrecursionlimit
from math import sqrt

def fib(n: int | complex) -> int | complex:
    if isinstance(n, complex):
        phi = (1 + sqrt(5)) / 2
        psi = (1 - sqrt(5)) / 2
        return ((phi ** n) - (psi ** n)) / sqrt(5)


    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    do_complex = input("Do you want complex numbers (default n, y or n, complicated math)? ").lower() != "n"

    while True:
        n = input("Enter number: ")
        if do_complex:
            j = input("Enter complex number: ")
        print(f"Fibonacci of {n} is: {fib(int(n))}")
        if do_complex:
            print(f"Fibonacci of {j.lower().replace("j", "")}j is close to: "
                  f"{fib(eval(f"{j.lower().replace("j", "")}j"))}")