"""[Midterm 2019] Harshad Number"""
def main():
    """check num is Harshad number or not"""
    divider = 0
    for _ in range(10):
        num = input()
        for i in num:
            if i == "-":
                continue
            divider += int(i)
        if divider == 0 or int(num)%divider != 0:
            print("No")
        else:
            print("Yes")
        divider = 0
main()
