"""[Midterm 2019] Sequence N"""
def main(size):
    """print N by size"""
    for row in range(size):
        for col in range(size):
            if col == 0 or col == size-1 or row == col:
                print("*", end="")
            else:
                print(" ", end="")
        print()
main(int(input()))
