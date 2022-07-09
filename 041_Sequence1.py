"""Sequence I"""
def main(num):
    """print 1 to num for num line"""
    for _ in range(num):
        for i in range(1, num+1):
            print(i, end=" ")
        print()
main(int(input()))
