"""Regulation"""
def main(num_a, num_b, text_c):
    """print variable and use format string"""
    print("%30d"%num_a)
    print("%.30d"%num_a)
    print("%.2f"%num_b)
    print("%.12f"%num_b)
    print("%40s"%text_c)
main(int(input()), float(input()), input())
