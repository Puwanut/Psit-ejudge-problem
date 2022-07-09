"""Grade II"""
def main(point):
    """calculate Grade"""
    if 0 <= point <= 100:
        if point >= 95:
            print("A")
        elif point >= 90:
            print("B+")
        elif point >= 85:
            print("B")
        elif point >= 80:
            print("C+")
        elif point >= 75:
            print("C")
        elif point >= 70:
            print("D+")
        elif point >= 65:
            print("D")
        elif point >= 60:
            print("F+")
        else:
            print("F")
    else:
        print("ERR")
main(float(input()))
