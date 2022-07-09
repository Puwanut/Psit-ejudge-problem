"""FoodGrade II"""
def chickeninbox(capacity, weight_chicken):
    """find amount of chicken wings that can put into box"""
    allweight = [int(i) for i in weight_chicken.split()]
    allweight.sort()
    inbox = 0
    count = 0
    for weight in allweight:
        if weight+inbox <= capacity:
            inbox += weight
            count += 1
    print(count)
chickeninbox(int(input()), input())
