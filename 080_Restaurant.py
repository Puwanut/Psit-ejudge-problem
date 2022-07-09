"""Restaurant"""
def main(price1, pro, discount, add):
    """find worth price"""
    price2 = (price1+add)*(100-discount)/100
    if price1 == pro:
        price1 = price1*(100-discount)/100
    if price1 < price2:
        print("No %.3f"%(price2-price1))
    elif price1 > price2:
        print("Yes %.3f"%(price1-price2))
    else:
        print("Yes")
main(float(input()), float(input()), float(input()), float(input()))
