"""Perfect"""
def sum_perfect(amount):
    """find sum of perfect numbers in range 1 to amount"""
    total_perfect = 0
    for num in range(2, amount+1):
        total_num = 1
        for divisor in range(2, int(num**0.5)+1):
            if num%divisor == 0:
                divisor2 = num/divisor
                total_num += divisor+divisor2
        if total_num == num:
            total_perfect += num
    print(total_perfect)
sum_perfect(int(input()))
