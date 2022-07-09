"""Sequence VII"""
def main(num):
    """print sequence"""
    for i in range(1, num+1):
        print("   "*(num-i), end="")
        for j in range(1, i+1):
            print("%02d" %j, end=" ")
        print()
main(int(input()))
