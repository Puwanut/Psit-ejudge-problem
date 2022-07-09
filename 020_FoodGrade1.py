"""FoodGrade I"""
def main(weight, amount, count):
    """print amount of chicken weight in range 60+-10"""
    if 50 <= weight <= 70:
        count += 1
    if amount-1 == 0:
        print(count)
    else:
        return main(int(input()), amount-1, count)
main(int(input()), 24, 0)
