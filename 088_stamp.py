"""[Midterm 2019] Stamps"""
def main():
    """find total cost and remain stamps"""
    times = int(input())
    get_pro, get_stamp = int(input()), int(input())
    prostamp, discount = int(input()), int(input())
    mystamp = total_cost = 0
    for _ in range(times):
        bill = int(input())
        while mystamp >= prostamp and bill > 0:
            mystamp -= prostamp
            bill -= discount
            if bill < 0:
                bill = 0
        mystamp += (bill//get_pro)*get_stamp
        total_cost += bill
    print(total_cost, mystamp, sep="\n")
main()
