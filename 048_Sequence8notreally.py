"""Sequence VII"""
def main(num):
    """print sequence"""
    for i in range(1, num+1):
        print(" "*(num*2-i), end="")
        for j in range(1, i+1):
            print(j, end=" ")
        print()
main(int(input()))
