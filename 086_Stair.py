"""[Midterm 2019] Stair"""
def main(mystep, amount):
    """find the least step to 2nd floor"""
    count_up = 0 #จำนวนขั้นบันไดที่ขึ้น
    count_step = 0 #จำนวนก้าว
    last = 0
    for _ in range(amount):
        height = int(input())
        if mystep < height+last:
            count_step += 1
            last = 0
        if mystep > height+last:
            count_up += 1
            last += height
        elif mystep == height+last:
            count_up += 1
            count_step += 1
            last = 0
        else:
            last = mystep+1
    if mystep >= height and last != 0:
        count_step += 1
    if count_up != amount:
        print("NO")
    else:
        print(count_step)
main(int(input()), int(input()))
