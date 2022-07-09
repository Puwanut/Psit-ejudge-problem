"""Timing II"""
def main(sec):
    """print time format"""
    day = sec//86400
    if day >= 10000:
        print("ERR_:__:__:__")
    else:
        hour = sec%86400//3600
        minute = sec%3600//60
        sec %= 60
        print("%04d:%02d:%02d:%02d" %(day, hour, minute, sec))
main(int(input()))
