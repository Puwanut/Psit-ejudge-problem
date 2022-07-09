"""DataSpike"""
def main():
    """main function"""
    size1, size2, size3, size4 = int(input()), int(input()), int(input()), int(input())
    size5, size6, size7, size8 = int(input()), int(input()), int(input()), int(input())
    largest = size1
    largest = findlargest(largest, size2)
    largest = findlargest(largest, size3)
    largest = findlargest(largest, size4)
    largest = findlargest(largest, size5)
    largest = findlargest(largest, size6)
    largest = findlargest(largest, size7)
    largest = findlargest(largest, size8)
    print(largest)

def findlargest(largest, size):
    """find largest and return largest size"""
    if largest < size:
        return size
    return largest
main()
