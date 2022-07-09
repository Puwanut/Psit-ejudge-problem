"""Bill"""
def main(price):
    """find total price"""
    service = price*0.1
    if service < 50:
        service = 50
    elif service > 1000:
        service = 1000
    price += service
    price += (0.07*price)
    print("%.2f"%price)
main(int(input()))
