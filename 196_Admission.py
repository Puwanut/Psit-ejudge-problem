"""[Final 2019 Recommend] Admission"""
def admission():
    """best admission"""
    min_point = {"A": 20000,
                 "B": 17500,
                 "C": 18000,
                 "D": 28250,
                 "E": 27000,
                 "F": 25000,
                 "G": 21750,
                 "H": 22000}
    point = int(input())
    fac1, fac2, fac3, fac4 = input(), input(), input(), input()
    if point >= min_point[fac1]:
        return fac1
    elif point >= min_point[fac2]:
        return fac2
    elif point >= min_point[fac3]:
        return fac3
    elif point >= min_point[fac4]:
        return fac4
    return "FISHER"

print(admission())
