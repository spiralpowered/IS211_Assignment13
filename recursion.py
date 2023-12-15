from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonacci(n):
    if n < 1:
        raise ValueError("n must be a positive integer.")

    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)

def gcd(a,b):
    if a < 0:
        raise ValueError("a must be a positive integer or 0.")
    if b < 0:
        raise ValueError("b must be a positive integer or 0.")

    if a == 0:
        return b
    elif b == 0:
        return a
    elif a > 0:
        return gcd(b,(a%b))

def compareTo(s1,s2):
    if len(s1) > len(s2):
        return 1
    elif len(s1) < len(s2):
        return -1
    elif len(s1) == len(s2):
        if s1 == '' and s2 == '':
            return 0
        elif s1[0] > s2[0]:
            return 1
        elif s1[0] < s2[0]:
            return -1
        else:
            return compareTo(s1[1:], s2[1:])

if __name__ == '__main__':

    print("Fibonacci Sequence")
    n = int(input("Enter a number: "))
    print(f"nth term in fibonacci = {fibonacci(n)}")

    print("\nEuclid’s GCD Algorithm")
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(f"GCD = {gcd(a, b)}")

    print("\nString Comparison")
    x = str(input("Enter a string: "))
    y = str(input("Enter another string: "))
    print(compareTo(x, y))