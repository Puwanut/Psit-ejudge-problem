"""Turnstile"""
def main(action, state, amount):
    """find amount of people that walk pass"""
    while action != "END":
        if state == "Locked":
            if action == "C":
                state = "Unlocked"
        else:#state == "Unlocked"
            if action == "P":
                amount += 1
                state = "Locked"
        action = input()
    print(amount)
main(input(), "Locked", 0)
