"""FourDirections"""
def main(direction):
    """print directions in same line"""
    for row in range(1, 6):
        for i in direction:
            if row == 1 or row == 5:
                print("  *  ", end=" ")
            elif row == 2:
                print(" *   "*(i == 'L') + " *** "*(i == 'U') + \
                "  *  "*(i == 'D') + "   * "*(i == 'R'), end=" ")
            elif row == 3:
                print("*****"*(i == 'L' or i == 'R') + "* * *"*(i == 'U' or i == 'D'), end=" ")
            elif row == 4:
                print(" *   "*(i == 'L') + "  *  "*(i == 'U') + \
                " *** "*(i == 'D') + "   * "*(i == 'R'), end=" ")
        print()
main(input())
