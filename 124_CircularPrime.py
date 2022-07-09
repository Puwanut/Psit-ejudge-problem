"""CircularPrime"""
def sum_circularprime(amount):
    """Find sum of all Circular Prime in range 1 to amount"""
    total = 0
    for num in range(1, amount+1):
        if is_circularprime(num):
            total += num
    print(total)

def is_circularprime(num):
    """Return True if num is Circular Prime"""
    for i in range(len(str(num))):
        rotate_num = rotate(num, i)
        if not is_prime(rotate_num):
            return False
    return True

def rotate(num, i):
    """Swap num by rotate"""
    return int(str(num)[i:]+str(num)[:i])

def is_prime(num):
    """Return True if num is Prime number"""
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

sum_circularprime(int(input()))
