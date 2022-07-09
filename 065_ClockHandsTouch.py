"""ClockHandsTouch"""
def main(hour, minute):
    """calculate clock hand will overlapping or not"""
    h_hand = (hour*30 + minute/2)%360
    m_hand = minute*6
    if h_hand-m_hand <= 6 and h_hand >= m_hand:
        print("True")
    else:
        print("False")
main(int(input()), int(input()))
