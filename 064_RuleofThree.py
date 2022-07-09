"""RuleofThree"""
def main(amount, worth_price, worth_size, best_ratio):
    """find the best worth"""
    for _ in range(amount):
        price, size = float(input()), float(input())
        ratio = size/price
        if ratio > best_ratio:
            best_ratio = ratio
            worth_price, worth_size = price, size
        elif ratio == best_ratio and price < worth_price:
            worth_price, worth_size = price, size
    print("%.2f %.2f"%(worth_price, worth_size))
main(int(input()), 0, 0, 0)
