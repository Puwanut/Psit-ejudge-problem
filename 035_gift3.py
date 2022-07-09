"""Gift III"""
def main(amount):
    """find heavy2nd gift """
    if amount == 0:
        print("Exit")
    else:
        heavy_1st = int(input())
        heavy_2nd = 0
        for _ in range(amount-1):
            weight2 = int(input())
            if weight2 > heavy_1st:
                heavy_2nd, heavy_1st = heavy_1st, weight2
            elif heavy_2nd <= weight2 < heavy_1st:
                heavy_2nd, heavy_1st = weight2, heavy_1st
        if heavy_2nd == 0:
            print("Exit")
        else:
            print(heavy_2nd)
main(int(input()))
