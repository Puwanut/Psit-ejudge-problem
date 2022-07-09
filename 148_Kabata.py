"""Kabata"""
def iskabata(text):
    """return True if text if text is Kabata language"""
    if 'baka' in text:
        return False
    for sound in ['bakka', 'ka', 'ba', 'ta']:
        text = text.replace(sound, '')
    if len(text) == 0:
        return True
    return False

def kabata_check(amount):
    """Show result of checking"""
    for _ in range(amount):
        if iskabata(input()):
            print('yes')
        else:
            print('no')

kabata_check(int(input()))
