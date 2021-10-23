# recursive function to find the factorial of a number
def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return (n * factorial(n - 1))


def main():
    a = int(input("Enter a positive integer:"))
    fact = factorial(a)
    print("Factorial=", fact)
    return
main()
