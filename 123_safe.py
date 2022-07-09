"""Safe"""
def rotatetimes(pass1, pass2):
    """find rotate times from pass1 to pass2"""
    count_rotate = 0
    for i in range(len(pass1)):
        rotate = abs(ord(pass1[i])-ord(pass2[i]))
        if rotate >= 13:
            count_rotate += (26-rotate)
        else:
            count_rotate += rotate
    print(count_rotate)
rotatetimes(input(), input())
