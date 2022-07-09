"""Donut"""
def main(price, pro, free, want):
    """find worth price and amount recieved of buying donut"""
    pro_times = want//(pro+free)
    buy = pro*pro_times
    remain = want%(pro+free)
    if remain >= pro:
        buy += pro
    else:
        buy += remain
    amount = buy + (buy//pro)*free
    price = buy*price
    print(price, amount)
main(int(input()), int(input()), int(input()), int(input()))
