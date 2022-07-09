"""[Final 2018 & Final 2019 Recommend] Milk V2"""
def maxmilk():
    """maximum milk can received"""
    price = float(input())
    lid_ex = int(input()) #ex = exchange
    lid_ex_milk = int(input())
    bottle_ex = int(input())
    bottle_ex_milk = int(input())
    money = float(input())

    buy = money//price
    total_milk = lid = bottle = buy
    while lid >= lid_ex or bottle >= bottle_ex:
        milk_fromlid = (lid//lid_ex)*lid_ex_milk
        milk_frombottle = (bottle//bottle_ex)*bottle_ex_milk
        get_milk = milk_fromlid+milk_frombottle
        lid = get_milk + lid%lid_ex
        bottle = get_milk + bottle%bottle_ex
        total_milk += get_milk
    print(int(total_milk))

maxmilk()
