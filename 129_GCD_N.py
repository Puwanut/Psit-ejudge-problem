"""GCD_N"""
def allgcn():
    """find gcn of all num"""
    amount = int(input())
    num1 = gcn = int(input())
    for _ in range(amount-1):
        num2 = int(input())
        num1 = gcn = findgcn(max(num1, num2), min(num1, num2))
    return gcn

def findgcn(num1, num2):
    """find gcn of num1 and num2"""
    while num2 != 0:
        num1, num2 = num2, num1%num2
    return num1

print(allgcn())
