#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13. What is the 10 001st prime number? 
def isprime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
x = 3
counter = 2
while counter <= 10001:
    if isprime(x):
        counter += 1
        x += 2
    else:
        x += 2
print (x)
