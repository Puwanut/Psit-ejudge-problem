"""Sequence IV"""
def main(num):
    """print sequence"""
    for i in range(1, num**2+1):
        print(str(i) + " ", end="\n"*(i%num == 0))
main(int(input()))
