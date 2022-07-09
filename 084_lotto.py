"""[Midterm 2019] Lotto"""
def main(total_prize):
    """find total prize"""
    first = input()
    last2 = input()
    front3_1, front3_2 = input(), input()
    last3_1, last3_2 = input(), input()
    mylotto = input()
    if first == "000000":
        nearfirst1 = "000001"
        nearfirst2 = "999999"
    elif first == "999999":
        nearfirst1 = "000000"
        nearfirst2 = "999998"
    else:
        nearfirst1 = "%06d"%(int(first)+1)
        nearfirst2 = "%06d"%(int(first)-1)
    if mylotto == first:
        total_prize += 6000000
    if mylotto[4:] == last2:
        total_prize += 2000
    if mylotto[:3] == front3_1:
        total_prize += 4000
    if mylotto[:3] == front3_2:
        total_prize += 4000
    if mylotto[3:] == last3_1:
        total_prize += 4000
    if mylotto[3:] == last3_2:
        total_prize += 4000
    if mylotto == nearfirst1 or mylotto == nearfirst2:
        total_prize += 100000
    print(total_prize)
main(0)
