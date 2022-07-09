"""Diginity_Midterm2014"""
def main(rfid, total):
    """show result of calculating"""
    while rfid != 0:
        while rfid >= 10:
            for i in str(rfid):
                total += int(i)
            rfid = total
            total = 0
        print(rfid)
        rfid = int(input())
main(int(input()), 0)
