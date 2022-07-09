"""Gift II"""
def main():
    """main function"""
    weight1, weight2, weight3, weight4 = int(input()), int(input()), int(input()), int(input())
    weight5, weight6, weight7, weight8 = int(input()), int(input()), int(input()), int(input())
    checkgift(weight1)
    checkgift(weight2)
    checkgift(weight3)
    checkgift(weight4)
    checkgift(weight5)
    checkgift(weight6)
    checkgift(weight7)
    checkgift(weight8)

def checkgift(weight):
    """find even number gift and print it"""
    if weight%2 == 0:
        print(weight)

main()
