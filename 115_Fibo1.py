"""FibonacciRecursionV1"""
def main(num):
    """find fibonacci of num"""
    if num == 0:
        return 0
    if num == 1:
        return 1
    return main(num-1) + main(num-2)
print(main(int(input())))
