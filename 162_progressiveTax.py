"""[Midterm 2014] ProgressiveTax"""
def findtax(income):
    """find tax"""
    tax = 0
    rate_income = [4000000, 2000000, 1000000, 750000, 500000, 300000, 150000]
    rate_tax = [0.35, 0.30, 0.25, 0.20, 0.15, 0.10, 0.05]
    for i in range(7):
        if income > rate_income[i]:
            excess = income - rate_income[i]
            tax += int(rate_tax[i]*excess)
            income -= excess
    print(tax)
findtax(float(input()))
