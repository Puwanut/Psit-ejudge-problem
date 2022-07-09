"""[Midterm 2019] Elo"""
def main(rate_a, rate_b, player):
    """find elo of player"""
    elo_a = 1/(1+10**((rate_b-rate_a)/400))
    elo_b = 1/(1+10**((rate_a-rate_b)/400))
    if player == "A":
        print("%.2f"%elo_a)
    else:
        print("%.2f"%elo_b)
main(int(input()), int(input()), input())
