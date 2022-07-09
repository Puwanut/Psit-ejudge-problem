"""Triangle I"""
def main(length1, length2, length3):
    """s0rt length and check can create triangle"""
    if length1 > length2:
        length1, length2 = length2, length1
    if length2 > length3:
        length2, length3 = length3, length2
    if length1 > length2:
        length1, length2 = length2, length1
    if abs(length3**2 - (length1**2 + length2**2)) <= 0.01:
        print("Yes")
    else:
        print("No")

main(float(input()), float(input()), float(input()))
