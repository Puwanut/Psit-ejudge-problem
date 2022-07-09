"""[Final 2018] Semiprime"""
def is_prime(num):
    """Return True if num is Prime number"""
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

def allsemiprime(amount):
    """find amount of semiprime"""
    primes = []
    for num in range(1, amount+1):
        if is_prime(num):
            primes.append(num)

    semiprime = 0
    for i in range(len(primes)):
        prime1 = primes[i]
        for prime2 in primes[i:]:
            if prime1*prime2 <= amount:
                semiprime += 1
    print(semiprime)

allsemiprime(int(input()))
