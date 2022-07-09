"""Sequence III"""
def main(num):
    """print sequence"""
    for i in range(2, num+2):
        for j in range(i, num+i):
            print(j, end=" ")
        print()
main(int(input()))
