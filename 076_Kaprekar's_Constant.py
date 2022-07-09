"""Kaprekar's Constant"""
def main(num, count):
    """find times to get a result 6174"""
    while int(num) != 6174:
        num1 = num[0]
        num2 = num[1]
        num3 = num[2]
        num4 = num[3]
        if num1 < num2:
            num1, num2 = num2, num1
        if num2 < num3:
            num2, num3 = num3, num2
        if num3 < num4:
            num3, num4 = num4, num3
        if num2 < num3:
            num2, num3 = num3, num2
        if num1 < num2:
            num1, num2 = num2, num1
        if num2 < num3:
            num2, num3 = num3, num2
        most = int(num1 + num2 + num3 + num4)
        less = int(num4 + num3 + num2 + num1)
        num = "%04d"%(most - less)
        count += 1
    print(count)
main(input(), 0)
