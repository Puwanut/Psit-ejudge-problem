"""Difference"""
import json
def difference(list_a, list_b):
    """Find difference of list a and list b"""
    dif_dict = {}
    union_set = set(list_a).union(set(list_b))
    for item in union_set:
        item_a = list_a.count(item)
        item_b = list_b.count(item)
        if item_a != item_b:
            dif_dict[item] = abs(item_a-item_b)
    dif_list = sorted(dif_dict)
    if len(dif_list) == 0:
        print("ONAJI DAYO!")
    else:
        for item in dif_list:
            print(item, dif_dict[item])

difference(json.loads(input()), json.loads(input()))
