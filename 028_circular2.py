"""Circular II"""
def main():
    """check overlap part"""
    pos_x1, pos_y1, radius1 = float(input()), float(input()), float(input())
    pos_x2, pos_y2, radius2 = float(input()), float(input()), float(input())
    distance = ((pos_x1-pos_x2)**2+(pos_y1-pos_y2)**2)**.5 #ระยะห่างระหว่างเรากับเพื่อน
    if radius1+radius2 > distance:
        print("Yes")
    else:
        print("No")
main()
