"""[Final 2019 Recommend] Kayak"""
def lowest_difference(num, peopleweight):
    """find total lowest difference weight of kayak_2seat"""
    weight = sorted(map(int, peopleweight.split()))
    kayak_2seat = num-1
    total_difference = 0
    for _ in range(kayak_2seat):
        difference_list = []
        for i in range(len(weight)-1):
            difference = abs(weight[i]-weight[i+1])
            difference_list.append(difference)
        min_dif = min(difference_list)
        total_difference += min_dif
        indexweight = difference_list.index(min_dif)
        weight.remove(weight[indexweight])
        weight.remove(weight[indexweight])
    print(total_difference)

lowest_difference(int(input()), input())
