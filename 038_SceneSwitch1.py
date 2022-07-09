"""SceneSwitch I"""
def main():
    """count turn on warm light"""
    light, state = "cool", "on"
    count_warm = 0
    time1 = input()
    if time1 == "End":
        print(count_warm)
    else:
        time1 = float(time1)
        time2 = input()
        while time2 != "End":
            if state == "on":
                state = "off"
            elif state == "off":
                state = "on"
                if float(time2)-time1 <= 6 and light == "cool":
                    light = "warm"
                    count_warm += 1
                else:
                    light = "cool"
            time1 = float(time2)
            time2 = input()
        print(count_warm)
main()
