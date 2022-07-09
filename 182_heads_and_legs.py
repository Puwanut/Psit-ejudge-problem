"""Heads and Legs"""
def findanimal(head, leg):
    """find amount of rabbits and birds"""
    rabbit, ghost = divmod(leg-2*head, 2)
    bird = head - rabbit
    if rabbit >= 0 and bird >= 0 and ghost == 0:
        print(rabbit, bird)
    else:
        print("Impossible")
findanimal(int(input()), int(input()))
