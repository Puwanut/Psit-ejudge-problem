"""Is prime larger"""
def is_prime(num):
    """Return True if num is Prime number"""
    if num == 2:
        return True
    if num == 1 or num%2 == 0:
        return False
    for i in range(3, int(num**.5)+1, 2):
        if num%i == 0:
            return False
    return True
print(is_prime(int(input())))
