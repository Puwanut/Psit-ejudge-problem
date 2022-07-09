"""Compound Interest"""
def getmoney(deposit, interest, year):
    """find future value"""
    value = deposit
    for _ in range(year):
        value *= (1+interest/100)
    print("%.2f"%value)
getmoney(int(input()), float(input()), int(input()))
