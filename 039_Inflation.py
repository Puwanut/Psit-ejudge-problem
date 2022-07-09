"""Inflation"""
def main(price, year):
    """find price in next k years"""
    for _ in range(year):
        price += (price*381)//10000
    print("%d.%02d"%(price//100, price%100))
main(int(float(input())*100), int(input()))
