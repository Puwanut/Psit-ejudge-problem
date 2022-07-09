"""SurprisingVote"""
def main(total, highest):
    """chance of surprising"""
    remain = total-highest
    if remain-highest >= 0:
        vote2 = highest
        vote3 = remain-vote2
    else:
        vote2 = remain
        vote3 = 0
    if highest-vote3 > 2:
        print("Surprising")
    else:
        print("Not surprising")
main(float(input()), float(input()))
