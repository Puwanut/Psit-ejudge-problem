"""[Final 2019 Recommend] Taxi"""
import math
def taxi_fare():
    """find total taxi fare"""
    total_time_fare = total_distance_fare = kilo_now = 0
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
        total_distance_fare += distance_fare(distance+kilo_now)
        kilo_now += distance

    if total_distance_fare%2 != 1:
        total_distance_fare = math.ceil(total_time_fare) + int(total_time_fare)%2
    if total_time_fare%2 != 0:
        total_time_fare -= total_time_fare%1 + 2
    total_fare += total_time_fare+total_distance_fare
    print(total_fare)

def distance_fare(distance):
    """calculate distance fare"""
    fare = 0
    if distance > 80:
        fare += 8.50*(distance-80)
        distance = 80
    if distance > 60:
        fare += 7.50*(distance-60)
        distance = 60
    if distance > 40:
        fare += 6.50*(distance-40)
        distance = 40
    if distance > 20:
        fare += 6*(distance-20)
        distance = 20
    if distance > 12:
        fare += 5.50*(distance-12)
        distance = 12
    if distance >= 2:
        fare += 5*(distance-1)
    return fare

def time_fare(time):
    """calculate time fare"""
    return time*1.50

taxi_fare()
