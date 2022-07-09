"""Discount"""
def totalpay():
    """find total price to pay"""
    bookprice = []
    while True:
        cashier = input()
        if cashier == "ENTER":
            break
        bookprice.append(int(cashier))
    bookprice.sort()
    buy = len(bookprice)
    if buy >= 25:
        bookprice = bookprice[buy//5:]
    elif buy >= 20:
        bookprice = bookprice[4:]
    elif buy >= 12:
        bookprice = bookprice[2:]
    elif buy >= 6:
        bookprice = bookprice[1:]
    print(sum(bookprice))

totalpay()
