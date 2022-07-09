"""Key"""
def main(idnum, total):
    """calculate key 4 digit"""
    for i in idnum:
        total += int(i)
    value = int(idnum[10:])*10
    key = total + value
    if key >= 10000:
        key = str(key)[-4:]
    elif key < 1000:
        key += 1000
    print(key)
main(input(), 0)
