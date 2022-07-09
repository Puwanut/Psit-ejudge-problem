"""AlmostMean"""
def main(amount):
    """find maximum point before Mean"""
    sid_list, point_list = [], []
    for _ in range(amount):
        sid, point = input().split("\t")
        sid_list.append(sid)
        point_list.append(float(point))
    point_mean = sum(point_list)/amount
    point_max = 0 #max before mean
    for point in point_list:
        if point > point_max and point < point_mean:
            point_max = point
    index = point_list.index(point_max)
    print(sid_list[index] + "\t" + str(point_max))
main(int(input()))
