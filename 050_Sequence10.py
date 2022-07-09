"""Sequence X"""
def main(num):
    """print sequence"""
    for i in range(1, num+1):
        print("   "*(num-i), end="")
        for j in range(1, i+1):
            print("%02d" %j, end=" ")
        for j in range(i-1, 0, -1):
            print("%02d" %j, end=" ")
        print()
    for i in range(num-1, 0, -1):
        print("   "*(num-i), end="")
        for j in range(1, i+1):
            print("%02d" %j, end=" ")
        for j in range(i-1, 0, -1):
            print("%02d" %j, end=" ")
        print()
main(int(input()))
