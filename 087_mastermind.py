"""[Midterm 2019] Mastermind"""
def main(ans, guess):
    """show result of guess"""
    ans = list(ans)
    guess = list(guess)
    result = []
    for i in range(4):
        if guess[i] == ans[i]:
            result.append("B")
            ans[i] = "-"
            guess[i] = "-"
    for _ in range(ans.count("-")):
        ans.remove("-")
        guess.remove("-")
    for num in guess:
        if num in ans:
            result.append("W")
    while len(result) < 4:
        result.append("O")
    print(*result, sep="")
main(input(), input())
