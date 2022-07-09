"""Largest Number"""
def main(num1, num2, num3, largest):
    """find largest number and print"""
    largest = findlarge(num1, num2, num3, largest)
    largest = findlarge(num1, num3, num2, largest)
    largest = findlarge(num2, num1, num3, largest)
    largest = findlarge(num2, num3, num1, largest)
    largest = findlarge(num3, num1, num2, largest)
    largest = findlarge(num3, num2, num1, largest)
    print(largest)

def findlarge(num1, num2, num3, largest):
    """check s0rt number that more than largest or not"""
    total = int(num1+num2+num3)
    if total > largest:
        return total
    return largest

main(input(), input(), input(), 0)
