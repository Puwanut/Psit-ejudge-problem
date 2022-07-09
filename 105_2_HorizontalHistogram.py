"""HorizontalHistogram"""
def main(text):
    """ """
    upper, lower = [], []
    for char in text:
        if char not in upper+lower:
            if char.isupper():
                upper.append(char)
            else:
                lower.append(char)
    for char in charlist:
        count = text.count(char)
        print(char + " : ", end="")
        for i in range(1, count+1):
            if i%6 == 0:
                print("|", end="")
            print("-", end="")
        print()
main(input())
