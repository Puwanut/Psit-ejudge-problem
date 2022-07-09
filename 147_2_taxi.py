"""[Final 2019 Recommend] Taxi"""
import math
def taxi_fare():
    """find total taxi fare"""
    total_time_fare = total_distance_fare = kilo_at = 0
    total_fare = 35
    while True:
        data = input()
        if data == 'F':
            break
        datasplit = data.split()
        status = datasplit[0]
        distance = int(datasplit[-1])
        if status == 'W':
            time = int(datasplit[1])
            total_time_fare += time_fare(time)
        fare, kilo_at = distance_fare(distance, kilo_at)
        total_distance_fare += fare

    if total_distance_fare%2 != 1:
        total_distance_fare = math.ceil(total_time_fare) + int(total_time_fare)%2

    if total_time_fare%2 != 0:
        total_time_fare -= total_time_fare%1 + 2

    total_fare += total_time_fare+total_distance_fare
    print(total_fare)

def distance_fare(distance, kilo_at):
    """calculate distance fare"""
    fare = 0
    for _ in range(distance):
        if kilo_at > 80:
            fare += 8.50
        elif kilo_at > 60:
            fare += 7.50
        elif kilo_at > 40:
            fare += 6.50
        elif kilo_at > 20:
            fare += 6
        elif kilo_at > 12:
            fare += 5.50
        elif kilo_at >= 2:
            fare += 5
        kilo_at += 1
    return fare, kilo_at

def time_fare(time):
    """calculate time fare"""
    return time*1.50

taxi_fare()
