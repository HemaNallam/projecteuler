#The sum of the primes below 10 is 2+3+5+7=17.Find the sum of all the primes below two million.

import time

sum = 2
start = time.time()

for number in range(3, 2000000):
    prime = True
    for x in range(2, number):
        if number % x == 0:
            prime = False
    if prime:
        sum += number

print "Sum =", sum
end = time.time() - start
print "Runtime =", end
