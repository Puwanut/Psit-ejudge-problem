"""BootSequence"""
def main(num):
    """print 1 to num and seperate with _ """
    for i in range(1, num+1):
        print(i, end="_"*(i != num))
main(int(input()))
