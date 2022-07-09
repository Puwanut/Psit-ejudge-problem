"""Difference"""
def main(amount_a, amount_b):
    """find difference of Set A - Set B"""
    set_a, set_b = set(), set()
    for _ in range(amount_a):
        set_a.add(int(input()))
    for _ in range(amount_b):
        set_b.add(int(input()))
    set_ans = set_a-set_b
    set_ans = sorted(set_ans)
    print(*set_ans)
main(int(input()), int(input()))
