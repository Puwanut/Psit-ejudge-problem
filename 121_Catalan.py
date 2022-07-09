"""Catalan"""
def catalan(num):
    """find value of catalan"""
    c_old = 1
    for i in range(num):
        c_num = ((4*i+2)/(i+2))*c_old
        c_old = c_num
    print(int(c_num))
catalan(int(input()))
