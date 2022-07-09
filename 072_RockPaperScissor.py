"""RockPaperScissor"""
def main(text, point_a, point_b):
    """Show competition results"""
    for i in range(0, len(text), 2):
        if text[i] == 'P' and text[i+1] == 'R':
            point_a += 1
        elif text[i] == 'R' and text[i+1] == 'P':
            point_b += 1
        elif text[i] == 'S' and text[i+1] == 'P':
            point_a += 1
        elif text[i] == 'P' and text[i+1] == 'S':
            point_b += 1
        elif text[i] == 'R' and text[i+1] == 'S':
            point_a += 1
        elif text[i] == 'S' and text[i+1] == 'R':
            point_b += 1
    if point_a == point_b:
        print("DRAW", point_a)
    elif point_a > point_b:
        print("A win %d-%d"%(point_a, point_b))
    else:
        print("B win %d-%d"%(point_b, point_a))
main(input(), 0, 0)
