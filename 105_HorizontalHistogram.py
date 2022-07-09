"""HorizontalHistogram"""
def main(text):
    """show amount of each characters"""
    charlist = []
    for char in text:
        if char not in charlist:
            charlist.append(char)
    charlist.sort(key=str.swapcase)
    for char in charlist:
        count = text.count(char)
        print(char + " : ", end="")
        for i in range(count):
            if i%5 == 0 and i >= 5:
                print("|", end="")
            print("-", end="")
        print()
main(input())
