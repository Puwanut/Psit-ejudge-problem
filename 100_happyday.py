"""HappyDay"""
def main(happypoint, amount):
    """find amount of happy days"""
    pointint = []
    pointstr = happypoint.split(",")
    for i in pointstr:
        pointint.append(int(i))
    for i in range(len(pointint)):
        if pointint[i] >= 80:
            amount += 1
        elif i != 0 and pointint[i] >= 20 and pointint[i]-pointint[i-1] >= 10:
            amount += 1
    print(amount)
main(input(), 0)
