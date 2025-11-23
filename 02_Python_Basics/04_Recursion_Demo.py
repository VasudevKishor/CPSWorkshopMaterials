# 04_Recursion_Demo.py

def factorial(n):
    """Calculates n! (n * n-1 * ... 1)"""
    # BASE CASE
    if n == 1 or n == 0:
        return 1
    # RECURSIVE CASE
    else:
        return n * factorial(n - 1)

def main():
    num = 5
    print(f"Calculating factorial of {num}...")
    result = factorial(num)
    print(f"The factorial of {num} is: {result}")

if __name__ == "__main__":
    main()
