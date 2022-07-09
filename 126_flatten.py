"""flatten"""
import json
def flatten(numlist):
    """flattened num list"""
    anslist = []
    while numlist != []:
        if isinstance(numlist[0], list):
            numlist.extend(numlist.pop(0))
        else:
            anslist.append(numlist.pop(0))
    anslist.sort(reverse=True)
    print(anslist)
flatten(json.loads(input()))
