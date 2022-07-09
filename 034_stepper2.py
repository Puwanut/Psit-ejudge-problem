"""Stepper II"""
def main(num1, num2):
    """print num m to n"""
    count = 1
    if num1 > num2:
        count = -1
    for i in range(num1, num2+count, count):
        print(i)
main(int(input()), int(input()))
