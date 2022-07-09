"""CaesarV1"""
def rightshift(shift, text):
    """shift text"""
    shifttext = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                if ord(char)+shift < ord('A'):
                    char = chr(ord(char)+shift+26)
                elif ord(char)+shift > ord('Z'):
                    char = chr(ord(char)+shift-26)
                else:
                    char = chr(ord(char)+shift)
            elif char.islower():
                if ord(char)+shift < ord('a'):
                    char = chr(ord(char)+shift+26)
                elif ord(char)+shift > ord('z'):
                    char = chr(ord(char)+shift-26)
                else:
                    char = chr(ord(char)+shift)
        shifttext += char
    print(shifttext)
rightshift(int(input())%26, input())