"""Seeker"""
def main():
    """print total of code"""
    text = input()
    numlist = []
    num = ""
    total = 0
    for i in text+"a":
        if i.isdigit():
            num += str(i)
        elif num != "":
            numlist.append(int(num))
            num = ""
    for num in numlist:
        total += num
    print(total)
main()
