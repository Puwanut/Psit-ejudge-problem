"""Guess"""
def guess_answer():
    """Guess the answer range and show the possible answers"""
    ans_set = set(range(0, 101))
    while True:
        guess = input()
        if guess == "END":
            print(*sorted(ans_set))
            break
        ans_set = analyze(guess, ans_set)

def analyze(guess, ans_set):
    """analyze guess and return possible answer"""
    operator, value, yes_no = guess.split()
    value = int(value)

    if operator == '>':
        if yes_no == 'YES': # > value
            return ans_set.intersection(set(range(value+1, 101)))
        else: # <= value
            return ans_set.intersection(set(range(0, value+1)))

    elif operator == '<':
        if yes_no == 'YES': # < value
            return ans_set.intersection(set(range(0, value)))
        else: # >= value
            return ans_set.intersection(set(range(value, 101)))

    elif operator == '=':
        if yes_no == 'YES': # = value
            return {value}
        else: # != value
            return ans_set - {value}

guess_answer()
