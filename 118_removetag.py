"""RemoveTag"""
def removetag(text):
    """show list of removed tag text"""
    word = ""
    wordlist = []
    intag = False
    for char in text+'<':
        if char == '<':
            intag = True
            wordlist.extend(word.split())
            word = ""
        elif char == '>':
            intag = False
        elif not intag:
            word += char
    print(wordlist)
removetag(input())
