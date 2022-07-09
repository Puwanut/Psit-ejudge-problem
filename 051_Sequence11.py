"""Sequence XI"""
def main(num):
    """print sequence"""
    for row in range(-num+1, num):
        row = -abs(row)+num
        for col in range(-num+1, num):
            col = -abs(col)+num
            if col <= row:
                print("%02d"%col, end=" ")
            elif row <= col:
                print("%02d"%row, end=" ")
        print()
main(int(input()))

