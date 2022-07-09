"""Indicator_Right"""
def main(num_k, num_n):
    """print indicator right"""
    for i in range(-num_n//2+1, num_n//2+1):
        i = -abs(i)+num_n//2
        print(" "*i + "*"*num_k)
main(int(input()), int(input()))
