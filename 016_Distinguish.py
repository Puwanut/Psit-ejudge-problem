"""Distinguish"""
def main(height):
    """check condition height over 180 cm"""
    if height > 180:
        print("You're hit the door edge.")
    else:
        print("Nothing happens.")
main(int(input()))
