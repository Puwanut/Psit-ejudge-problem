"""Refrigerator"""
def keepday(_):
    """find maximum keep food day until spoiled"""
    foods = [int(food) for food in input().split()]
    days = 0
    while 0 not in foods:
        foods = [food-1 for food in foods]
        least = foods.index(min(foods))
        foods[least] += 1
        days += 1
    print(days)
keepday(int(input()))
