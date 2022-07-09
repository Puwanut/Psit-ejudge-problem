"""WeightStation"""
def main(weight_avg, weight1, weight2, weight3):
    """check weight and balance of truck"""
    weight4 = 4*weight_avg-weight1-weight2-weight3
    if weight1+weight2+weight3+weight4 > 15000:
        print("Overweight")
    elif weight1 <= weight_avg-weight_avg/2 or weight1 >= weight_avg+weight_avg/2:
        print("Unbalance")
    elif weight2 <= weight_avg-weight_avg/2 or weight2 >= weight_avg+weight_avg/2:
        print("Unbalance")
    elif weight3 <= weight_avg-weight_avg/2 or weight3 >= weight_avg+weight_avg/2:
        print("Unbalance")
    elif weight4 <= weight_avg-weight_avg/2 or weight4 >= weight_avg+weight_avg/2:
        print("Unbalance")
    else:
        print("Pass %.2f"%weight4)
main(float(input()), float(input()), float(input()), float(input()))
