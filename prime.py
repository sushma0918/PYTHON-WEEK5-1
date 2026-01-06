#24331A05G8
#prime number without recursion
def is_prime(n):
    if n <= 1:
        return False


    for i in range(2, n):
        if n % i == 0:
            return False
    return True
num = int(input("Enter a number: "))
if is_prime(num):
    print("Prime number")
else:
    print("Not a prime number")


#prime number with recursion
def is_prime_recursive(n, i=2):
    if n <= 1:
        return False
    if i == n:
        return True
    if n % i == 0:
        return False
    return is_prime_recursive(n, i + 1)
num = int(input("Enter a number: "))
if is_prime_recursive(num):
    print("Prime number")
else:
    print("Not a prime number")
