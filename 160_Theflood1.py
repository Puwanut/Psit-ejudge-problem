"""TheFlood I"""
def keeptimes():
    """find maximum times flood"""
    heights = [int(height) for height in input().split()]
    times = 0
    while 0 not in heights:
        heights = [height-1 for height in heights]
        least = heights.index(min(heights))
        heights[least] += 1
        times += 1
    print(times)
keeptimes()
