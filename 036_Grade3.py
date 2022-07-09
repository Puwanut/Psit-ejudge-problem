"""Grade III"""
def main(amount):
    """find gpa"""
    total = 0
    for _ in range(amount):
        point = float(input())
        total += calgrade(point)
    gpa = int((total/amount)*100)/100
    print("%.2f"%gpa)

def calgrade(point):
    """calculate grade"""
    if 95 <= point <= 100:
        grade = 4
    elif point >= 90:
        grade = 3.5
    elif point >= 85:
        grade = 3
    elif point >= 80:
        grade = 2.5
    elif point >= 75:
        grade = 2.0
    elif point >= 70:
        grade = 1.5
    elif point >= 65:
        grade = 1
    elif point >= 60:
        grade = 0.5
    else:
        grade = 0
    return grade

main(int(input()))
