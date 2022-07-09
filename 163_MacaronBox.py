"""[Midterm 2015] MacaronBoxSML"""
def usebox(amount):
    """find amount of box used"""
    large = amount//24
    medium = small = 0
    remain = amount%24
    if remain > 12:
        large += 1
    elif 6 < remain <= 12:
        medium += 1
    elif remain > 0:
        small += 1
    print(small, medium, large, sep='\n')
usebox(int(input()))
