"""Align"""
def main(size, align, text):
    """print align text"""
    if align == "left":
        print(text)
    elif align == "center":
        print(text.center(size+(len(text)%2 != 0)))
    else:
        print(text.rjust(size))
main(int(input()), input(), input())
