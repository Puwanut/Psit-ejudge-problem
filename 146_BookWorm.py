"""BookWorm"""
def all_read(test):
    """Show maximum books can read in each test"""
    for _ in range(test):
        alltime = float(input())
        books = int(input())
        print(max_read(alltime, books))

def max_read(alltime, books):
    """find max of books can read in time"""
    total_time = total_book = 0
    read_time = [float(input()) for _ in range(books)]
    read_time.sort()
    for time in read_time:
        if total_time+time <= alltime:
            total_time += time
            total_book += 1
        else:
            break
    return total_book

all_read(int(input()))
