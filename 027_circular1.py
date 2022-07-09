"""Circular I"""
def main(my_x, my_y, radius, mos_x, mos_y):
    """check mosquito in my radius"""
    distance = ((my_x-mos_x)**2+(my_y-mos_y)**2)**.5
    if distance <= radius:
        print("Yes")
    else:
        print("No")
main(float(input()), float(input()), float(input()), float(input()), float(input()))
