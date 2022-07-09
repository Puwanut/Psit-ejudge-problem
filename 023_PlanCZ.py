"""PlanC-Z"""
def main(option, num1, num2, num3):
    """s0rt number and print according to option"""
    if num1 >= num2 >= num3:
        num_high, num_mid, num_low = num1, num2, num3
    elif num1 >= num3 >= num2:
        num_high, num_mid, num_low = num1, num3, num2
    elif num2 >= num1 >= num3:
        num_high, num_mid, num_low = num2, num1, num3
    elif num2 >= num3 >= num1:
        num_high, num_mid, num_low = num2, num3, num1
    elif num3 >= num1 >= num2:
        num_high, num_mid, num_low = num3, num1, num2
    elif num3 >= num2 >= num1:
        num_high, num_mid, num_low = num3, num2, num1
    if option == "Ascend":
        print("%.2f, %.2f, %.2f"%(num_low, num_mid, num_high))
    else:
        print("%.2f, %.2f, %.2f"%(num_high, num_mid, num_low))
main(input(), float(input()), float(input()), float(input()))
