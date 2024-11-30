numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for nam in numbers:
    if nam == 1:
        continue
    is_prime = True
    for i in range(2, nam):
        if nam % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(nam)
    else:
        not_primes.append(nam)

print("Primes:", primes)
print("Not primes:", not_primes)