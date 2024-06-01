numbers = [1, 2]
total = 0

for i in range(4000000):
    if i == numbers[-1] + numbers[-2]:
        numbers.append(i)

for n in numbers:
    if n % 2 == 0:
        total += n

print(total)
