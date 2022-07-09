"""SMS"""
def send_sms(amount):
    """print sms"""
    char = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    sms = ''
    for _ in range(amount):
        button = int(input())
        times = int(input())
        if button != 1:
            sms += char[button-2][(times-1)%len(char[button-2])]
        elif button == 1 and len(sms) > 0:
            sms = sms[:max(0, len(sms)-times)]
    if len(sms) == 0:
        print('null')
    else:
        print(sms)
send_sms(int(input()))
