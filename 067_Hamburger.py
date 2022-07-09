"""Hamburger"""
def main(left, right):
    """print hamburger"""
    print("|"*left + "**"*(left+right) + "|"*right)
main(int(input()), int(input()))
