"""Sequence XII"""
def main(num):
    """print sequence"""
    for row in range(-num+1, num):
        for col in range(-num+1, num):
            print("%02d"%(num-abs(abs(col)-abs(row))), end=" ")
        print()
main(int(input()))
