"""Sequence V"""
def main(num):
    """print sequence"""
    count = 1
    for i in range(num, 0, -1):
        print(str(i) + " ", end="\n"*(count%7 == 0))
        count += 1
main(int(input()))
