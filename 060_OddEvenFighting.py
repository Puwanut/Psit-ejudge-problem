"""OddEvenFighting"""
def main(num, total_odd, total_even):
    """find winner(most value)"""
    while num != 0:
        if num%2 == 0:
            total_even += num
        else:
            total_odd += num
        num = int(input())
    if total_even > total_odd:
        print("Even", total_even)
    elif total_odd > total_even:
        print("Odd", total_odd)
    else:
        print("Draw", total_even)
main(int(input()), 0, 0)
