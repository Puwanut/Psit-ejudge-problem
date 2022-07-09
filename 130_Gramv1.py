"""Gram_v1"""
def most_2gram(text):
    """show most 2-gram and amount of The most 2-gram"""
    gramdict = {}
    for i in range(len(text)-1):
        twogram = text[i:i+2]
        gramdict[twogram] = gramdict.get(twogram, 0) + 1
    most_value = max(gramdict.values())
    for i in range(len(text)-1):
        twogram = text[i:i+2]
        if gramdict[twogram] == most_value:
            print(twogram)
            print(most_value)
            break
most_2gram(input())
