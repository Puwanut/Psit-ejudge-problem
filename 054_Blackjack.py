"""BlackJack"""
def main(amount, point, ace):
    """show best possible point"""
    for _ in range(amount):
        card = input()
        if card == "J" or card == "Q" or card == "K":
            point += 10
        elif card == "A":
            ace += 1
        else:
            point += int(card)
    if ace == 1 and point <= 10:
        point += 11
    elif ace == 2 and point <= 9:
        point += 12
    elif ace == 3:
        point += 13
    else:
        point += ace
    print(point)
main(int(input()), 0, 0)
