"""Amicable"""
def sum_amicable(amount):
    """find sum of amicable numbers in range 1 to amount"""
    total = 0
    for num in range(1, amount+1):
        if is_amicable(num, amount):
            total += num
    print(total)

def is_amicable(num, amount):
    """Return True if num is Amicable"""
    sum_p
    if num <= amount: